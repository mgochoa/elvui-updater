import os
import shutil
import tempfile
import requests
from zipfile import ZipFile

API_URL = "https://api.tukui.org/v1/addon/elvui"


def get_metadata(url):
    response = requests.get(url)
    return response.json()


class UpdaterService:

    def __init__(self):
        self.elvui_metadata: dict or None = None
        self.temp_zip: tempfile.NamedTemporaryFile or None = None
        self.load_elvui_metadata()

    def load_elvui_metadata(self):
        self.elvui_metadata = get_metadata(API_URL)
        print("Elvui metadata", self.elvui_metadata)

    def get_zip_file(self) -> tempfile.NamedTemporaryFile:
        response = requests.get(self.elvui_metadata["url"])
        with tempfile.NamedTemporaryFile(mode="wb", delete=False) as tf:
            tf.write(response.content)
            return tf

    def unzip_and_copy_to_folder(self, destination):
        if self.temp_zip:
            with tempfile.TemporaryDirectory() as temp_dir:
                with ZipFile(self.temp_zip.name) as z_object:
                    z_object.extractall(path=temp_dir)
                    if temp_dir and len(os.listdir(temp_dir)) > 1:
                        shutil.copytree(temp_dir, destination, dirs_exist_ok=True)
                        print("Copied elvui correctly to addons folder")

    def update_elvui(self, wow_addon_folder):
        self.temp_zip = self.get_zip_file()
        print(f"Download in to temp zip:{self.temp_zip}")
        self.unzip_and_copy_to_folder(wow_addon_folder)
