from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os


class Api():

    def __init__(self,
                 api_url=None,
                 api_token_url=None,
                 client_id=None,
                 client_secret=None,
                 grant_type='client_credentials'):
        self.api_token_url = api_token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    def get_token(self):
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        return {
            'client_credentials': self.get_backend_token
        }[self.grant_type]()

    def get_backend_token(self):
        if self.grant_type == 'client_credentials' and (
                self.client_id is None or self.client_secret is None):
            raise Exception('need custom exception')
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url=self.api_token_url,
            client_id=self.client_id,
            client_secret=self.client_secret)
        return token
