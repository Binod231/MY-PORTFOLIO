import os
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Database configuration
DB_PATH = os.path.join(os.path.dirname(__file__), 'portfolio-messages.db')

# Initialize database table
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

init_db()  # Call this when app starts

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not all([name, email, message]):
            flash('All fields are required!', 'warning')
        elif '@' not in email or '.' not in email:
            flash('Please enter a valid email address', 'danger')
        else:
            try:
                with sqlite3.connect(DB_PATH) as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO user (name, email, message) VALUES (?, ?, ?)",
                        (name, email, message)
                    )
                    flash('Message sent successfully!', 'success')
                    return redirect(url_for('success'))
            except sqlite3.IntegrityError:
                flash('Email already exists!', 'danger')
            except Exception as e:
                app.logger.error(f"Database error: {str(e)}")
                flash('Error sending message', 'danger')

        return redirect(url_for('home'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run()