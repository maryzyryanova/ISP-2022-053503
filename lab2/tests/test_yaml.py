from fabric import Fabric
from test_father import Test

class TestYaml(Test):
    fabric = Fabric.create_serializer("yaml")