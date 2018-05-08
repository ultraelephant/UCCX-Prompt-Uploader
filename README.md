# UCCX-Prompt-Uploader
Upload uccx prompts via REST Api



Prompts should be converted to valid audio format (8kbit mono U-law)


Keys by order:


-s [--ssl] validate ssl connection

-f [--force] force overwrite existing prompt

-a [--promptname] full or relative prompt file name | __mandatory__

-u [--username] uccx rest api user name            | __mandatory__

-p [--password] uccx rest api user password        | __mandatory__

-d [--directory] uccx prompt storage directory     | __mandatory__



Example usage:


python3 uccxpu.py -f -a testupload.wav -u uccxadmin -p uccxadminpassword -d default 10.10.10.10



Uploading is process by shell script. But there is no big deal to port it on Windows, it is just cURL with several of parameters, so if you have free time - go ahead.
