#!/bin/bash

wget --no-check-certificate https://wordnetcode.princeton.edu/wn3.1.dict.tar.gz
tar -xvf wn3.1.dict.tar.gz

cd dict

egrep -o "^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s[a-zA-Z_]*\s" data.adj | cut -d ' ' -f 5 > conv.data.adj
egrep -o "^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s[a-zA-Z_]*\s" data.adv | cut -d ' ' -f 5 > conv.data.adv
egrep -o "^[0-9]{8}\s[0-9]{2}\s[a-z]\s[0-9]{2}\s[a-zA-Z_]*\s" data.verb | cut -d ' ' -f 5 > conv.data.verb

cd ..
mv conv* ../wordnet_vocab
rm -r dict