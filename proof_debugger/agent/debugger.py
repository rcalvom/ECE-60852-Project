""" Proof debugger"""



# Proof debugger
# from proof_debugger.agent.llm import LLM
from proof_debugger.agent import CBMCErrorHandler
from proof_debugger.host import HostManager
from proof_debugger.utils import setup_logger
import proof_debugger.agent.utils as agent_utils
from proof_debugger.agent.models import ProofDebuggerResponse, CBMCError, FixResult

logger = setup_logger(__name__)

class ProofDebugger:
    """Proof debugger given an initial harness function and project"""

    def __init__(
        self,
        project_directory: str,
        harness_directory: str,
        target_function_name: str,
        target_file_path: str,
    ) -> None:
        self.host = HostManager(
            hostname="tools-environment",
            username="debuggeruser",
        )
        # self.llm = LLM()
        self.error_manager = CBMCErrorHandler(harness_directory)
        self.project_directory = project_directory
        self.harness_directory = harness_directory
        self.target_function_name = target_function_name
        self.target_file_path = target_file_path
        self.__max_attempts = 3

    def generate(self) -> bool:
        """Iterates over errors"""
        # agent_utils.restore_backup_if_found(self.harness_directory)
        make_success = self.__execute_make()
        if not make_success:
            logger.error("Initial proof does not build successfully.")
            return False
        # agent_utils.create_backup(self.harness_directory)
        self.error_manager.parse_report()
        error = self.error_manager.get_next_error()
        while error is not None:
            logger.info("Target Error: %s", error)
            result = None
            for attempt in range(1, self.__max_attempts + 1):
                result = self.generate_single_fix(attempt, error, result)
                if result == FixResult.SOLVED:
                    break
            if result == FixResult.SOLVED:
                logger.info("Error resolved!")
            else:
                logger.warning("Error not resolved...")
            self.error_manager.add_error_to_skip(error)
            error = self.error_manager.get_next_error()
        return len(self.error_manager.errors) == 0

    def generate_single_fix(
        self,
        attempt: int,
        error: CBMCError,
        previous_result: FixResult | None,
    ) -> FixResult:
        """Generate the fix of a given error"""
        logger.info("Attempt: %i", attempt)
        logger.info("Cluster: %s", error.error_cluster)
        logger.info("Error id: %s", error.error_id)
        # TODO: Select the prompt
        response = self.prompt_to_llm()
        # agent_utils.update_harness_content(response.updated_harness_code, self.harness_directory)
        make_success = self.__execute_make()
        if not make_success:
            logger.error("Proof does not build successfully.")
            return FixResult.BUILD_ERROR
        self.error_manager.parse_report()
        if self.error_manager.exist_in_report(error):
            logger.info("Error still present in the report.")
            return FixResult.NOT_SOLVED
        return FixResult.SOLVED
    
    def prompt_to_llm(self) -> ProofDebuggerResponse:
        """Prompt the LLM and get the response"""
        # self.llm
        return ProofDebuggerResponse("", "", "")  # TODO: Implement LLM interaction

    def __execute_make(self) -> bool:
        return_code, _out = self.host.run_make(
            working_dir=self.harness_directory,
        )
        return return_code == 0