#!/bin/sh

set -o errexit
set -o pipefail

ARG="$@"

case "$ARG" in
    test)
        export PYTHONDONTWRITEBYTECODE=1

        # Run application
        python app.py &

        # Wait fot application
        while ! nc -z localhost 5000; do   
            sleep 0.1
        done

        # Execute tests
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
