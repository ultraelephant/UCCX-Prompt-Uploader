#!/bin/bash

curl -u $3:$4 -k --request POST \
  --url https://$1/adminapi/prompt/uploadFile/ \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: multipart/form-data' \
  --form mimetype=multipart/form-data \
  --form file=@$2
