#!/bin/bash

kubectl create secret generic discord \
    --from-literal=token="${DISCORD_PROD_TOKEN}" \
    --from-literal=dscrd-chnl-general="${DSCRD_PROD_CHNL_GENERAL}" \
    --from-literal=dscrd-guild-id="${DISCORD_FWM_GUILD_ID}" \
    --dry-run=client -o yaml \
    | kubectl --kubeconfig ~/.kube/bletchley-config -n fwm-bot apply -f -

