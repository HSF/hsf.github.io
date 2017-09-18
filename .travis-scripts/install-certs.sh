#! /bin/bash
#
# Install extra certificates for HTML proofer
#
cp -v $(dirname $0)/ca/*.crt /usr/local/share/ca-certificates
/usr/sbin/update-ca-certificates
