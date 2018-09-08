from flask import *
import mlab
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
