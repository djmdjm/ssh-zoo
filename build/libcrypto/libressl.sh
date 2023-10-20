#!/bin/sh

fatal() {
	echo "$@" 1>&2
	exit 1
}

name="$1"
ref="$2"
test -z "$name" && fatal "usage: libressl.sh version [git-ref]"
test -z "$ref" && ref="$name"
opwd="$PWD"

dir="libressl-portable-${name}"
instdir="$opwd/libressl-$name"

J=""
which nproc >/dev/null && J="-j `nproc`"

set -xe

rm -rf libressl-portable-${name}
git clone --branch $ref --depth 1 https://github.com/libressl/portable $dir
cd $dir
./autogen.sh
./configure --prefix="$instdir" \
    --libdir="$instdir/lib" --includedir="$instdir/include"
make $J
make check
make install
cd ..
rm -rf libressl-portable-${name}
