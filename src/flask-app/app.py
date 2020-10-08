from flask import Flask, render_template, request
import smtplib, os

app = Flask(__name__)

subscribers = []

@app.route('/')
def index():
   
    return render_template('index.html')

@app.route('/about')
def about():
    
    names =["John", "Merry", "Robert", "Sally"]
    return render_template('about.html', names=names)

@app.route('/subscribe')
def subscribe():
   
    return render_template('subscribe.html')

@app.route('/form', methods=["POST"])
def form():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    #message = "You have been subscribed to my email newsletter"
    #server = smtplib.SMTP("smtp.gmail.com", 587)
    #server.starttls()
    #server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASS"))
    #server.sendmail(os.getenv("EMAIL_ADDRESS"),email,message)

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields required"
        return render_template("fail.html", error_statement=error_statement,
                          first_name=first_name,
                          last_name=last_name,
                          email=email)
    subscribers.append(f"{first_name} {last_name} {email}")
    return render_template('form.html', subscribers=subscribers)