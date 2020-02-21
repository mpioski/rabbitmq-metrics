import requests
from source.config.config import Config


class Api:
    def __init__(self):
        conf = Config()
        conn = conf.rabbit_connection()
        self.user = conn["user"]
        self.password = conn["password"]
        self.host = conn["host"]
        self.port = conn["port"]
        self.api = "{0}:{1}/api".format(self.host, self.port)

    def __enter__(self):
        self.session = requests.Session()
        self.session.auth = (self.user, self.password)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
