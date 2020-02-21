import os
import yaml


class Config:
    """
    This class is responsible to get all configurations from config.yml file
    """

    __monostate = None
    __path = os.path.dirname(__file__)
    __file = None
    conf = None

    def __init__(self):
        if not Config.__monostate:
            Config.__monostate = self.__dict__
            with open(os.path.join(self.__path, "files/config.yml")) as _file:
                self.__file = _file.read()
            self.conf = yaml.load(self.__file, Loader=yaml.BaseLoader)
        else:
            self.__dict__ = Config.__monostate

    def fields(self, search):
        fields = search + "_fields"
        return self.conf[fields]

    def rabbit_connection(self):
        return self.conf["rabbit"]
