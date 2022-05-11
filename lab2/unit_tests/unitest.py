import unittest
from fabric import Fabric
from . import test_data


class SerializeTester(unittest.TestCase):
#---------JSON---------
    def test_json_int(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.int_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)
        
    def test_json_float(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.float_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_str(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.str_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_boolean(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.boolean_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_none(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.none_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_list(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.list_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_tuple(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.tuple_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_set(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.set_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_json_dict(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.dict_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj['Name'], new_obj['Name'])

    def test_json_lambda(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.simple_lambda
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_json_simple_func(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.simple_func
        self.s.dump(old_obj, 'testjson')
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_json_cmplx_func(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.cmplx_func
        old_obj_2 = test_data.simple_lambda
        new_obj = self.s.loads(self.s.dumps(old_obj))
        new_obj_2 = self.s.loads(self.s.dumps(old_obj_2))
        self.assertEqual(old_obj(4), new_obj(4))
        self.assertEqual(old_obj_2(4), new_obj_2(4))

    def test_json_simple_class_obj(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.SimpleClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_json_cmplx_class_obj(self):
        self.s = Fabric.create_serializer('json')
        old_obj = test_data.ComplexClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))

#---------YAML---------
    def test_yaml_int(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.int_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_float(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.float_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_str(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.str_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_boolean(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.boolean_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_none(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.none_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_list(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.list_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_tuple(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.tuple_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_set(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.set_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_lambda(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.simple_lambda
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_yaml_simple_func(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.simple_func
        self.s.dump(old_obj, 'testyaml')
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_yaml_cmplx_func(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.cmplx_func
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_yaml_simple_class_obj(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.SimpleClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_yaml_dict(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.dict_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_yaml_cmplx_class_obj(self):
        self.s = Fabric.create_serializer('yaml')
        old_obj = test_data.ComplexClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))
    
#---------TOML---------
    def test_toml_int(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.int_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_float(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.float_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_str(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.str_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_boolean(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.boolean_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_none(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.none_glob
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_list(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.list_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_tuple(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.tuple_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_set(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.set_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj, new_obj)

    def test_toml_dict(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.dict_1
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj['Name'], new_obj['Name'])

    def test_toml_lambda(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.simple_lambda
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(5), new_obj(5))

    def test_toml_simple_func(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.simple_func
        self.s.dump(old_obj, 'testtoml')
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_toml_cmplx_func(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.cmplx_func
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj(4), new_obj(4))

    def test_toml_simple_class_obj(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.SimpleClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.say_kuku(), new_obj.say_kuku(new_obj))
        self.assertEqual(old_obj.word, new_obj.word)

    def test_toml_cmplx_class_obj(self):
        self.s = Fabric.create_serializer('toml')
        old_obj = test_data.ComplexClass()
        new_obj = self.s.loads(self.s.dumps(old_obj))
        self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
        self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob(new_obj))
        self.assertEqual(old_obj.const, new_obj.const)
        self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))

if __name__ == '__main__':
    unittest.main()


# class Test(unittest.TestCase):
#     json_fabric = Fabric.create_serializer("json")
#     toml_fabric = Fabric.create_serializer("toml")
#     yaml_fabric = Fabric.create_serializer("yaml")

#     def test_int_json(self):
#         input = test_data.int_glob
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_float_json(self):
#         input = test_data.float_glob
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_none_json(self):
#         input = test_data.none_glob
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

    
#     def test_bool_json(self):
#         input = test_data.boolean_glob
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_string_json(self):
#         input = test_data.str_glob
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_list_json(self):
#         input = test_data.list_1
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_set_json(self):
#         input = test_data.set_1
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_tuple_json(self):
#         input = test_data.tuple_1
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_dict_json(self):
#         input = test_data.dict_1
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_lambda_json(self):
#         input = test_data.simple_lambda
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output(5), input(5))

#     def test_simple_function_json(self):
#         input = test_data.simple_func
#         output = selfjson_fabric.loads(selfjson_fabric.dumps(input))
#         self.assertEqual(output(4), input(4))

#     def test_complex_function_json(self):
#         input_1 = test_data.cmplx_func
#         input_2 = test_data.simple_lambda
#         output_1 = selfjson_fabric.loads(selfjson_fabric.dumps(input_1))
#         output_2 = selfjson_fabric.loads(selfjson_fabric.dumps(input_2))
#         self.assertEqual(output_1(4), input_1(4))
#         self.assertEqual(output_2(2), input_2(4))

#     def test_simple_class_json(self):
#         old_obj = test_data.SimpleClass()
#         new_obj = selfjson_fabric.loads(selfjson_fabric.dumps(old_obj))
#         # self.assertEqual(old_obj.say_kuku(), new_obj)
#         self.assertEqual(old_obj.word, new_obj.word)

#     def test_complex_class_json(self):
#         old_obj = test_data.ComplexClass()
#         new_obj = selfjson_fabric.loads(selfjson_fabric.dumps(old_obj))
#         # self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
#         self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob())
#         self.assertEqual(old_obj.const, new_obj.const)
#         # self.assertEqual(old_obj.simple_class.say_kuku(), new_obj.simple_class.say_kuku(new_obj.simple_class))    
#         self.test_simple_class_json()

#     def test_int_yaml(self):
#         input = test_data.int_glob
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_float_yaml(self):
#         input = test_data.float_glob
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_none_yaml(self):
#         input = test_data.none_glob
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_bool_yaml(self):
#         input = test_data.boolean_glob
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_string_yaml(self):
#         input = test_data.str_glob
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_list_yaml(self):
#         input = test_data.list_1
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_set_yaml(self):
#         input = test_data.set_1
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_tuple_yaml(self):
#         input = test_data.tuple_1
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     def test_dict_yaml(self):
#         input = test_data.dict_1
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output, input)

#     # def test_lambda_yaml(self):
#     #     input = test_data.simple_lambda
#     #     output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#     #     self.assertEqual(output(5), input(5))

#     def test_simple_function_yaml(self):
#         input = test_data.simple_func
#         output = selfyaml_fabric.loads(selfyaml_fabric.dumps(input))
#         self.assertEqual(output(4), input(4))

#     def test_complex_function_yaml(self):
#         input_1 = test_data.cmplx_func
#         # input_2 = test_data.simple_lambda
#         output_1 = selfyaml_fabric.loads(selfyaml_fabric.dumps(input_1))
#         # output_2 = selfyaml_fabric.loads(selfyaml_fabric.dumps(input_2))
#         self.assertEqual(output_1(4), input_1(4))
#         # self.assertEqual(output_2(2), input_2(4))

#     def test_complex_class_yaml(self):
#         old_obj = test_data.ComplexClass()
#         new_obj = selfyaml_fabric.loads(selfyaml_fabric.dumps(old_obj))
#         self.assertEqual(old_obj.simple_class.word, new_obj.simple_class.word)
#         self.assertEqual(old_obj.func_with_glob(), new_obj.func_with_glob())
#         self.assertEqual(old_obj.const, new_obj.const)
            

#     def test_simple_class_yaml(self):
#         old_obj = test_data.SimpleClass()
#         new_obj = selfyaml_fabric.loads(selfyaml_fabric.dumps(old_obj))
#         # self.assertEqual(old_obj.say_kuku(), new_obj)
#         self.assertEqual(old_obj.word, new_obj.word)

# if __name__ == '__main__':
#     unittest.main()