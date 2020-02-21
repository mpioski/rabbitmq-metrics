import yaml


class Config:

    __monostate = None
    conf = None

    def __init__(self):
        if not Config.__monostate:
            Config.__monostate = self.__dict__
            self.conf = yaml.load(
                open("source/config/files/config.yml"), Loader=yaml.BaseLoader
            )
        else:
            self.__dict__ = Config.__monostate

    def fields(self, search):
        fields = search + "_fields"
        return self.conf[fields]

    def rabbit_connection(self):
        return self.conf["rabbit"]
