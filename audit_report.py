class AuditReport:
    def __init__ (self, results, audit_id, audit_description):
        self.results = results
        self.audit_id = audit_id
        self.audit_description = audit_description

    @property
    def passed(self):
        return all(result.passed for result in self.results)

    def to_dict (self):
        return {
            "audit_id": self.audit_id,
            "audit_description": self.audit_description,
            "checks": [result.to_dict() for result in self.results], # list comprehension
            "passed": self.passed
        }

    def __str__ (self):
        status = "PASS" if self.passed else "FAIL"
        results_text = "\n\n".join(str(result) for result in self.results)

        return (
            f"System Auditor\n"
            f"Audit ID: {self.audit_id}\n"
            f"Description: {self.audit_description}\n\n"
            f"{results_text}\n\n"
            f"OVERALL: {status}"
        )
    