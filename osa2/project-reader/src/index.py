from project_reader import ProjectReader


def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/test-project/pyproject.toml" # pylint: disable=line-too-long
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
