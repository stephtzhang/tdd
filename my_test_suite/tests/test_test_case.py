# TODO
# ----
# make TestSuite from a TestCase class
# catch and report setUp errors
# call tests from script in my_test_suite and nix importing hack

# hack to add parent dir to python's search path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../..'))

from my_test_suite.test_case import WasRun, TestCase, TestResult, TestSuite


class TestTestCase(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(test.log == "setUp testMethod tearDown ")

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 0 failed")

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 1 failed")

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert(self.result.summary() == "2 run, 1 failed")

suite = TestSuite()
suite.add(TestTestCase("testTemplateMethod"))
suite.add(TestTestCase("testResult"))
suite.add(TestTestCase("testFailedResult"))
suite.add(TestTestCase("testSuite"))
result = TestResult()
suite.run(result)
print result.summary()
