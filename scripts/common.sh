#!/usr/bin/env bash

SERVICE_NAME="sample-api"

SERVICE_PACKAGE_NAME="api_service"
TEST_BUILD_IMAGE_NAME="${SERVICE_NAME}-build"
TEST_IMAGE_NAME="${SERVICE_NAME}-test"
TEST_CONTAINER_NAME="${SERVICE_NAME}-test"
START_IMAGE_NAME="${SERVICE_NAME}-image"
