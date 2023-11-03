from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/", methods=["GET"])
def redirect_external():
    return redirect("/home", code=302)



@app.route("/home")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/elon2", methods=['POST', 'GET'])
def greeter():
	flash("Hi, " + str(request.form['name_input']))
	return render_template("index2.html")





