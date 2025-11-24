""" Utils functions for agent"""

# System
import os


def restore_backup_if_found(harness_file_path: str):
    """Restore the a backup to a harness function"""
    backup_path = f"{harness_file_path}.backup"
    if not os.path.exists(backup_path):
        return
    with open(harness_file_path, "w", encoding="utf-8") as harness_file:
        with open(backup_path, "r", encoding="utf-8") as backup_file:
            harness_file.write(backup_file.read())


def create_backup(harness_file_path: str):
    """ Create a backup of a harness file"""
    backup_path = f"{harness_file_path}.backup"
    with open(harness_file_path, "r", encoding="utf-8") as harness_file:
        with open(backup_path, "w", encoding="utf-8") as backup_file:
            backup_file.write(harness_file.read())
