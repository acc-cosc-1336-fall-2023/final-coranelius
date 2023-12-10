#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests.question_tests import TestAncestorConsensus

# Create a test suite
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestAncestorConsensus('test_get_most_likely_ancestor_consensus'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())