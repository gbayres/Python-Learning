@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("public/sign_up.html")


    
