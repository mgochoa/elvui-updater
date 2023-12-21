import configparser
import os
from pathlib import Path

from logger import logger


class AppConfig:
    def __init__(self):
        self.config_file = None
        self.config = configparser.ConfigParser()
        self.load_configuration()

    def load_configuration(self):
        parent_directory = Path(__file__).parent
        self.config_file = os.path.join(parent_directory, "config.ini")
        if not os.path.exists(self.config_file):
            self.config["Settings"] = {"WOW_ADDONS_FOLDER": ""}
            self.config.write(open(self.config_file, "w"))
        else:
            self.config.read(self.config_file)

    def get_setting(self, key) -> str or None:
        return self.config.get("Settings", key)

    def set_setting(self, key, value):
        self.config["Settings"] = {key: value}
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
