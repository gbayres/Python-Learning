from app import app
from flask import render_template
from flask import request, redirect

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/jinja")
def jinja():
    return render_template("public/jinja.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        print(list(request))

        return redirect(request.url)
        
    return render_template("public/sign_up.html")
