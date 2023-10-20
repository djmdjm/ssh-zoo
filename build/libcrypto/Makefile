all: libressl-3.4.3 libressl-3.8.1 latest

latest: libressl-3.8.1
	-rm -f latest
	ln -sf libressl-v3.8.1 latest

libressl-3.4.3: libressl-v3.4.3/lib/libcrypto.a

libressl-v3.4.3/lib/libcrypto.a:
	./libressl.sh v3.4.3 OPENBSD_7_0 # Note: v3.4.3 tag fails to patch

libressl-3.8.1: libressl-v3.8.1/lib/libcrypto.a

libressl-v3.8.1/lib/libcrypto.a:
	./libressl.sh v3.8.1

clean:
	-rm -rf libressl-v3.4.3 libressl-v3.8.1

