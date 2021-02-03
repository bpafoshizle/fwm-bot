#!/bin/bash

kubectl --kubeconfig ~/.kube/bletchley-config \
    -n egroup-bot \
    create secret generic discord \
        --from-literal=token="${DISCORD_TOKEN}"