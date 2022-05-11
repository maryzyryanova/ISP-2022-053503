import unittest
import test_data
# from fabric import Fabric

class Test(unittest.TestCase):

    def __init__(self, fabric) -> None:
        self.fabric = fabric

    def test_int(self):
        input = test_data.int_glob
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_float(self):
        input = test_data.float_glob
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_none(self):
        input = test_data.none_glob
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_bool(self):
        input = test_data.boolean_glob
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_string(self):
        input = test_data.str_glob
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_list(self):
        input = test_data.list_1
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_set(self):
        input = test_data.set_1
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_tuple(self):
        input = test_data.tuple_1
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_dict(self):
        input = test_data.dict_1
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_lambda(self):
        input = test_data.simple_lambda
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_simple_function(self):
        input = test_data.simple_func
        output = self.fabric.loads(self.fabric.dumps(input))
        self.assertEqual(output, input)

    def test_complex_function(self):
        input = test_data.cmplx_func
        

