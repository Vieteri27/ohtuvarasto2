from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        project_contents = toml.loads(content)

        name = project_contents["tool"]["poetry"]["name"]
        desc = project_contents["tool"]["poetry"]["description"]
        dependencies = project_contents["tool"]["poetry"]["dependencies"]
        dev_dependencies = project_contents["tool"]["poetry"]["group"]["dev"]["dependencies"]
        license = project_contents["tool"]["poetry"]["license"]
        authors = project_contents["tool"]["poetry"]["authors"]

        # deserialisoi TOML-formaatissa oleva merkkijono
        # ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_dependencies, license, authors) # pylint: disable=too-many-function-args
