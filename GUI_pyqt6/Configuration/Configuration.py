import json


class Configuration:
    def __init__(self, database_path):
        self.database_path = database_path

    def get_json(self):
        return json.dumps(self.__dict__)


def save_configuration(configuration, file_path):
    json_data = configuration.get_json()
    file = open(file_path, "w")
    file.write(json_data)
    file.close()


def load_configuration(file_path):
    file = open(file_path, "r")
    jsons = file.read()
    file.close()

    configuration_dict = json.loads(jsons)
    configuration = Configuration(configuration_dict["database_path"])
    return configuration
