'''
Fabric method for serializator's type
'''


class Fabric:
    def create_sreializer(serializer: str) -> object:
        if serializer == "json":
            return "JSON"
        elif serializer == "yaml":
            return "YAML"
        return "TOML"
