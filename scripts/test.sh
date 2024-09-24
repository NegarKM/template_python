#!/usr/bin/env bash

source scripts/common.sh

docker rm --force "${TEST_CONTAINER_NAME}" 2>/dev/null ||
    echo "Container ${TEST_CONTAINER_NAME} does not exist. Creating..."

#set -e

docker build \
    --tag "${TEST_BUILD_IMAGE_NAME}" \
    .

docker build \
    --tag "${TEST_IMAGE_NAME}" \
    --build-arg BUILD_IMAGE=${TEST_BUILD_IMAGE_NAME} \
    --no-cache \
    --file tests/Dockerfile \
    .

docker run \
    --name "${TEST_CONTAINER_NAME}" \
    --env-file ".env" \
    --env DB_INIT_FILE="tests/database/init_db.sql" \
    --env TEST_MODE=True \
    --interactive \
    --tty \
    "${TEST_IMAGE_NAME}"
