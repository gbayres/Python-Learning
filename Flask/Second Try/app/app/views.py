from app import app
from flask import render_template
from flask import request, redirect
from flask import jsonify, make_response
import os
from werkzeug.utils import secure_filename
from flask import send_file, send_from_directory, safe_join, abort
from flask import session, url_for


def allowed_image(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/")
def index():
    cookies = request.cookies
    flavor = cookies.get("flavor")
    print(flavor)
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

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)

        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "password": "example",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "password": "python",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk",
        "password": "tesla",
    }
}

@app.route("/profile/<username>")
def public_profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar, baz):

    print(f"foo is {foo}")
    print(f"bar is {bar}")
    print(f"baz is {baz}")


    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["POST"])
def json_example():

    if request.is_json:

        req = request.get_json()

        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")

        }

        res = make_response(jsonify(response_body), 200)


        return res

    else:

        return make_response(jsonify({"message": "Request boy must be JSON"}), 400)

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "OK"}), 200)

    return res
    
@app.route("/query")
def query():

    if request.args:

        # We have our query string nicely serialized as a Python dictionary
        args = request.args

        # We'll create a string to display the parameters & values
        serialized = ", ".join(f"{k}: {v}" for k, v in request.args.items())

        # Display the query string to the client in a different format
        return f"(Query) {serialized}", 200

    else:

        return "No query string received", 200 

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    if request.method == "POST":

        if request.files:

            if 'filesize' in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exeeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)
                    path = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
                    image.save(path)
                    print("Image saved!")
                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)


    return render_template("public/upload_image.html")


@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(app.config["CLIENT_IMAGES"], filename=image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/get-csv/<csv_id>")
def get_csv(csv_id):
    filename = f"{csv_id}.csv"
    try:
        return send_from_directory(app.config["CLIENT_CSV"], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/get-pdf/<pdf_id>")
def get_pdf(pdf_id):
    filename = f"{pdf_id}.pdf"

    try:
        return send_from_directory(app.config['CLIENT_PDF'], filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/get-report/<path:path>")
def get_report(path):
    try:
        return send_from_directory(app.config["CLIENT_REPORTS"], filename=path, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route("/cookies")
def cookies():
    print(request.path)
    resp = make_response("Cookies")
    resp.set_cookie(
        "flavor", 
        "chocolate chip",
        max_age=10,
        path=request.path
        )
    return resp

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        print(username)
        password = req.get("password")

        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]
        
        if password != user["password"]:
            print("Incorret password")
            return redirect(request.url)
        else:
            session["USERNAME"] = username #user["username"]
            print("session username set")
            return redirect(url_for("profile2"))
    
    return render_template("public/sign_in.html")

@app.route("/profile2")
def profile2():
    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]
        return render_template("public/profile2.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("sign_in"))
    
@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME", None)
    return redirect(url_for("sign_in"))