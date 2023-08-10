"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/products')
def products():
    """Render the the page to display list of products"""
    return  render_template('products.html', products=products)


products = [
        {
            'id': 0,
            'title': 'Cowrie Shield Earring',
            'image': 'earring1.jpeg',
            'description':'A Kenyan inspired handmade beaded earring. It can also be worn as a ring or bracelet.',
            'price': 2000
        },
        {
            'id': 1,
            'title': 'Double Beaded Rings',
            'image': 'earring4.jpeg',
            'description':'Handmade double hooped beaded earring.',
            'price': 1500
        },
        {
            'id': 2,
            'title': 'Drop Cowrie Earrings',
            'image': 'earring3.jpeg',
            'description':'Drop earrings made with cowrie shells and glass beads',
            'price': 2000
        },
        {
            'id': 3,
            'title': 'Gem stone Bracelets',
            'image': 'bracelet.jpeg',
            'description':'Bracelet set of 2, made from aventurine gem stones',
            'price': 2500
        },
        {
            'id': 4,
            'title': 'Embroidered Spideys',
            'image': 'embroid_tshirt.jpg',
            'description':'Machine embroidered sweatshirt, stitched is a scene from Spiderman and a viral meme',
            'price': 5000
        },
        {
            'id': 5,
            'title': 'Crocheted shroom',
            'image': 'bag.jpg',
            'description':'Crocheted mushroom shoulder bag',
            'price': 4500
        }
]

@app.route('/products/<product_id>')
def product_info(product_id):
    return render_template('product.html', product=products[int(product_id)])
    

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
