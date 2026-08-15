#!/bin/bash

# variables
IMAGE=andexor/andexor-grass-soa-service
VERSION=1

# debug
docker run -it --rm ${IMAGE}:${VERSION} /bin/bash
