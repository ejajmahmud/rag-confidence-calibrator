"""CLI for rag-confidence-calibrator."""
import sys
import argparse
from .calibrator import ConfidenceCalibrator


def main():
    parser = argparse.ArgumentParser(description="RAG Confidence Calibrator")
    parser.add_argument("--claim", default="Python 3.12 released in 2023", help="Claim")
    parser.add_argument("--source", default="Python 3.12 was officially released in October 2023", help="Source")
    args = parser.parse_args()

    c = ConfidenceCalibrator()
    res = c.verify_grounding(args.claim, args.source)
    print(f"Grounding verification: {res}")
    sys.exit(0)


if __name__ == "__main__":
    main()
