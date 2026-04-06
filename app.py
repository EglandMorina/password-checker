from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("checker.html")


@app.route("/password-checker", methods=["GET", "POST"])
def checker():
    result = None
    missing = []

    if request.method == "POST":
        password = request.form["password"]

        has_number = False
        has_uppercase = False
        has_lowercase = False

        for char in password:
            if char.isdigit():
                has_number = True
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True

        if len(password) < 8:
            missing.append("Add at least 8 characters")

        if not has_number:
            missing.append("Add a number")

        if not has_uppercase:
            missing.append("Add uppercase letter")

        if not has_lowercase:
            missing.append("Add lowercase letter")

        if len(password) < 8:
            result = "Weak"
        elif has_number and has_uppercase and has_lowercase:
            result = "Strong"
        else:
            result = "Medium"

    return render_template("checker.html", result=result, missing=missing)


if __name__ == "__main__":
    app.run(host="0.0.0.0",
port=int(os.environ.get("PORT", 10000)))