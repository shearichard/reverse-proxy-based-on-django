import sqlite3
from flask import Flask, request, jsonify, render_template, g
import logging
import uuid

DISPLAY_ALL_ROUTES_ON_CONSOLE = False

app = Flask(__name__)

'''
# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('../db.sqlite3')  # Replace with your database file
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

@app.before_request
def log_request_info():
    # Generate a unique request ID
    request_id = str(uuid.uuid4())
    g.request_id = request_id  # Store it in Flask's global context
    logging.info(f'Request ID: {request_id} - Request Headers: {request.headers}')
    logging.info(f'Request ID: {request_id} - Request Body: {request.get_data(as_text=True)}')
    logging.info(f'Request ID: {request_id} - Request Method: {request.method}')
    logging.info(f'Request ID: {request_id} - Request Path: {request.path}')

@app.after_request
def log_response_info(response):
    request_id = g.request_id  # Retrieve the request ID
    logging.info(f'Request ID: {request_id} - Response Status: {response.status}')
    logging.info(f'Request ID: {request_id} - Response Headers: {response.headers}')
    return response


'''
@app.route('/example', methods=['GET', 'POST'])
def example():
    return jsonify(message="This is an example response.")

# Route for the root URL
@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>Home Page</h1>
    <div>
        <a href="/country">Go to Country Page</a>
    </div>
    ''', 200  # HTTP 200 OK

# Route for /api/v1/city/
@app.route('/api/v1/city/', methods=['GET'])
def city_list():
    return jsonify({}), 200  # HTTP 200 OK

# Route for /api/v1/city/<int:pk>/delete/
@app.route('/api/v1/city/<int:pk>/delete/', methods=['DELETE'])
def city_delete(pk):
    return jsonify({}), 204  # HTTP 204 No Content

# Route for /api/v1/country/
@app.route('/api/v1/country/', methods=['GET'])
def country_list():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assidu_country")
    countries = cursor.fetchall()
    conn.close()

    # Convert the rows to a list of dictionaries
    country_list = [dict(row) for row in countries]
    return jsonify(country_list), 200  # HTTP 200 OK

# Route for /api/v1/country/<int:pk>/
@app.route('/api/v1/country/<int:pk>/', methods=['GET'])
def country_detail(pk):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assidu_country WHERE id = ?", (pk,))
    country = cursor.fetchone()
    conn.close()

    if country is None:
        return jsonify({"error": "Country not found"}), 404  # HTTP 404 Not Found

    return jsonify(dict(country)), 200  # HTTP 200 OK

# Route for /api/v1/country/<int:pk>/delete/
@app.route('/api/v1/country/<int:pk>/delete/', methods=['DELETE'])
def country_delete(pk):
    return jsonify({}), 204  # HTTP 204 No Content

# Route for /api/v1/country/<int:pk>/edit/
@app.route('/api/v1/country/<int:pk>/edit/', methods=['PUT'])
def country_update(pk):
    return jsonify({}), 200  # HTTP 200 OK

# Route for /api/v1/country/new/
@app.route('/api/v1/country/new/', methods=['POST'])
def country_create():
    return jsonify({}), 201  # HTTP 201 Created

# New route for /country (HTML page)
@app.route('/country', methods=['GET'])
def country_html():
    return render_template('country.html')
    #return '''country list''', 200

# New route for /country/<id> (HTML page)
@app.route('/country/<int:id>', methods=['GET'])
def country_detail_html(id):
    return render_template('country_detail.html', country_id=id)

'''
if __name__ == '__main__':
    app.run(debug=True)
'''
if __name__ == '__main__':
    if DISPLAY_ALL_ROUTES_ON_CONSOLE:
        with app.app_context():
            print("Available routes:")
            for rule in app.url_map.iter_rules():
                print(f"{rule.endpoint}: {rule.rule} [{', '.join(rule.methods)}]")

    app.run(debug=True)

