import unittest

import test

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)