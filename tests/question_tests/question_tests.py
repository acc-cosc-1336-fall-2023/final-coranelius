import unittest
from src.question_d.question_d import get_most_likely_ancestor_consensus


class TestAncestorConsensus(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"
        
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
       
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 4)
        self.assertEqual(result[2], 10)

if __name__ == '__main__':
    unittest.main()