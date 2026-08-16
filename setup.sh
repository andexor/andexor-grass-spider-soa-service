#!/bin/bash

# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

# Modify and run this to add new dependencies.

uv add dnspython
# uv add "dnspython[aioquic]"
# uv add "dnspython[cryptography]"
# uv add "dnspython[httpx]"
uv add "dnspython[idna]"
