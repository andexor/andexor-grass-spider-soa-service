# Install Pre-requisites

Most projects have certain pre-requisites that are required for development, testing, or running in production. Install the ones that are needed

## uv

For projects written in Python, you need to use the uv package manager to install the third-party modules they depend on. uv is not available in a standard OS package format. It needs to be installed via this script.

> Run `install-uv.sh`

Do not use npm, pip, pnpm, or other legacy tools like them. They have funamental vulnerabilities that have been addressed by uv.

### Dependency cooldowns

In order to protect against using malicious code, a 1 week delay is suggested between when a package is published and when it is used. Most security issues are resolved within this time frame.

Add this to the `pyproject.toml` file in your project:

> [tool.uv]
>
> exclude-newer = "1 week"

## Bun

For projects written in TypeScript, you need to use Bun for package management, builds, and execution. It needs to be installed from this script.

> Run `install-bun.sh`

## Docker

For projects that are built in Docker or run in Docker, you need to have Docker properly installed.

> Run `install-docker.sh`

This script requires a reboot, so the system will be rebooted automatically.
After rebooting, run this to verify that it is working:

> Run `docker run hello-world`
