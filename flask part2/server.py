# Import the Flask class from the flask module
from flask import Flask, make_response, request

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

# Send custom HTTP code back with a tuple.
@app.route("/no_content")
def no_content():
    return {"message" : "No content found"}, 204

# Send custom HTTP code back with the make_response() method.
@app.route("/exp")
def index_explicit():
    res = make_response({"message" : "Hello World"})
    res.status_code = 200
    return res


## Step 2 : process input arguments

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]



@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404


@app.route("/name_search")
def name_search():
    # Find a person in the database.
    # Returns:
    #     json: Person if found, with status of 200
    #     404: If not found
    #     422: If argument 'q' is missing
    query = request.args.get('q')

    if not query:
        return {"message": "Query parameter 'q' is missing"}, 422
    
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person['first_name'].lower():
            return person
    
    return {"message": "Person not found"}, 404


## Step 3: Add dynamic URLs
@app.get("/count")
def count():
    try:
        return {"data count" : len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        # Return a JSON response with a message and a 500 Internal Server Error status code
        return {"message": "data not defined"}, 500

@app.get("/person/<uuid:unique_identifier>")
def find_by_uuid(unique_identifier):
    # return JSON if found
    # return 404 if person not found
    # only able to call this method by passing a valid UUID type id.

    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'var_name' parameter
        if person['id'] == str(unique_identifier):
            return person

    return {'message' : "Person not found"}, 404

@app.route("/person/<uuid:uuid>", methods=["DELETE"])
def delete_by_uuid(uuid):

    for person in data:
        if person['id'] == str(uuid):
            #delete
            data.remove(person)
            return {"message" : f"Person with {uuid} deleted"}, 200
    
    return {"message" : "Person not found"}, 404

# Step 4 : Parse JSON from request body


@app.route("/person", methods = ['POST'])
def add_by_uuid():
    # person id if the person was successfully added to data; HTTP 200 code
    # message of Invalid input parameter with a status of HTTP 422 if the json body is missing

    # Get the JSON data from the incoming request
    new_person = request.get_json()

    # Check if the JSON data is empty or None
    if not new_person:
        # Return a JSON response indicating that the request data is invalid or missing
        # with a status code of 400 (Bad Request)
        return {"message": "Invalid input, no data provided"}, 400
    
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200

#step 5 - Add error handlers

@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404

