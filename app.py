from flask import Flask, jsonify, Response, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import logger
import argparse
import json


app = Flask(__name__)


@app.route("/personal/health", methods=["GET"])
def health():
    logger.info("HealthCheck API")
    return jsonify({"status": "up"})


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource="admin")
    db = client["personaldetails_db"]
    return db


def create_person(person):
    db = get_db()
    db_response = db.personaldetails_tb.insert_one(person)
    print("Person created successfully!")
    print(db_response.inserted_id)
    uid = str(db_response.inserted_id)
    return uid


def read_person(unique_id):
    db = get_db()
    person = db.personaldetails_tb.find_one({"unique_id": unique_id})
    print("Person read successfully!")
    print(person)


def update_person(unique_id, updated_data):
    db = get_db()
    db_response = db.personaldetails_tb.update_one(
        {"_id": ObjectId(unique_id)},
        {"$set": updated_data}
    )
    if db_response.modified_count == 1:
        print("Person updated successfully!")
        logger.info("The address of {} has been successfully updated to {}".format(unique_id, updated_data))
    else:
        print("Person update failed!")
        logger.info("NOTHING was updated")


def delete_person(unique_id):
    db = get_db()
    db_response = db.personaldetails_tb.delete_one({"_id": ObjectId(unique_id)})
    logger.info("The record {} is being deleted from the personal details collection".format(unique_id))
    if db_response.deleted_count == 1:
        print("Person deleted successfully!")
        logger.info("The record {} was SUCCESSFULLY deleted from the collection".format(unique_id))
    else:
        print("Person deletion failed!")
        # logger.info("NOTHING was deleted")


@app.route("/getpersonaldata", methods=["GET"])
def get_personal_details():
    logger.info("Get All the Personal Details API")
    db = get_db()
    try:
        personal_details = list(db.personaldetails_tb.find())
        print(personal_details)
        logger.info(personal_details)
        for person in personal_details:
            person["_id"] = str(person["_id"])
        return Response(
            response=json.dumps(personal_details),
            status=200,
            mimetype="application/json"
        )

    except Exception as E:
        print(E)
        logger.info("Couldn't fetch the personal details due to {}".format(E))
        return Response(
            response=json.dumps({"message": "Could NOT fetch personal details!"}),
            status=500,
            mimetype="application/json"
        )


@app.route("/personal/crud", methods=["GET"])
def do_basic_crud():
    logger.info("Perform Basic Crud Operations API")
    new_person = {"first_name": "Will",
                  "last_name": "Chad",
                  "age": 44,
                  "address": "56 Side St",
                  "contact_number": "+1234564564",
                  "nationality": "USA"}

    uid = create_person(new_person)
    read_person(uid)
    update_person(uid, {"age": 31})
    # delete_person(uid)
    return Response(
        response=json.dumps({"Status": "Crud Operations Successful"}),
        status=200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sys_args = parser.parse_args()
    app.run(host='0.0.0.0', port=8080)


