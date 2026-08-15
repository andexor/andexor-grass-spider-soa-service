#!/bin/bash

# variables
IMAGE=andexor/andexor-grass-soa-service
VERSION=1

# run
docker run --rm ${IMAGE}:${VERSION}
