"""Grounding and hallucination confidence calibrator for RAG."""
import re
from typing import Dict, Any


class ConfidenceCalibrator:
    def verify_grounding(self, claim: str, source_text: str) -> Dict[str, Any]:
        claim_numbers = re.findall(r"\b\d+(?:\.\d+)?[a-zA-Z%]*\b", claim)
        source_numbers = set(re.findall(r"\b\d+(?:\.\d+)?[a-zA-Z%]*\b", source_text))

        # Check number support
        unsupported_numbers = [n for n in claim_numbers if n not in source_numbers]

        # Word overlap
        claim_words = set(re.findall(r"\w+", claim.lower()))
        source_words = set(re.findall(r"\w+", source_text.lower()))
        overlap = len(claim_words & source_words) / (len(claim_words) or 1)

        is_grounded = len(unsupported_numbers) == 0 and overlap >= 0.5
        confidence = round(overlap * (0.2 if unsupported_numbers else 1.0), 2)

        return {
            "is_grounded": is_grounded,
            "confidence_score": confidence,
            "unsupported_numbers": unsupported_numbers,
            "lexical_overlap": round(overlap, 2)
        }
