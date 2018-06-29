from app import app
from flask import jsonify, request
from app.soapclientbuilder import SoapClientBuilder

@app.route('/fingerprintapiproxy/api/v1.0/match', methods=['POST'])
def match():
    soapclient = SoapClientBuilder()
    
    data = request.get_json()
    
    msisdn = data['Msisdn']
    probe_minutiae = data['ProbeMinutiae']
    candidate_template = data['CandidateTemplate']

    soap_request_body = soapclient.build_request_body(msisdn=msisdn, probe_minutiae=probe_minutiae, candidate_template=candidate_template)
    soap_response = soapclient.send_request(soap_request_body)
    parsed_soap_response = soapclient.parse_response(soap_response)

    return jsonify(parsed_soap_response),201
