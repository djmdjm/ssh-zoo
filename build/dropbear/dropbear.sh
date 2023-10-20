#!/bin/sh

fatal() {
	echo "$@" 1>&2
	exit 1
}

name="$1"
test -z "$name" && fatal "usage: dropbear.sh version"
ref="DROPBEAR_$name"
opwd="$PWD"

dir="dropbear-${ref}"
instdir="$opwd/dropbear-$name"
patchesdir="$PWD/patches-$name"

J=""
which nproc >/dev/null && J="-j `nproc`"

set -xe

rm -rf $dir
git clone --branch $ref --depth 1 https://github.com/mkj/dropbear $dir
cd $dir
test -d $patchesdir && git am $patchesdir/*
autoconf
autoheader
./configure \
    --enable-bundled-libtom \
    --prefix="$instdir" \
    --libdir="$instdir/lib" --includedir="$instdir/include" \
    --libexecdir="$instdir/libexec" --sysconfdir="$instdir/etc"
make $J
make install
cd ..
rm -rf $dir
