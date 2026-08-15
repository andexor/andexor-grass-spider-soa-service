from dataclasses import asdict
from . import soa
import json

def main() -> None:
    report = soa.getSOAReport()
    print(json.dumps(asdict(report), indent = 4))
