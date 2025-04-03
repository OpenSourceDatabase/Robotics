#!/usr/bin/env bash

if ! docker -v &>/dev/null; then
  echo "Prerequisite error: Docker not found"
  exit 1
fi

docker run --rm -it -p 8000:8000 ghcr.io/opensourcedatabase/robotics:main

