#!/bin/bash
set -e
VER=${1:-v$(date +%Y%m%d%H%M%S)}
docker build -t your-dockerhub-username/aceest_fitness:${VER} .
echo "Built image: your-dockerhub-username/aceest_fitness:${VER}"
