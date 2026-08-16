<!--
SPDX-License-Identifier: Apache-2.0
Copyright 2026 Andexor Network, Inc.
Author: Ed Jenkins<ed@andexor.net>
-->

# Install Pre-requisites

Most projects have certain pre-requisites that are required for development, testing, or running in production. Install the ones that are needed.

## Python

Follow these instructions to setup a development environment for projects that are written in Python. The latest Python interpreter should already be installed on your system.

### uv

For projects written in Python, you need to use the uv package manager to install the third-party modules they depend on. uv is not available in a standard OS package format. It needs to be installed via this script.

> Run `install-uv.sh`

Do not use npm, pip, pnpm, or other legacy tools like them. They have funamental vulnerabilities that have been addressed by uv.

### Dependency cooldowns

In order to protect against using malicious code, a 1 week delay is suggested between when a package is published and when it is used. Most security issues are resolved within this time frame.

Add this to the `pyproject.toml` file in your project:

> [tool.uv]<br/>
> exclude-newer = "1 week"

### Install dependencies.

Install the Python packages that this project uses.

> Run `setup.sh`<br/>
> Run `uv sync`

## TypeScript

For projects written in TypeScript, you need to use Bun for package management, builds, and execution. It needs to be installed from this script.

> Run `install-bun.sh`

## Docker

For projects that are built in Docker or run in Docker, you need to have Docker properly installed.

> Run `install-docker.sh`

This script requires a reboot, so the system will be rebooted automatically.
After rebooting, run this to verify that it is working:

> Run `docker run hello-world`
