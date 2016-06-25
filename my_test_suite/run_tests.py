import inspect
import sys
import os
import re
from importlib import import_module

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '..'))
from my_test_suite.test_case import TestCase, TestSuite, TestResult

path = 'tests'

# get all test modules in the tests directory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
test_module ='^test\w+.py$'
test_module_re = re.compile(test_module)
test_modules = [f for f in files if test_module_re.match(f)]

test_func ='^test_\w+$'
test_func_re = re.compile(test_func)
# add test functions in the test modules to a new TestSuite
suite = TestSuite()
for test_module in test_modules:
    test_module = '{path}.{module}'.format(path=path, module=os.path.splitext(test_module)[0])
    imported_module = import_module(test_module)
    all_classes = inspect.getmembers(imported_module, inspect.isclass)
    test_classes = [cls_info for cls_info in all_classes if issubclass(cls_info[1], TestCase)]
    for cls_info in test_classes:
        test_class = cls_info[1]
        all_funcs = inspect.getmembers(test_class, inspect.ismethod)
        test_funcs = [func_info for func_info in all_funcs if test_func_re.match(func_info[0])]
        for func_info in test_funcs:
            func_name = func_info[0]
            suite.add(test_class(func_name))

result = TestResult()
suite.run(result)
print result.summary()


