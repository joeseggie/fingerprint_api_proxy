from app import app
from flask import jsonify

@app.route('/')
def index():
    environment = app.config['ENV']
    fingerprint_wsdl = app.config['FINGERPRINT_WSDL']
    return jsonify({'Environment': environment, 'Fingerprint WSDL': fingerprint_wsdl})
