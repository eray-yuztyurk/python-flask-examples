"""
Flask REST API Example
----------------------

This project is a simple demonstration of a Flask-based REST API.  
It is designed for learning, testing, and showcasing common API features such as:

- Basic GET, POST, and DELETE endpoints
- Searching data using query parameters
- UUID-based resource lookup and deletion
- Custom 404 handler and global exception handler
- Use of `make_response` and tuple-based responses
- In-memory sample dataset (Germany & Austria user records)

The application is intentionally minimal and focuses on core REST principles,  
error handling, and clean endpoint design. It can serve as a foundation for  
larger Flask applications or educational tutorials.

"""
#---------------------------------------------------------------------------------------

# Import the Flask class from the flask module, also make_response and request
from flask import Flask, make_response,request

# Create an instance of the Flask class
app = Flask(__name__)

########################################################################################
# Defining a route for the root URL ("/") - Using string as return
########################################################################################
@app.route("/")
def index():
    return "hello world!"

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' localhost:5000

>>>
HTTP/1.1 200 OK
Server: Werkzeug/3.1.3 Python/3.11.14
Date: Fri, 28 Nov 2025 20:07:47 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: close

hello world!
'''
########################################################################################
# Return using tuple as return ("/no_content")
########################################################################################
@app.route("/no_content")
def no_content(): 
    """return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """ 
    #return make_response({"message":"No content found"})
    return ({"message":"No content found"},204)

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' localhost:5000/no_content
'''
########################################################################################
# Return using make_response ("/exp") 
########################################################################################
@app.route("/exp")
def index_explicit():
    resp = make_response({"message":"success"}) # -> status_code included
    resp.status_code = 200
    return resp

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' localhost:5000/exp
'''
########################################################################################
# Adding User Sample Data
########################################################################################
data = [
    {
        "id": "b83c29c1-92c0-4c9c-9c4f-4cd2a52f3f10",
        "first_name": "Lukas",
        "last_name": "Meyer",
        "graduation_year": 2003,
        "address": "Hauptstraße 27",
        "city": "Berlin",
        "zip": "10117",
        "country": "Germany",
        "avatar": "http://dummyimage.com/150x100.png/0044aa/ffffff"
    },
    {
        "id": "f1d2983d-470e-4fd9-9e00-0b7b4b2b530a",
        "first_name": "Anna",
        "last_name": "Schubert",
        "graduation_year": 1994,
        "address": "Marktplatz 11",
        "city": "Hamburg",
        "zip": "20095",
        "country": "Germany",
        "avatar": "http://dummyimage.com/160x100.png/aa0000/ffffff"
    },
    {
        "id": "c9eb0afe-e645-407b-a664-ddee3e7f87c5",
        "first_name": "Fabian",
        "last_name": "Gruber",
        "graduation_year": 1987,
        "address": "Mozartgasse 8",
        "city": "Wien",
        "zip": "1010",
        "country": "Austria",
        "avatar": "http://dummyimage.com/180x100.png/ffaa00/000000"
    },
    {
        "id": "2c1b92dd-2ea3-43cf-b734-91afeb2ce56e",
        "first_name": "Sophie",
        "last_name": "Huber",
        "graduation_year": 2001,
        "address": "Lindengasse 42",
        "city": "Graz",
        "zip": "8010",
        "country": "Austria",
        "avatar": "http://dummyimage.com/140x100.png/33cc33/ffffff"
    },
    {
        "id": "77f3fa41-3898-4642-8fce-42b4a49a1c8b",
        "first_name": "Jonas",
        "last_name": "Fechter",
        "graduation_year": 1980,
        "address": "Bergstraße 5",
        "city": "München",
        "zip": "80331",
        "country": "Germany",
        "avatar": "http://dummyimage.com/190x100.png/990099/ffffff"
    }
]
########################################################################################
# Returning count of users in data ("/data")
########################################################################################
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message":f"User count in data is {len(data)}"}

        else:
            return {"message":"Data is empty"}, 500
    
    except NameError:
        return {"message":"Data is not found"}, 404

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' localhost:5000/data
'''
########################################################################################
# Searching user in data ("/name_search") using query - "q" parameter
########################################################################################
@app.route("/name_search")
def name_search():
    """Find a person in the database.
    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If argument 'q' is missing
        422: If argument 'q' is present but invalid
    """

    query = request.args.get("q")

    if query is None:
        return {"message":"Query parameter 'q' is missing"}, 400

    if query.strip() == "" or query.isdigit():
        return {"message":"Invalid input parameter"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    return {"message":"Person has not been found"}, 404

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' "localhost:5000/name_search?q=Lukas"

>>>
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 21:14:31 GMT
Content-Type: application/json
Content-Length: 295
Connection: close

{
  "address": "Hauptstraße 27",
  "avatar": "http://dummyimage.com/150x100.png/0044aa/ffffff",
  "city": "Berlin",
  "country": "Germany",
  "first_name": "Lukas",
  "graduation_year": 2003,
  "id": "b83c29c1-92c0-4c9c-9c4f-4cd2a52f3f10",
  "last_name": "Meyer",
  "zip": "10117"
}
'''
#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' "localhost:5000/name_search?q="

>>>
{
  "message": "Invalid input parameter"
}
'''
#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"

>>>
{
  "message": "Person has not been found"
}
>>>
'''
########################################################################################
# Return total number of users in data ("/count") 
########################################################################################
@app.get("/count")
def count():
    try:
        return {"message":f"Total person count in data is {len(data)}"}, 200

    except NameError:
        return {"message":"Data is not found"}, 500

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i -w '\n' "localhost:5000/count"
'''
########################################################################################
# Getting user info with uuid using REST based API ("/person/<type:variable_name>") 
########################################################################################
@app.get("/person/<uuid:UUID>")
def find_by_uuid(UUID):

    for person in data:
        if person["id"] == str(UUID):
            return person, 200

    return {"message":"Person has not been found"}, 404

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i localhost:5000/person/b83c29c1-92c0-4c9c-9c4f-4cd2a52f3f10
'''
#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X GET -i localhost:5000/person/not-a-valid-uuid

>>>
{
  "message": "API is not found"
}
'''
########################################################################################
# Deleting user info with uuid using REST based API ("/person/<type:variable_name>") 
########################################################################################
@app.delete("/person/<uuid:UUID>")
def delete_by_uuid(UUID):

    for person in data:
        if person["id"] == str(UUID):
            data.remove(person)
            return {"message":f"Person with ID of {UUID} is deleted."}, 200

    return {"message":"Person has not been found"}, 404

#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X DELETE -i localhost:5000/person/b83c29c1-92c0-4c9c-9c4f-4cd2a52f3f10

>>>
{
  "message": "Person with ID of b83c29c1-92c0-4c9c-9c4f-4cd2a52f3f10 is deleted."
}
'''
########################################################################################
# Defining a route for the root URL ("/")
########################################################################################
@app.post("/person")
def add_person():

    new_user = request.get_json()

    if not new_user:
        return {"message":"No data has been provided or invalid parameters"}, 422

    try:
        data.append(new_user)
        return {"message":f"User has been added to the data.{new_user}"}, 201

    except NameError:
        return {"message":"User could not be saved to data"}, 500
#---------------------------------------------------------------------------------------
'''
Terminal >>>

curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "Max",
        "last_name": "Keller",
        "graduation_year": 2005,
        "address": "Ringstraße 10",
        "city": "Wien",
        "zip": "1010",
        "country": "Austria",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

Terminal >>>
curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{}'
'''
########################################################################################
# 404 Error Handler
########################################################################################
@app.errorhandler(404)
def api_not_found(error):

    return {"message": "API is not found"}, 404
    
#---------------------------------------------------------------------------------------
'''
Terminal >>>
curl -X POST -i -w '\n' http://localhost:5000/notvalid
'''
########################################################################################
# Global Error Handler
########################################################################################
@app.errorhandler(Exception)
def handle_exceptions(error):
    return {"message":str(error)}, 500

########################################################################################
# Raise Exception Error
########################################################################################
@app.route("/testing500")
def testing500():
    raise Exception("Test for exception error!")

#---------------------------------------------------------------------------------------
'''
Terminal >>>
curl http://localhost:5000/testing500
'''
#---------------------------------------------------------------------------------------
