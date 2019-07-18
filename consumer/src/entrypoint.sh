#!/bin/sh

set -o errexit
set -o pipefail

ARG="$@"

case "$ARG" in
    verify)
        pactman-verifier -l ./pact/Consumer-Provider-pact.json Consumer ${API_PROVIDER_URL} ${API_PROVIDER_URL}/_pact/provider_state --verbose
    ;;
    test)
        export PYTHONDONTWRITEBYTECODE=1

        pytest --verbose -p no:cacheprovider 
    ;;
    dev)
        export PYTHONDONTWRITEBYTECODE=1
        
        python app.py
    ;;
    prd)
        # TO DO
    ;;
    *)
        $ARG
    ;;
esac