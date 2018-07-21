from flask import Flask
app=Flask(__name__)

@app.route("/users/<username>")

def users(username):
    users={
    "Huy": {
        "Name": "Nguyen Quang Huy",
        "Age": "29"
        },
    "Don": {
        "Name": "Don Zoombie",
        "Age": "23"
        },
    "Duc": {
        "Name": "Do Nghiem Duc", 
        "Age": "15"
        }
    }
    if username in users.keys():
        return ("Name: " + users[username]["Name"] + "\t" 
        + "Age: " + users[username]["Age"])
        
    else:
        return "User not found"    

if __name__ == "__main__":
    app.run(debug=True)