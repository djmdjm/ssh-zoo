#!/bin/sh

fatal() {
	echo "$@" 1>&2
	exit 1
}

name="$1"
test -z "$name" && fatal "usage: putty.sh version"
url="https://the.earth.li/~sgtatham/putty/latest/putty-${name}.tar.gz"
opwd="$PWD"

dir="putty-build-${name}"
instdir="$opwd/putty-$name"

J=""
which nproc >/dev/null && J="-j `nproc`"

set -xe

rm -rf $dir $instdir
curl -L $url | tar zxvf -
mv $instdir $dir
cd $dir
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$instdir ..
make $J
make install
cd ../..
rm -rf $dir
