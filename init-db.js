db = db.getSiblingDB("personaldetails_db");
db.personaldetails_tb.drop();

db.personaldetails_tb.insertMany([
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "address": "123 Main St",
        "contact_number": "+1234567890",
        "nationality": "USA"
    },
    {
        "first_name": "David",
        "last_name": "Ham",
        "age": 33,
        "address": "456 10th St",
        "contact_number": "+9876543210",
        "nationality": "USA"
    },
    {
        "first_name": "Ana",
        "last_name": "Han",
        "age": 36,
        "address": "123 Cha St",
        "contact_number": "+1234987650",
        "nationality": "USA"
    },
    {
        "first_name": "Dale",
        "last_name": "Steyn",
        "age": 40,
        "address": "43 Wicket St",
        "contact_number": "+1231231231",
        "nationality": "USA"
    }
])