from flask import Flask, redirect

app=Flask(__name__)

@app.route("/about_me")
def about_me():
    return """Name: Do Nghiem Duc
    Age: 15
    School: Chu Van An"""

@app.route("/school")
def school():
    return redirect("http://techkids.vn")

if __name__ == "__main__":
    app.run(debug=True)


