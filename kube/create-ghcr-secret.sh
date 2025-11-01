#!/bin/bash

kubectl --kubeconfig ~/.kube/bletchley-config \
    -n fwm-bot \
    create secret docker-registry ghcr-fwm-bot \
        --docker-server=ghcr.io \
        --docker-username="${GITHUB_USERNAME}" \
        --docker-password="${GITHUB_PACKAGE_TOKEN}"  \
        --docker-email="${GITHUB_EMAIL}"