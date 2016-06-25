from my_test_suite.test_case import WasRun, TestCase, TestResult, TestSuite

class TestTestCase(TestCase):
    def setUp(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(test.log == "setUp testMethod tearDown ")

    def test_result(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 0 failed")

    def test_failed_result(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 1 failed")

    def test_test_suite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert(self.result.summary() == "2 run, 1 failed")

