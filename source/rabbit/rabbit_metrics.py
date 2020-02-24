import json

from .api import Api


class RabbitMetrics(Api):

    def get_info(self, name, json_type=True):

        url = "{0}/{1}".format(self.api, name)
        response = self.session.get(url=url)

        if json_type:
            return response.text

        return response.json()

    def post_info(self, name, data, json_type=True):

        url = "{0}/{1}".format(self.api, name)
        response = self.session.post(url=url, data=json.dumps(data))
        if json_type:
            return response.text

        return response.json()

    def put_info(self, name, data, json_type=True):

        url = "{0}/{1}".format(self.api, name)
        response = self.session.put(url=url, data=json.dumps(data))
        if json_type:
            return response.text

        return response.json()

    def delete_info(self, name, data):
        url = "{0}/{1}".format(self.api, name)
        response = self.session.delete(url=url, data=json.dumps(data))
        return response.text
