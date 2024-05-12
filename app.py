from flask import Flask,request

app = Flask(__name__)

# creating idea repository
ideas = {
    1 : {
        "id": 1,
        "Idea name": "ONDC",
        "idea description" : "Details about ONDC",
        "Idea name" : "Aman"
    },
    2 : {
        "id": 2,
        "Idea name": "Climate change",
        "idea description" : "Details about climate change",
        "Idea name" : "Bisht"
    }
}

# create a restful api for fetching all details
@app.get("/ideaapp/api/v1/ideas")
def get_all_ideas():
    return ideas
 


#create a restful API for creating new idea
@app.post("/ideaapp/api/v1/ideas")
def create_idea():
    try:
        # logic to create new idea
        
        # first read the request body
        request_body = request.get_json()

        #check if the id passed is already in the ideas
        if request_body["id"] and request_body["id"] in  ideas():

            return {"message": "Idea already exists with the given id"}, 400
    
        #insert the passed idea in the directory
        ideas[request_body["id"]] = request_body

        return {"message": "Idea created successfully"}, 201
    except KeyError:
        return "id is missing", 400
    except:
        return "some internal server error loser",500

    

if __name__ == '__main__':
    app.run(port=8080)

    