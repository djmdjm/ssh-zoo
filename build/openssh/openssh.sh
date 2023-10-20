#!/bin/sh

fatal() {
	echo "$@" 1>&2
	exit 1
}

name="$1"
libcrypto="$2"
test -z "$name" && fatal "usage: openssh.sh version [libcrypto-version]"
test -z "$libcrypto" && libcrypto=latest
ref=$(echo "$name" | sed 's/^/V_/;s/[.]/_/')
opwd="$PWD"

dir="openssh-portable-${name}"
instdir="$opwd/openssh-$name"
libcryptodir="$PWD/../libcrypto/$libcrypto"
patchesdir="$PWD/patches-$name"

J=""
which nproc >/dev/null && J="-j `nproc`"

set -xe

rm -rf $dir
git clone --branch $ref --depth 1 \
	https://github.com/openssh/openssh-portable $dir
cd $dir
test -d $patchesdir && git am $patchesdir/*
autoreconf
env LDFLAGS="-Wl,-rpath,$libcryptodir/lib" ./configure \
    --with-ssl-dir="$libcryptodir" --with-rpath="-Wl,-rpath," \
    --prefix="$instdir" \
    --libdir="$instdir/lib" --includedir="$instdir/include" \
    --libexecdir="$instdir/libexec" --sysconfdir="$instdir/etc"
make $J
make install
cd ..
rm -rf $dir
