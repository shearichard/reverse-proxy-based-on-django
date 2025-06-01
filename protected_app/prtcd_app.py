from flask import Flask, jsonify, render_template

app = Flask(__name__)

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
    return jsonify({}), 200  # HTTP 200 OK

# Route for /api/v1/country/<int:pk>/
@app.route('/api/v1/country/<int:pk>/', methods=['GET'])
def country_detail(pk):
    return jsonify({}), 200  # HTTP 200 OK

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
    with app.app_context():
        print("Available routes:")
        for rule in app.url_map.iter_rules():
            print(f"{rule.endpoint}: {rule.rule} [{', '.join(rule.methods)}]")
    app.run(debug=True)

