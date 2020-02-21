from .api import Api


class RabbitMetrics(Api):
    def get_info(self, name, json=True):

        url = "{0}/{1}".format(self.api, name)
        response = self.session.get(url=url)

        if json:
            return response.text

        return response.json()
