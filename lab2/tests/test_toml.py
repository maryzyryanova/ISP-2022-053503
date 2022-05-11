from fabric import Fabric
from test_father import Test

class TestToml(Test):
    fabric = Fabric.create_serializer("toml")