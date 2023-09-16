#!/usr/bin/env bash

DIR=$(realpath $0) && DIR=${DIR%/*}
cd $DIR
set -ex

if ! command -v bumpversion &>/dev/null; then
  pip install bumpversion
fi
bumpversion patch
rm -rf dist
python setup.py sdist
twine upload dist/*
