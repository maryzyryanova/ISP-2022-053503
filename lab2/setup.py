from setuptools import setup

setup(
    name = "Lab-2",
    version = "1.0",
    author = "Mary Zyryanova",
    author_email = "z.y.r.y.a.n.o.v.a@mail.ru",
    packages = ["serialized_data", "serializers_classes", "unit_tests"],
    scripts = ["fabric.py", "main.py", "packing.py", "unpacking.py", ]
)