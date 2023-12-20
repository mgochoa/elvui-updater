import configparser
import os


class AppConfig:
    def __init__(self):
        self.config_file = None
        self.config = configparser.ConfigParser()

    def load_configuration(self):
        current_directory = os.getcwd()
        self.config_file = os.path.join(current_directory, "config.ini")

        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
            return True
        else:
            return False

    def get_setting(self, key) -> str or None:
        return self.config["Settings"].get(key)

    def set_setting(self, key, value):
        self.config["Settings"] = {key: value}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
