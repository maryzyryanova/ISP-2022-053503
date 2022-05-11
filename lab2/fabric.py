'''
Fabric method for serializator's type
'''

import serializers_classes.json_serializer as json
import serializers_classes.toml_serializer as toml
import serializers_classes.yaml_serializer as yaml


class Fabric:
    def create_serializer(serializer: str) -> object:
        if serializer == "json":
            return json.JSON()
        elif serializer == "yaml":
            return yaml.YAML()
        return toml.TOML()
