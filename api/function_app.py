import azure.functions as func  # type: ignore
import logging
import requests
from datetime import datetime
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)





class SDIXAdapterAgent:
    def __init__(self) -> None:
        self.baseurl = 'https://sdi-x-adapter.sdika.we.network/'

        self.offer = {
            "credentialType": "VerifiedIban",
            "contextUri": "https://sdika.signicat.com/schema/verified-iban",
            "claims": {},
            "config": {
                "issuer": "bob",
                "issuerUrl": "https://sdi-x-adapter.sdika.we.network",
                "walletUrl": "https://wallet.sdika.we.network/initiate_issuance",
                "callback": "https://httpdump.io/0nakw"
            }
        }

    def requestVerifiableCredential(self) -> str:
        url = self.baseurl + 'verifier/requestVerifiableCredential'
        data = json.dumps({
            'credentialType': 'VerifiedIban',
            'presentationDefinition': None,
            'successRedirectUrl': 'https://protected.resource',
            'config': {
            'callback': 'https://httpdump.io/0nakw',
            'walletUrl': 'https://wallet.sdika.we.network/oauth/auth'
            }
        })
        response = requests.post(url, json=data)
        return response.text

    def getVerifiableCredential(self, id) -> str:
        url = self.baseurl + 'verifier/getVerifiableCredential'
        data = json.dumps({
          'transactionId': id,
          'config': {
            'callback': 'https://httpdump.io/0nakw',
            'walletUrl': 'https://wallet.sdika.we.network/oauth/auth'
          }
        })
        response = requests.post(url, json=data)
        return response.text



@app.route(route="requestVerifiableCredential")
def requestVerifiableCredential(req: func.HttpRequest) -> func.HttpResponse:
    ret =  SDIXAdapterAgent().requestVerifiableCredential()
    return func.HttpResponse(ret, status_code=200)


@app.route(route="getVerifiableCredential")
def getVerifiableCredential(req: func.HttpRequest) -> func.HttpResponse:
    id_field = 'id'
    id = req.params.get(id_field),
    ret = SDIXAdapterAgent().getVerifiableCredential(id)
    return func.HttpResponse(ret, status_code=200)