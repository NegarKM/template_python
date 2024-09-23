#!/usr/bin/env bash

source scripts/common.sh

docker rm --force "${SERVICE_NAME}" 2>/dev/null ||
    echo "Container ${SERVICE_NAME} does not exist. Creating..."

#set -e

docker build \
    --tag "${START_IMAGE_NAME}" \
    .

docker run \
    --interactive \
    --publish "5001:5000" \
    --env-file ".env" \
    --name "${SERVICE_NAME}" \
    "${START_IMAGE_NAME}"
