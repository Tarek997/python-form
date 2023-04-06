import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Insert the form data into the 'users' table
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create the 'users' table with the required columns
cursor.execute('''CREATE TABLE users
                (name TEXT, email TEXT, age INT)''')

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
