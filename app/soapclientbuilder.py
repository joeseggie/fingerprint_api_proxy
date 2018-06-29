"""Soap client builder"""
from app import app
import requests
from requests.auth import HTTPBasicAuth

class SoapClientBuilder():
    """Class the builds the soap client"""

    def __init__(self):
        """Constructor"""
        self.fingerprint_api_wsdl = app.config['FINGERPRINT_WSDL']
        self.api_username = app.config['USERNAME']
        self.api_password = app.config['PASSWORD']
    
    def build_request_body(self, msisdn, probe_minutiae, candidate_template):
        """Builds the soap request the is going to be sent

        Arguments:
            msisdn {str} -- MSISDN being registered
            probe_minutiae {str} -- base64 encoded fingerprint from ID
            candidate_template {str} -- base64 encoded template of scanned fingerprint

        Returns:
            text/xml soap request formatted string
        """
        soap_body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:end="http://endpoint.tlc.com/"><soapenv:Header/><soapenv:Body><end:verifier><!--Optional:--><parameter><msisdn>{0}</msisdn><probeMinutiae>{1}</probeMinutiae><candidateTemplate>{2}</candidateTemplate></parameter></end:verifier></soapenv:Body></soapenv:Envelope>'.format(msisdn, probe_minutiae, candidate_template)

        return soap_body
    
    def send_request(self, request_body):
        """Sends request to process the soap request
        
        Argument(s):
            request_body {str} -- text/xml formatted string

        Returns:
            Response from SOAP API as string
        """
        url = self.fingerprint_api_wsdl
        headers = {'Context-Type': 'text/xml'}
        username = self.api_username
        password = self.api_password
        auth = HTTPBasicAuth(username=username, password=password)

        api_response = requests.post(url, data=request_body, headers=headers, auth=auth)

        return api_response.content.decode('utf-8')
