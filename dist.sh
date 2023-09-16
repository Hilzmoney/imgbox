#!/usr/bin/env bash

DIR=$(realpath $0) && DIR=${DIR%/*}
cd $DIR
set -ex

git add -u
git commit -m.
git pull
if ! command -v bumpversion &>/dev/null; then
  pip install bumpversion
fi
bumpversion patch
git push
rm -rf dist

python setup.py sdist bdist_wheel || pip install wheel && python setup.py sdist bdist_wheel
twine upload dist/*
