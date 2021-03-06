from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

queries = []

@app.route('/')
def index():
    # title = "Hellometer"
    return render_template("index.html")

@app.route('/data')
def data():
    title = "Data Hellometer"
    customers = ["1", "2", "3", "4", "5"]
    return render_template("data.html", customers=customers, title=title)

@app.route('/contact')
def contact():
    title = "Contact us"
    return render_template("contact.html", title=title)

@app.route('/form', methods=["POST"])
def form():
    title = "Thank You!"
    email_address = request.form.get("email_address")
    details = request.form.get("details")

    message = "You message has been submitted"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("angelaxie@gmail.com", "PASSWORD")
    server.sendmail("angelaxie@gmail.com", email_address, message)

    if not email_address or not details:
        error_statement = "All Form Fields Required"
        return render_template("contact.html",  
            error_statement = error_statement,
            email_address = email_address,
            details = details,
            message = message)

    queries.append(f"{email_address} | {details}")
    return render_template("form.html", queries = queries, title=title)