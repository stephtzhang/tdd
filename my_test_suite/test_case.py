class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def summary(self):
        return "{} run, {} failed".format(self.runCount, self.errorCount)

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def setUp(self):
        self.log += "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception