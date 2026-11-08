class Project:
    def __init__(self, name, description, authors, license, reqPython, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = license
        self.reqPython = reqPython
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):

        authorsStr = ""
        for author in self.authors:
            authorsStr += f"\n- {author['name']}"

        depStr = ""
        if self.reqPython != "":
            depStr += f"\n- python"
        for dep in self.dependencies:
            name = dep.split(">=")[0]
            depStr += f"\n- {name}"

        devDepStr = ""
        for devDep in self.dev_dependencies:
            name = devDep.split(">=")[0]
            devDepStr += f"\n- {name}"

        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {authorsStr}\n"
            f"\nDependencies: {depStr}\n"
            f"\nDevelopment Dependencies: {devDepStr}\n"
        )
