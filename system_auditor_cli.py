import sys
import json
from audit import Audit

def main():
    if len(sys.argv) not in (2,3):
        print ("Usage: system_auditor_cli.py input.json [output.json]")
        return
        
    input_file = sys.argv[1]

    with open (input_file, "r") as file:
        definition = json.load (file)

    audit = Audit (definition)
    report = audit.run()
    print (report)

    if len(sys.argv) == 3:
        output_file = sys.argv[2]

        with open (output_file, "w", encoding = "utf-8") as file:
            json.dump (report.to_dict(),file,indent=4)

if __name__ == "__main__":
    main()