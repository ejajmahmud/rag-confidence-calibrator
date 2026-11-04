"""Tests for rag-confidence-calibrator."""
import unittest
from rag_confidence_calibrator.calibrator import ConfidenceCalibrator


class TestConfidenceCalibrator(unittest.TestCase):
    def setUp(self):
        self.cal = ConfidenceCalibrator()

    def test_grounded_claim(self):
        claim = "Speedup was 4x across 8 nodes"
        source = "We achieved a 4x speedup across 8 nodes in our benchmark."
        res = self.cal.verify_grounding(claim, source)
        self.assertTrue(res["is_grounded"])
        self.assertEqual(len(res["unsupported_numbers"]), 0)

    def test_hallucinated_number(self):
        claim = "Speedup was 50x across 8 nodes"
        source = "We achieved a 4x speedup across 8 nodes."
        res = self.cal.verify_grounding(claim, source)
        self.assertFalse(res["is_grounded"])
        self.assertIn("50x", res["unsupported_numbers"])


if __name__ == "__main__":
    unittest.main()
