""" Host Manager"""

# System
import subprocess

# Proof debugger
from proof_debugger.utils import setup_logger

logger = setup_logger(__name__)


class HostManager():
    """Host Manager handler, the only access to host"""

    def __init__(self, hostname: str, username: str) -> None:
        self.hostname = hostname
        self.username = username

    def run_make(self, working_dir: str) -> tuple[int, str | None]:
        """ Run make in a given repository"""
        return self.execute_command(working_dir, "make")

    def execute_command(self, working_dir: str, command: str) -> tuple[int, str | None]:
        """Execute a command in a remote working directory using system SSH."""
        full_command = f"cd {working_dir} && {command}"
        ssh_command = [
            "ssh",
            "-o", "StrictHostKeyChecking=no",
            f"{self.username}@{self.hostname}",
            full_command
        ]
        with subprocess.Popen(
            ssh_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        ) as process:
            try:
                out, err = process.communicate(timeout=5)
                if process.returncode != 0:
                    logger.error(
                        "Command failed (%d): %s",
                        process.returncode,
                        err.strip(),
                    )
                return process.returncode, out.strip()
            except subprocess.TimeoutExpired:
                logger.error("SSH command timed out")
                process.terminate()
                try:
                    out, err = process.communicate(timeout=2)
                except subprocess.TimeoutExpired:
                    process.kill()
                    out, err = process.communicate()
                return process.returncode, out.strip()
