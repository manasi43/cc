from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key for session management

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/cart')
# def cart():
#     return render_template('cart.html')

# @app.route('/checkout', methods=['GET', 'POST'])
# def checkout():
#     if request.method == 'POST':
#         name = request.form['name']
#         contact = request.form['contact']
#         pincode = request.form['pincode']
#         state = request.form['state']
#         address = request.form['address']
#         payment_method = request.form['payment']
        
#         # Here, you can handle the order logic (e.g., save to a database)
#         # For now, we'll just flash a success message
#         flash(f'Order placed successfully by {name}!', 'success')
#         return redirect(url_for('checkout'))

#     return render_template('checkout.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phoneno = request.form['phoneno']
        email = request.form['email']
        msg = request.form['msg']
        
        # Handle the contact form submission (e.g., send an email, save to a database)
        # For now, we'll just flash a success message
        flash(f'Message sent successfully by {fname}!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
