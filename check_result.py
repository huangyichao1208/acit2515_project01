
class CheckResult:
    def __init__ (self, name, description, measured, requirement, passed):
        self.name = name
        self.description = description
        self.measured = measured
        self.requirement = requirement
        self.passed = passed

    def to_dict(self):
        dict_export = {
            "name": self.name,
            "description": self.description,
            "measured": self.measured,
            "requirement": self.requirement,
            "passed": self.passed
        }
        return dict_export
    
    def __str__(self):
        status = "PASS" if self.passed else "FAIL" # condense 4 sentences into 1
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Measured: {self.measured}\n"
            f"Requirement: {self.requirement}\n"
            f"Result: {status}"
        )