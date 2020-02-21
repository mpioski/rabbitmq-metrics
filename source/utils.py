from source.config.config import Config


class Format:
    def __init__(self):
        self.conf = Config()

    def filter_dict(self, dictionary, specific_keys, new_dict=None):
        """
        Creates a new dictionary from the keys of another dictionary.
        :param dictionary: original dictionary
        :param specific_keys: keys to be found
        :param new_dict:
        :return:
        """
        if new_dict is None:
            new_dict = {}
        for key, value in dictionary.items():
            if key in specific_keys:
                new_dict.update({key: value})
            if isinstance(value, dict):
                self.filter_dict(value, specific_keys, new_dict)

        return new_dict

    def format_queues(self, queues, fields=None):
        if fields is None:
            fields = self.conf.fields("queue")

        queues_info = []

        for queue in queues:
            info = self.filter_dict(queue, fields)
            queues_info.append(info)

        return queues_info
