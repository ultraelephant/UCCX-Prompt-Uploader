# UCCX-Prompt-Uploader
Upload uccx prompts via REST Api

Prompts should be converted to valid audio format (8kbit mono U-law)

Keys by order:

-s [--ssl] validate ssl connection
-f [--force] force overwrite existing prompt
-a [--promptname] full or relative prompt file name | mandatory
-u [--username] uccx rest api user name            | mandatory
-p [--password] uccx rest api user password        | mandatory
-d [--directory] uccx prompt storage directory     | mandatory

Example usage:

python3 uccxpu.py -f -a testupload.wav -u uccxadmin -p uccxadminpassword -d default 10.10.10.10
