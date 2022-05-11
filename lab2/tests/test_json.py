from fabric import Fabric
from test_father import Test

class TestJson(Test):
    fabric = Fabric.create_serializer("json")