""" Proof debugger"""

# Proof debugger
from proof_debugger.agent.llm import LLM
from proof_debugger.host import HostManager
from proof_debugger.utils import setup_logger
import proof_debugger.agent.utils as agent_utils

logger = setup_logger(__name__)


class ProofDebugger:
    """Proof debugger given an initial harness function and project"""

    def __init__(
        self,
        project_directory: str,
        harness_directory: str,
        harness_file_path: str,
    ) -> None:
        # self.llm = LLM()
        self.host = HostManager(
            hostname="tools-environment",
            username="debuggeruser",
        )
        self.project_directory = project_directory
        self.harness_directory = harness_directory
        self.harness_file_path = harness_file_path

    def generate(self) -> bool:
        """Iterates over errors"""
        agent_utils.restore_backup_if_found(self.harness_file_path)
        make_success = self.__execute_make()
        if not make_success:
            logger.error("Initial proof does not build successfully.")
            return False
        agent_utils.create_backup(self.harness_file_path)
        error = self.__pop_error()
        # while error is not None:
        #     logger.info("Target Error: %s", error)
        #     result = self.generate_single_fix(error)
        #     if not result:
        #         return False
        #     error = self.__pop_error()
        return True

    # def generate_single_fix(self, error: CBMCError) -> bool:
    #     """Generate the fix of a given error"""
    #     for attempt in range(1, self.__max_attempts + 1):
    #         logger.info("Attempt: %i", attempt)
    #         logger.info("Cluster: %s", error.cluster)
    #         logger.info("Error id: %s", error.error_id)
    #         self.__refine_harness_file(error)
    #         self.__execute_make()
    #         if self.__is_error_solved(error):
    #             logger.info("Error resolved!")
    #             return True
    #     logger.info("Error not resolved...")
    #     return False

    def __execute_make(self) -> bool:
        return_code, _out = self.host.run_make(
            working_dir=self.harness_directory,
        )
        return return_code == 0

    def __pop_error(self):
        pass
        # Create Error report
        # Return the first Error
