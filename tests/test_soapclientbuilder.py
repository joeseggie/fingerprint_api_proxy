from app.soapclientbuilder import SoapClientBuilder

class TestSoapClientBuilder:
    
    def test_build_request_body(self):
        # Given
        msisdn = '414000114'
        probe_minutiae = 'RQ8CcW5FTALW8kXWAtxwQ8oDfnxFtwOScEUaA7HwQfcDxZGDQQP9hYUABDVxQc4EYxSD3wSbgUWZBOLiRL4FM2xFkwU4Y4RJBVx7QaYFqK1C/wWtr0JnBbKvhGMGEt2D6QY2wkeuBodQRr8Gv1NBhwcBvEZuB8xWg3kH5tKHPggOW0XGCEZXR48Ib3RHZwi7fEbJCQJ0RG0JEt2ERAk1WYJxCTpWRqYJSXxHZwlUiEXLCYFvQj4Jm1pEoAnOZoV6Cd12Q3QJ9mJFPQo9fkKfClJmQ98KUnCG/AphBkY2Co+Cgv8Kt3ODzwq3fYSLCw6Aht4LLIpD1AtQgA=='
        candidate_template = 'Rk1SACAyMAAAAACKAAABAAFoAMUAxQEAAAAXEoChACFKAIBwAFdXAICHAFc5AEAoAHfbAIBPAHbhAIBsAHzyAECsAHslAIDBAIMkAEAmAI5bAIB3AKf3AEDIAKoUAEDKAK+JAIA8ALXqAICPAM76AIA2ANdpAEBuAOL0AEB2APN0AEBxAPf2AAAArb7wHThvAAAAAAAAAAAAAAAAAAAAAAAAAAAAUMESAAAAAAAAAAAAAAAAAAAAAAAAAAAAUMESAAAAAP////8BAAAAAAAAAAEAAAECAAAAvva0peR4rb4EAAAA4q7VF3EgAADkXeK28B04b5gwdreYd62+AxVocAMAAADAea2+AQAAAPAdOG+YMHa3AQAAABNwIsk46Se1EAAAAAAAAADszyu1AAAgARMAAAAwea2+cSAAAL72tKVXnQa1cSAAAOR4rb6Aea2+iKwrtZgwdrcAAAAA5F3ithNwIslU5ie1wYL97AAEAACI9rSlAAQAAGDMjLeIrCu1OKAqtUC7K7XkXeK2UHitvtD1J7VIeK2+POwntdD1J7Uk6ye1OOsntQMAAAAAAAAAPPAstRCALLUAAFUAAwAAABNwIskAAEMAAwAAAAMAAAAoj3W3BHqtvuRd4rZgjsISR/wHtUMAAAAAAAAAtAQAAJg3oLcAAAAAmDB2t0MAAAAAAAAAtAQAABNwIslgjsISxQEotWR5rb6IrCu1cwAAAFR5rb44oCq1+P0ntYh6rb6ZBwi1mDB2twYAAADweK2+5F3itih5rb7k/Se1PP4ntWD2J7UE/ie1wP0ntQYAAACBk9y2YHmtvgEAAAAuea2+AgAAAAEAAAAAAEMAAABVAAEAAAAAAEMAEwAAAJg3oLe1BAAAkDegtxNwIsmYN6C3ZHmtvsg2drdkea2+yDZ2t5g3oLepHxa1iKwrtTigKrUEAAAAiHqtvtD1J7U87Ce1FOwntdD1J7Uk6ye1OOsntegudreYMHa3QwAAAAAAAAAAN6C3OKAqtQAAVQAAAEMAAABVALB5rb4Aeq2+QHaftxNwIsnINna3AADA////30GYMHa3BgAAAECOwhJgjsIS8P8xb5gwdrcAAAAAiHqtvj1JBbWEjOC2YAAAAAAAAADFsh9yAHqtvgR6rb5Ieq2+SHqtvkj9pm/Ye62+AwAAAAiYom9AjsISYI4='
        builder = SoapClientBuilder()

        # When
        soap_request_body = builder.build_request_body(msisdn, probe_minutiae, candidate_template)

        # Then
        print(soap_request_body)
        assert isinstance(soap_request_body, str)
    
    def test_send_request(self):
        # Given
        builder = SoapClientBuilder()
        soap_body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:end="http://endpoint.tlc.com/"><soapenv:Header/><soapenv:Body><end:verifier><!--Optional:--><parameter><msisdn>414000114</msisdn><probeMinutiae>RQ8CcW5FTALW8kXWAtxwQ8oDfnxFtwOScEUaA7HwQfcDxZGDQQP9hYUABDVxQc4EYxSD3wSbgUWZBOLiRL4FM2xFkwU4Y4RJBVx7QaYFqK1C/wWtr0JnBbKvhGMGEt2D6QY2wkeuBodQRr8Gv1NBhwcBvEZuB8xWg3kH5tKHPggOW0XGCEZXR48Ib3RHZwi7fEbJCQJ0RG0JEt2ERAk1WYJxCTpWRqYJSXxHZwlUiEXLCYFvQj4Jm1pEoAnOZoV6Cd12Q3QJ9mJFPQo9fkKfClJmQ98KUnCG/AphBkY2Co+Cgv8Kt3ODzwq3fYSLCw6Aht4LLIpD1AtQgA==</probeMinutiae><candidateTemplate>Rk1SACAyMAAAAACKAAABAAFoAMUAxQEAAAAXEoChACFKAIBwAFdXAICHAFc5AEAoAHfbAIBPAHbhAIBsAHzyAECsAHslAIDBAIMkAEAmAI5bAIB3AKf3AEDIAKoUAEDKAK+JAIA8ALXqAICPAM76AIA2ANdpAEBuAOL0AEB2APN0AEBxAPf2AAAArb7wHThvAAAAAAAAAAAAAAAAAAAAAAAAAAAAUMESAAAAAAAAAAAAAAAAAAAAAAAAAAAAUMESAAAAAP////8BAAAAAAAAAAEAAAECAAAAvva0peR4rb4EAAAA4q7VF3EgAADkXeK28B04b5gwdreYd62+AxVocAMAAADAea2+AQAAAPAdOG+YMHa3AQAAABNwIsk46Se1EAAAAAAAAADszyu1AAAgARMAAAAwea2+cSAAAL72tKVXnQa1cSAAAOR4rb6Aea2+iKwrtZgwdrcAAAAA5F3ithNwIslU5ie1wYL97AAEAACI9rSlAAQAAGDMjLeIrCu1OKAqtUC7K7XkXeK2UHitvtD1J7VIeK2+POwntdD1J7Uk6ye1OOsntQMAAAAAAAAAPPAstRCALLUAAFUAAwAAABNwIskAAEMAAwAAAAMAAAAoj3W3BHqtvuRd4rZgjsISR/wHtUMAAAAAAAAAtAQAAJg3oLcAAAAAmDB2t0MAAAAAAAAAtAQAABNwIslgjsISxQEotWR5rb6IrCu1cwAAAFR5rb44oCq1+P0ntYh6rb6ZBwi1mDB2twYAAADweK2+5F3itih5rb7k/Se1PP4ntWD2J7UE/ie1wP0ntQYAAACBk9y2YHmtvgEAAAAuea2+AgAAAAEAAAAAAEMAAABVAAEAAAAAAEMAEwAAAJg3oLe1BAAAkDegtxNwIsmYN6C3ZHmtvsg2drdkea2+yDZ2t5g3oLepHxa1iKwrtTigKrUEAAAAiHqtvtD1J7U87Ce1FOwntdD1J7Uk6ye1OOsntegudreYMHa3QwAAAAAAAAAAN6C3OKAqtQAAVQAAAEMAAABVALB5rb4Aeq2+QHaftxNwIsnINna3AADA////30GYMHa3BgAAAECOwhJgjsIS8P8xb5gwdrcAAAAAiHqtvj1JBbWEjOC2YAAAAAAAAADFsh9yAHqtvgR6rb5Ieq2+SHqtvkj9pm/Ye62+AwAAAAiYom9AjsISYI4=</candidateTemplate></parameter></end:verifier></soapenv:Body></soapenv:Envelope>'

        # When
        api_response = builder.send_request(soap_body)

        # Then
        print(api_response)
        assert isinstance(api_response, str)
    
    def test_parse_response(self):
        # Given
        builder = SoapClientBuilder()
        soap_response = '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:verifierResponse xmlns:ns2="http://endpoint.tlc.com/"><return><referenceid>120180629000025</referenceid><msisdn>414000114</msisdn><threshold>40.0</threshold><score>99.13779959465239</score><matchingResult>Matched</matchingResult><kycUpdateStatus>-1006|KYC IS ALREADY APPROVED. NO ACTION TAKEN.</kycUpdateStatus><message>The matching score is 99.13779959465239. The score is greater than threshold</message></return></ns2:verifierResponse></soap:Body></soap:Envelope>'

        # When
        parsed_soap_response = builder.parse_response(soap_response)

        # Then
        print(parsed_soap_response)
        assert isinstance(parsed_soap_response, str)
