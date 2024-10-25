from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key for session management

# MySQL database connection details
db_config = {
    'host': 'database1.c7iegoogk12d.eu-north-1.rds.amazonaws.com',
    'database': 'art',
    'user': 'admin1',
    'password': 'manasipotdar'
}

# Function to create a database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phoneno = request.form['phoneno']
        email = request.form['email']
        msg = request.form['msg']
        
        # Create a connection to the database
        connection = create_connection()
        
        if connection:
            cursor = connection.cursor()
            try:
                # Insert the contact form data into the database
                cursor.execute("""
                    INSERT INTO contacts (first_name, last_name, phone_number, email, message) 
                    VALUES (%s, %s, %s, %s, %s)
                """, (fname, lname, phoneno, email, msg))
                connection.commit()
                
                flash(f'Message sent successfully by {fname}!', 'success')
            except Error as e:
                print(f"The error '{e}' occurred")
                flash('There was an error sending your message. Please try again.', 'error')
            finally:
                cursor.close()
                connection.close()  # Close the database connection

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
