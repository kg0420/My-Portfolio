from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "Krish123"  # Used for flash messages

# Homepage route
@app.route("/")
def home():
    return render_template("portfolio.html")

# Contact form route
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Compose the email
    email_message = EmailMessage()
    email_message['Subject'] = f'New Contact Form Submission from {name}'
    email_message['From'] = "your_email@gmail.com"  # Replace with your email
    email_message['To'] = "your_email@gmail.com"    # Same or another email
    email_message.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

    try:
        # Sending email via Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("krishgupta6502@gmail.com", "aznd zend uexg zdtn")  # Use app password
            smtp.send_message(email_message)

        flash("Message sent successfully!", "success")
    except Exception as e:
        flash(f"Error sending message: {e}", "error")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
