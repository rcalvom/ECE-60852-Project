""" CMBC Error handler """

# System
import json
import os


class CBMCErrorHandler:
    """Class to handle error parsing from cmbc report"""

    def __init__(self) -> None:
        self.errors: list[CBMCError] = []

    def parse_report(self, harness_directory: str):
        """Parse the error report present in the given directory"""
        report = self.get_report_data(harness_directory)
        print(report)

    def get_report_data(self, harness_directory: str) -> dict:
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


class CBMCError:
    """CBMC Error model"""

    def __init__(self) -> None:
        pass
