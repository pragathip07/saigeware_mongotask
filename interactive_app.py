# from flask import Flask, jsonify, Response, request
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# # from config import logger
# import json
#
#
# app = Flask(__name__)
#
#
# def get_db():
#     client = MongoClient(host='test_mongodb',
#                          port=27017,
#                          username='root',
#                          password='pass',
#                          authSource="admin")
#     db = client["personaldetails_db"]
#     return db
#
#
# @app.route('/')
# def ping_server():
#     return "Welcome to the personal details."
#
#
# @app.route("/personal/health", methods=["GET"])
# def health():
#     # logger.info("HealthCheck API")
#     return jsonify({"status": "up"})
#
#
# @app.route("/personal", methods=["GET"])
# def get_personal_details():
#     db = get_db()
#     try:
#         personal_details = list(db.personaldetails_tb.find())
#         print(personal_details)
#         # logger.info(personal_details)
#         for person in personal_details:
#             person["_id"] = str(person["_id"])
#         return Response(
#             response=json.dumps(personal_details),
#             status=200,
#             mimetype="application/json"
#         )
#
#     except Exception as E:
#         print(E)
#         # logger.info("Couldn't fetch the personal details due to {}".format(E))
#         return Response(
#             response=json.dumps({"message": "Could NOT fetch personal details!"}),
#             status=500,
#             mimetype="application/json"
#         )
#
#
# @app.route("/personal/create", methods=["POST"])
# def create_new_personal_data():
#     try:
#         db = get_db()
#         person = {"first_name": "Will",
#                   "last_name": "Chad",
#                   "age": 44,
#                   "address": "56 Side St",
#                   "contact_number": "+1234564564",
#                   "nationality": "USA"}
#
#         # person = {
#         #     "first_name": request.form["first_name"],
#         #     "last_name": request.form["last_name"],
#         #     "age": request.form["age"],
#         #     "address": request.form["address"],
#         #     "contact_number": request.form["contact_number"],
#         #     "nationality": request.form["nationality"]
#         # }
#
#         # logger.info("The new personal data being created : {}".format(person))
#
#         db_response = db.personaldetails_tb.insert_one(person)
#         # logger.info("New personal data successfully added, and here's the unique ID : {}".format(db_response.inserted_id))
#         print(db_response.inserted_id)
#
#         return Response(
#             response=json.dumps(
#                 {
#                     "message": "New personal data was SUCCESSFULLY CREATED",
#                     "id": f"{db_response.inserted_id}"
#                 }
#             ),
#             status=200,
#             mimetype="application/json"
#         )
#
#     except Exception as E:
#         print("Error : ", E)
#         return Response(
#             response=json.dumps({"message": "The creation has FAILED!", "error": str(E)}),
#             status=500,
#             mimetype="application/json"
#         )
#
#         # logger.info("The personal data could NOT be created as expected due to {}".format(E))
#
#
# @app.route("/personal/<uid>", methods=["PATCH"])
# def update_personal_details(uid):
#     try:
#         db = get_db()
#         db_response = db.personaldetails_tb.update_one(
#             {"_id": ObjectId(uid)},
#             {"$set": {"address": request.form["new_address"]}}
#         )
#
#         # logger.info("The address of {} is being updated".format(uid))
#
#         if db_response.modified_count == 1:
#             # logger.info("The address of {} has been successfully updated to {}".format(uid, request.form["new_address"]))
#             return Response(
#                 response=json.dumps({"message": "Done! Personal Data Updated SUCCESSFULLY!"}),
#                 status=200,
#                 mimetype="application/json"
#             )
#         # logger.info("NOTHING was updated")
#         return Response(
#             response=json.dumps({"message": "NOTHING To Update!"}),
#             status=200,
#             mimetype="application/json"
#         )
#
#     except Exception as E:
#         print("****************************************")
#         print(E)
#         print("****************************************")
#
#         return Response(
#             response=json.dumps({"message": "The update has FAILED!"}),
#             status=500,
#             mimetype="application/json"
#         )
#
#
# @app.route("/personal/<uid>", methods=["DELETE"])
# def delete_personal_data(uid):
#     try:
#         db = get_db()
#         db_response = db.personal_details.delete_one({"_id": ObjectId(uid)})
#         # logger.info("The record {} is being deleted from the personal details collection".format(uid))
#         if db_response.deleted_count == 1:
#             # logger.info("The record {} was SUCCESSFULLY deleted from the collection".format(uid))
#             return Response(
#                 response=json.dumps(
#                     {
#                         "message": "The personal data was deleted SUCCESSFULLY!",
#                         "id": f"{uid}"
#                     }
#                 ),
#                 status=200,
#                 mimetype="application/json"
#             )
#         # logger.info("NOTHING was deleted")
#         return Response(
#             response=json.dumps(
#                 {
#                     "message": "personal data with this particular unique ID was NOT FOUND!",
#                     "id": f"{uid}"
#                 }
#             ),
#             status=200,
#             mimetype="application/json"
#         )
#
#     except Exception as E:
#         print("****************************************")
#         print(E)
#         print("****************************************")
#
#         # logger.info("The deletion of personal data has FAILED ")
#         return Response(
#             response=json.dumps({"message": "The deletion of the personal data has been FAILED!"}),
#             status=500,
#             mimetype="application/json"
#         )
#
#
# # ======================================================================================================================
#
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=8080)
#
