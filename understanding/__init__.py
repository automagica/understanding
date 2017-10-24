import requests
import os


class Understanding():
    def __init__(self, service, api_key=None, api_version=None):
        """
        Initializes the Understanding object.

        Keyword arguments:
        service -- string referring to the service. 'wit' currently only supported
        api_key -- 3rd party service API key
        """
        self.service = service

        if not api_key:
            self.api_key = os.environ.get('UNDERSTANDING_API_KEY')
        else:
            self.api_key = api_key
        if not self.api_key:
            raise Exception(
                'Please set UNDERSTANDING_API_KEY environment variable or specify api_key attribute.')

        if not api_version and service == 'wit':
            self.api_version = '23102017'
        else:
            self.api_version = api_version

    def parse(self, message):
        """
        Parses a message to entities and intents.

        Keyword arguments:
        message -- string containing the to be parsed message
        """
        if self.service == 'wit':

            headers = {'Authorization': 'Bearer ' + self.api_key}
            r = requests.get('https://api.wit.ai/message?v=' +
                             self.api_version + '&q=' + message, headers=headers)
            data = r.json()

            if not data.get('error'):
                return data
            else:
                raise Exception('External service returned an error.')

        else:
            raise NotImplementedError

    def get_entities(self):
        """
        Returns list of entities
        """
        if self.service == 'wit':

            headers = {'Authorization': 'Bearer ' + self.api_key}
            r = requests.get('https://api.wit.ai/entities?v=' +
                             self.api_version, headers=headers)
            data = r.json()

            if data:
                return data
            else:
                raise Exception('External service returned an error.')

        else:
            raise NotImplementedError

    def get_intents(self):
        """
        Returns information on entitity
        """
        if self.service == 'wit':

            headers = {'Authorization': 'Bearer ' + self.api_key}
            r = requests.get('https://api.wit.ai/entities/intent' + '?v=' +
                             self.api_version, headers=headers)
            data = r.json()

            if data:
                return [value['value'] for value in data['values']]
            else:
                raise Exception('External service returned an error.')

        else:
            raise NotImplementedError
