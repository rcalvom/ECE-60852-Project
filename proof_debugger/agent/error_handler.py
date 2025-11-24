""" CMBC Error handler """


# System
import json
import os

# Utils
from dataclasses import dataclass




class CBMCErrorHandler:
    """Class to handle error parsing from cmbc report"""

    def __init__(self, harness_directory: str) -> None:
        self.harness_directory = harness_directory
        self.errors: list[CBMCError] = []
        # TODO: SKIP ERRORS

    def parse_report(self):
        """Parse the error report present in the given directory"""
        report = self.__get_report_data(self.harness_directory)
        # TODO: CONVERT THE REPORT IN A LIST OF ERRORS

    def get_next_error(self) -> CBMCError | None:
        """Get the next error to be processed"""
        if not self.errors:
            return None
        return self.errors.pop(0)
    
    def add_error_to_skip(self, error: CBMCError) -> None:
        """Add an error to the skip list"""
        # TODO: Implement skipping logic
        
    def exist_in_report(self, error: CBMCError) -> bool:
        """Check if the error still exists in the report"""
        return True  # TODO: Implement actual check

    def __get_report_data(self, harness_directory: str) -> dict:
        """Retrieve the error data"""
        json_report_path = os.path.join(
            harness_directory,
            "/build/report/json"
        )
        json_files = [
            f for f in os.listdir(json_report_path)
            if os.path.isfile(os.path.join(json_report_path, f))
        ]
        result = {}
        for json_file in json_files:
            with open(os.path.join(json_report_path, json_file), "r", encoding="utf-8") as f:
                result.update(json.loads(f.read()))
        return result
