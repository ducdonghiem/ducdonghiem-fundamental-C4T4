from flask import *
import mlab
from models.users_feedback import Feedback
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/feedback", methods = ["GET", "POST"])
def feedback():
    if request.method == 'GET':
        return render_template("feedback.html")
    elif request.method == "POST":
        form = request.form
        name = form['name']
        stt = form['stt']
        
        content = form['content']
        mlab.connect()
        feedback = Feedback(name = name, stt = stt, content = content, post = False)
        feedback.save()
        return redirect(url_for("comment"))
@app.route("/comment", methods = ["GET","POST"])
def comment():
    mlab.connect()
    feedback_list = Feedback.objects()
    if request.method == 'GET':
        return render_template("comment.html", feedback_list = feedback_list)
    





    

if __name__ == "__main__":
    app.run(debug=True)
