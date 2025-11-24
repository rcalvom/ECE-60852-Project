"""Proof debugger response model"""

# System
from enum import Enum

# Utils
from dataclasses import dataclass


class FixResult(Enum):
    """Fix Result Enum"""
    SOLVED = "Solved"
    NOT_SOLVED = "NotSolved"
    BUILD_ERROR = "BuildError"


@dataclass
class CBMCError:
    """CBMC Error model"""
    error_cluster: str
    error_id: str


@dataclass
class ProofDebuggerResponse:
    """Proof debugger response from the LLM"""
    analysis: str
    fix_recomendation: str
    updated_harness: str
