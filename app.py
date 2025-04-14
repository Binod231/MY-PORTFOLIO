import os
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validation
        if not all([name, email, message]):
            flash('All fields are required!', 'warning')
        elif '@' not in email or '.' not in email:
            flash('Please enter a valid email address', 'danger')
        else:
            try:
                conn = sqlite3.connect('portfolio-messages.db')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO user (name, email, message) VALUES (?, ?, ?)",
                    (name, email, message)
                )
                conn.commit()
                flash('Your message has been sent successfully!', 'success')
                return redirect(url_for('success'))  # Redirect to success page
            except sqlite3.IntegrityError:
                flash('This email has already been used. Please use a different email.', 'danger')
            except Exception as e:
                app.logger.error(f"Database error: {str(e)}")
                flash('An error occurred while sending your message. Please try again later.', 'danger')
            finally:
                if conn:
                    conn.close()

        return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/success',methods=['GET'])
def success():
    return render_template('success.html')

app.run(debug=True)