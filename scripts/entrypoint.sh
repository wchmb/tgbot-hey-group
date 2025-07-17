#!/usr/bin/env sh

set -e

echo "Service 'All': Status"
rc-status -a

echo "Service 'at': Starting ..."
rc-service atd start

exec $@