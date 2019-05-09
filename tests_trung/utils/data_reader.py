import configparser
from pathlib import Path


class DataReader:

    def __init__(self):
        data_folder = Path("tests_trung/")
        data_file = data_folder / "project.properties"
        config = configparser.RawConfigParser()
        config.read(data_file)
        self._url = config.get('ProjectData', 'environment.url')
        self._username = config.get('ProjectData', 'user.name')
        self._password = config.get('ProjectData', 'user.password')
        self._repository = config.get('ProjectData', 'repository.name')

    def get_url(self):
        return self._url

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_repository(self):
        return self._repository
