# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

from dataclasses import asdict
from . import soa
import json

def main() -> None:
    report:soa.SOAReport = soa.getSOAReport()
    print(json.dumps(asdict(report), indent = 4))
