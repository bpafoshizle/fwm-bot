#!/bin/bash

kubectl create secret generic discord \
    --from-literal=token="${DISCORD_PROD_TOKEN}" \
    --from-literal=dscrd-chnl-general="${DSCRD_PROD_CHNL_GENERAL}" \
    --dry-run=client -o yaml \
    | kubectl --kubeconfig ~/.kube/bletchley-config -n fwm-bot apply -f -

