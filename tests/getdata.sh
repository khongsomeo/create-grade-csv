#!/bin/bash

sample_txt="https://gist.githubusercontent.com/trhgquan/6155aa526d2161cda267f09b7cacbfbc/raw/75cb52b46c690536ca951952bfcb7adfeff9dcce/sample.txt"

sample_html="https://gist.githubusercontent.com/trhgquan/6155aa526d2161cda267f09b7cacbfbc/raw/75cb52b46c690536ca951952bfcb7adfeff9dcce/sample.html"

mkdir -p tests/data

curl -H "Accept: application/text" -H "Content-type: application/text" -X GET $sample_txt >> tests/data/sample.txt

curl -H "Accept: application/text" -H "Content-type: application/text" -X GET $sample_html >> tests/data/sample.html
