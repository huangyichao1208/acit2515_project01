from checks import create_check
from audit_report import AuditReport

class Audit:
    def __init__(self, definition):
        self.audit_id = definition["audit_id"]
        self.audit_description = definition["audit_description"]
        specifications = definition ["checks"]

        if not isinstance(self.audit_id, str) or not self.audit_id.strip():
            raise ValueError ("Invalid audit ID")
        
        if not isinstance(self.audit_description, str) or not self.audit_description.strip():
            raise ValueError("Invalid audit description")

        if not isinstance(specifications,list):
            raise ValueError("Checks must be a list!")

        self.checks = [
            create_check (specification) for specification in specifications
        ]

    def run (self):
        results = [
            check.run() for check in self.checks
        ]
        return AuditReport (
            results,
            self.audit_id,
            self.audit_description
        )
