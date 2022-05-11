import unittest
from fabric import Fabric
from . import test_data


class Test(unittest.TestCase):
    json_fabric = Fabric.create_serializer("json")
    toml_fabric = Fabric.create_serializer("toml")
    yaml_fabric = Fabric.create_serializer("yaml")

    def test_int_json(self):
        input = test_data.int_glob
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_float_json(self):
        input = test_data.float_glob
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_none_json(self):
        input = test_data.none_glob
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    
    def test_bool_json(self):
        input = test_data.boolean_glob
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_string_json(self):
        input = test_data.str_glob
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_list_json(self):
        input = test_data.list_1
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_set_json(self):
        input = test_data.set_1
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_tuple_json(self):
        input = test_data.tuple_1
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_dict_json(self):
        input = test_data.dict_1
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_lambda_json(self):
        input = test_data.simple_lambda
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output(5), input(5))

    def test_butoma_func_json(self):
        input = test_data.butoma_func
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output(5), input(5))

    def test_simple_function_json(self):
        input = test_data.simple_func
        output = self.json_fabric.loads(self.json_fabric.dumps(input))
        self.assertEqual(output(4), input(4))

    def test_complex_function_json(self):
        input_1 = test_data.cmplx_func
        input_2 = test_data.simple_lambda
        output_1 = self.json_fabric.loads(self.json_fabric.dumps(input_1))
        output_2 = self.json_fabric.loads(self.json_fabric.dumps(input_2))
        self.assertEqual(output_1(4), input_1(4))
        self.assertEqual(output_2(2), input_2(4))

    def test_simple_class_json(self):
        old_obj = test_data.SimpleClass()
        new_obj = self.json_fabric.loads(self.json_fabric.dumps(old_obj))
        # self.assertEqual(old_obj.say_kuku(), new_obj)
        self.assertEqual(old_obj.word, new_obj.word)

    def test_complex_class_json(self):
        old_obj = test_data.ComplexClass()
        new_obj = self.json_fabric.loads(self.json_fabric.dumps(old_obj))
        # self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob())
        self.assertEqual(old_obj.const, new_obj.const)
        # self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))    
        self.test_simple_class_json()

    def test_int_yaml(self):
        input = test_data.int_glob
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_float_yaml(self):
        input = test_data.float_glob
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_none_yaml(self):
        input = test_data.none_glob
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_bool_yaml(self):
        input = test_data.boolean_glob
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_string_yaml(self):
        input = test_data.str_glob
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_list_yaml(self):
        input = test_data.list_1
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_set_yaml(self):
        input = test_data.set_1
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_tuple_yaml(self):
        input = test_data.tuple_1
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    def test_dict_yaml(self):
        input = test_data.dict_1
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output, input)

    # def test_lambda_yaml(self):
    #     input = test_data.simple_lambda
    #     output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
    #     self.assertEqual(output(5), input(5))

    def test_simple_function_yaml(self):
        input = test_data.simple_func
        output = self.yaml_fabric.loads(self.yaml_fabric.dumps(input))
        self.assertEqual(output(4), input(4))

    def test_complex_function_yaml(self):
        input_1 = test_data.cmplx_func
        # input_2 = test_data.simple_lambda
        output_1 = self.yaml_fabric.loads(self.yaml_fabric.dumps(input_1))
        # output_2 = self.yaml_fabric.loads(self.yaml_fabric.dumps(input_2))
        self.assertEqual(output_1(4), input_1(4))
        # self.assertEqual(output_2(2), input_2(4))

    def test_complex_class_yaml(self):
        old_obj = test_data.ComplexClass()
        new_obj = self.yaml_fabric.loads(self.yaml_fabric.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob())
        self.assertEqual(old_obj.const, new_obj.const)
            
    def test_simple_class_yaml(self):
        old_obj = test_data.SimpleClass()
        new_obj = self.yaml_fabric.loads(self.yaml_fabric.dumps(old_obj))
        # self.assertEqual(old_obj.say_kuku(), new_obj)
        self.assertEqual(old_obj.word, new_obj.word)

if __name__ == '__main__':
    unittest.main()