from flask import Flask, jsonify

app = Flask(__name__)

# Route for /city/
@app.route('/city/', methods=['GET'])
def city_list():
    return jsonify({}), 200  # HTTP 200 OK

# Route for /city/<int:pk>/delete/
@app.route('/city/<int:pk>/delete/', methods=['DELETE'])
def city_delete(pk):
    return jsonify({}), 204  # HTTP 204 No Content

# Route for /country/
@app.route('/country/', methods=['GET'])
def country_list():
    return jsonify({}), 200  # HTTP 200 OK

# Route for /country/<int:pk>/
@app.route('/country/<int:pk>/', methods=['GET'])
def country_detail(pk):
    return jsonify({}), 200  # HTTP 200 OK

# Route for /country/<int:pk>/delete/
@app.route('/country/<int:pk>/delete/', methods=['DELETE'])
def country_delete(pk):
    return jsonify({}), 204  # HTTP 204 No Content

# Route for /country/<int:pk>/edit/
@app.route('/country/<int:pk>/edit/', methods=['PUT'])
def country_update(pk):
    return jsonify({}), 200  # HTTP 200 OK

# Route for /country/new/
@app.route('/country/new/', methods=['POST'])
def country_create():
    return jsonify({}), 201  # HTTP 201 Created

if __name__ == '__main__':
    app.run(debug=True)

