import requests
import argparse
import sys
import click
import subprocess
import os





argparser = argparse.ArgumentParser()
argparser.add_argument('-s', '--ssl' , default=False, action='store_true', help='Turn on SSL certificate verification')
argparser.add_argument('-f', '--force' , default=False, action='store_true', help='Force overwrite prompt')
argparser.add_argument('-a', '--promptname' , action='store', help='Full or relative prompt file name')
argparser.add_argument('-u', '--username' , action='store', help='Username')
argparser.add_argument('-p', '--password' , action='store', help='Password')
argparser.add_argument('-d', '--directory' , action='store', help='Prompt directory on UCCX. Should be without first and last slashes')
argparser.add_argument('url', help='UCCX Publisher IP or FQDN')
args = argparser.parse_args()





def filecheck (link,usr,pwd,sec):
 headers = {
  'Cache-Control': "no-cache",
 }
 response = requests.request("GET", link, auth=(usr, pwd), headers=headers, verify=sec)
 return(response.status_code)

def filedelete (link,usr,pwd,sec):
 headers = {
  'Cache-Control': "no-cache",
 }
 response = requests.request("DELETE", link, auth=(usr, pwd), headers=headers, verify=sec)

def fileupload (link,usr,pwd,file):
 subprocess.call([os.path.dirname(os.path.realpath(__file__))+'/uploader.sh', link, file, usr, pwd])
	
def filemove (link,usr,pwd,sec,dir,file):
 link_to_upload = "https://"+link+"/adminapi/prompt/"
 payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Files xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"../adminapi/src/main/resources/xsd/Files.xsd\">\n<Prompt>\n<File>\n <path>/"+dir+"/</path>\n<FileName>"+file+"</FileName>\n</File>\n</Prompt>\n</Files>"
 headers = {
 'Content-Type': "application/xml",
 'Cache-Control': "no-cache",
 }
 response = requests.request("POST", link_to_upload, auth=(usr, pwd), data=payload, headers=headers, verify=sec)
 return (response.text)





if os.path.isfile(args.promptname):
 prompt_filename = args.promptname.split("/")
 prompt_ext = prompt_filename[-1].split(".")
 if len(prompt_ext)<2 or prompt_ext[-1].lower() != "wav":
  sys.exit("Prompt must have valid WAV filename")
else:
 sys.exit("Prompt must be a file")

url = 'https://'+args.url+'/adminapi/prompt/'+args.directory+'/'+prompt_filename[-1]
check_status_code = filecheck (url,args.username,args.password,args.ssl)

if check_status_code == 200:
 if args.force:
  filedelete (url,args.username,args.password,args.ssl)
 else:
  if click.confirm('File exist. Do you want to replace it?', default=False):
   filedelete (url,args.username,args.password,args.ssl)
  else:
   sys.exit("User abort")
elif check_status_code == 404:
 print ('File not exist on uccx server')
else:
 sys.exit("Web server returned code: " + str(check_status_code))

fileupload (args.url,args.username,args.password,args.promptname)
print (filemove (args.url,args.username,args.password,args.ssl,args.directory,prompt_filename[-1]))
