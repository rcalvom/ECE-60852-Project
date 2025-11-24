"""Manage file"""

# System
import argparse

# Proof debugger
from proof_debugger.agent import ProofDebugger
from proof_debugger.utils import setup_logger

logger = setup_logger(__name__)


def main():
    """Entry point"""

    parser = argparse.ArgumentParser(description="Manage file with Agent")
    parser.add_argument(
        "debugger",
        help="Debugger name or mode",
    )
    parser.add_argument(
        "--project_directory",
        required=True,
        help="Path to the project base directory",
    )
    parser.add_argument(
        "--harness_directory",
        required=True,
        help="Path to the harness directory",
    )
    parser.add_argument(
        "--target_function_name",
        required=True,
        help="Name of the target function",
    )
    parser.add_argument(
        "--target_file_path",
        required=True,
        help="Path to the target function file",
    )
    args = parser.parse_args()

    if args.debugger:
        agent = ProofDebugger(
            project_directory=args.project_dir,
            harness_directory=args.harness_directory,
            target_function_name=args.target_function_name,
            target_file_path=args.target_file_path,
        )
        agent.generate()
    else:
        logger.error("Not in debugger mode. Exiting.")


if __name__ == "__main__":
    main()
