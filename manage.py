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
    parser.add_argument("debugger", help="Debugger name or mode")
    parser.add_argument("--project_dir", required=True, help="Path to the project base directory")
    parser.add_argument("--harness_dir", required=True, help="Path to the harness directory")
    parser.add_argument("--harness_file", required=True, help="Path to the harness file")
    args = parser.parse_args()

    if args.debugger:
        agent = ProofDebugger(
            project_directory=args.project_dir,
            harness_directory=args.harness_dir,
            harness_file_path=args.harness_file,
        )
        agent.generate()
    else:
        logger.info("Not in debugger mode. Exiting.")


if __name__ == "__main__":
    main()
