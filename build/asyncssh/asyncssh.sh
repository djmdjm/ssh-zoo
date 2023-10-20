#!/bin/sh

fatal() {
	echo "$@" 1>&2
	exit 1
}

name="$1"
test -z "$name" && fatal "usage: asyncssh.sh version"
ref="v$name"
opwd="$PWD"

dir="asyncssh-${ref}"
instdir="$opwd/asyncssh-$name"
patchesdir="$PWD/asyncssh-$name"

set -xe

rm -rf $dir
git clone --branch $ref --depth 1 https://github.com/ronf/asyncssh $dir
cd $dir
python3 setup.py build
cd ..
mv $dir/build $instdir
rm -rf $dir
