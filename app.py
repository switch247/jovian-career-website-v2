from flask import Flask, render_template, jsonify,render_template, redirect, request, session
from flask_session import Session
from database import from_database,from_database_job,add_application_to_db

# from flask_minify import minify

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# initializing minify for html, js and cssless
# minify(app=app, html=True, js=True, cssless=True)
# minify(self, app=None, html=True, js=True, cssless=True, fail_safe=True, bypass=[], passive=False, static=True, script_types=[])

@app.route("/")
def hello_world():
  # check if the users exist or not
    # if not session.get("name"):
        # if not there in the session then redirect to the login page
        # return redirect("/login")
  JOBS =from_database()
  if not JOBS:
     return "Not Found", 404
  
  return render_template("home.html",jobs=JOBS,comp_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  JOBS =from_database()
  return jsonify(JOBS)
@app.route("/api/job/<int:id>")
def show_job_json(id):
  JOB =from_database_job(id)
  return jsonify(JOB)

@app.route("/job/<int:id>")
def show_job(id):
  JOBS =from_database_job(id)
  # return jsonify(JOBS)
  return render_template("jobpage.html",job=JOBS)

@app.route("/job/<int:id>/apply",methods=["POST"])
def apply_job(id):
  if request.method == "POST":
    data =request.form
    job =from_database_job(id)
    add_application_to_db( id , data)
    # .args for get method
    # return jsonify(data)
    return render_template('applicationsubmited.html',application=data,job=job)









@app.route("/login", methods=["POST", "GET"])
def login():
    # if form is submited
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("name")
        # redirect to the main page
        return redirect("/")
    return render_template("login.html")
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
@app.route("/test/<int:age>")
def vint(age):
    return "I am %d years old " % age






if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
