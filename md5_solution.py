#This is a sample solution
import requests
import hashlib

URI = ""


def get_and_hash(ret):
    begin = ret.find("<h3 align='center'>") + 19
    end = ret.find("</h3>")
    md5_string = ret[begin:end].encode('utf-8')
    digest = hashlib.md5(md5_string).hexdigest()
    return digest

session = requests.Session()
s = requests.Session()
req = s.get(URI)
print(req.text) #Get the packet

md5 = get_and_hash(req.text)
req = s.post(URI, data={'action':'Submit',"user":md5}) #Post the encrypted string
print(req.text) #Get a reply
