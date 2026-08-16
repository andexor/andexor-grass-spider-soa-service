#!/bin/bash

# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Andexor Network, Inc.
# Author: Ed Jenkins<ed@andexor.net>

# variables
IMAGE=andexor/andexor-grass-spider-soa-service
VERSION=1

# run
docker run --rm ${IMAGE}:${VERSION}
