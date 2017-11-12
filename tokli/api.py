from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from os.path import expanduser
import os
import json


class Api():

    tokens_file = "%s/.config/tokli/tokens.json" % expanduser("~")

    def __init__(self,
                 name='default',
                 api_url=None,
                 api_token_url=None,
                 client_id=None,
                 client_secret=None,
                 grant_type='client_credentials',
                 force_refresh=False):
        self.api_token_url = api_token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.name = name
        self.force_refresh = force_refresh

    def get_cached_token(self, name):
        if os.path.isfile(self.tokens_file):
            with open(self.tokens_file, 'r') as stream:
                tokens = json.load(stream)
                if name in tokens:
                    return tokens[name]
        else:
            with open(self.tokens_file, 'w') as outfile:
                json.dump({name: {}}, outfile)
        return False

    def get_token(self):
        token_cached = self.get_cached_token(self.name)
        if token_cached and not self.force_refresh:
            return token_cached
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
        if 'access_token' in token:
            with open(self.tokens_file, 'r+') as stream:
                data = json.load(stream)
                data[self.name] = token
                stream.seek(0)
                json.dump(data, stream)
                stream.truncate()
        return token
