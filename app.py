from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "Krish123"  # Used for flash messages

# Homepage route
@app.route("/")
def home():
    return render_template("portfolio.html")

# Contact page (GET + POST)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Compose the email
        email_message = EmailMessage()
        email_message['Subject'] = f'New Contact Form Submission from {name}'
        email_message['From'] = "your_email@gmail.com"  # Replace with your Gmail
        email_message['To'] = "your_email@gmail.com"    # Receiver (same or another)
        email_message.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

        try:
            # Sending email via Gmail SMTP
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("krishgupta6502@gmail.com", "aznd zend uexg zdtn")  # Use your Gmail App Password
                smtp.send_message(email_message)

            flash("✅ Message sent successfully!", "success")
        except Exception as e:
            flash(f"❌ Error sending message: {e}", "error")

        return redirect("/contact")  # Redirect after sending
    return render_template("contact.html")  # Render contact form page

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Project page
@app.route("/project")
def project():
    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug=True)
