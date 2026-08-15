#!/bin/bash

# variables
IMAGE=andexor/andexor-grass-soa-service
VERSION=1

# See if there is an existing image.
ID=$(docker image list --quiet ${IMAGE}:${VERSION})

# If there is, remove it.
if [[ -n "${ID}" ]]; then
    docker image rm ${ID}
fi

# Build a new image.
docker build --tag ${IMAGE}:${VERSION} .
