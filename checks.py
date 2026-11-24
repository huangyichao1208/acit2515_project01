"""System checks that measure host resources and evaluate requirements."""

from abc import ABC, abstractmethod

import psutil
from check_result import CheckResult

# Add SystemCheck, DiskCheck, MemoryCheck, and create_check.
# Define SystemCheck before CPUCheck because CPUCheck inherits from it.
class SystemCheck (ABC):
    name: str

    def __init__ (self, requirement, description):
        self.requirement = requirement
        self.description = description

    @abstractmethod
    def measure(self):
        pass

    def run (self):
        measured = self.measure()
        passed = measured >= self.requirement

        return CheckResult (
            self.name,
            self.description,
            measured,
            self.requirement,
            passed
        )

class CPUCheck(SystemCheck):
    """Check the number of logical CPUs."""

    name = "CPUs"

    def measure(self) -> int:
        """Return the logical CPU count."""
        return psutil.cpu_count()

class DiskCheck (SystemCheck):
    name = "Disk Space"

    def measure(self) -> int:
        return psutil.disk_usage("/").free / (1024 ** 3)

class MemoryCheck (SystemCheck):
    name = "Memory"

    def measure(self) -> int:
        return psutil.virtual_memory().total / (1024 ** 3)

def create_check (specification):
    check_type = specification["type"]
    requirement = specification["requirement"]
    description = specification["description"]

    if check_type == "disk":
        return DiskCheck (requirement, description)
    elif check_type == "memory":
        return MemoryCheck (requirement, description)
    elif check_type == "cpu":
        return CPUCheck (requirement, description)
    else:
        raise ValueError (f"Unknown check_type: {check_type}")