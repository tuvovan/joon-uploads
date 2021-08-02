import os  # For File Manipulations like get paths, rename
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from upload_azure import *

app = Flask(__name__) 

app.secret_key = "secret key"  # for encrypting the session
# It will allow below 16MB contents only, you can change it
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, "uploads")

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/agreement")
def agreement():
    return render_template("agreement.html")

@app.route("/upload")
def upload_form():
    return render_template("upload_index.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


@app.route("/", methods=["POST"])
def upload_file():
    if request.method == "POST":
        product_name = request.form.get("products")
        thickness = request.form.get("thickness")
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected for uploading")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = '%s_%s_%s'%(product_name, thickness, filename)
            upload(filename, file)
            flash("File successfully uploaded")
            return redirect("/")
        else:
            flash("Allowed file types are txt, pdf, png, jpg, jpeg, gif")
            return redirect(request.url)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

