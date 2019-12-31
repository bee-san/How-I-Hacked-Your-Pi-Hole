from shodan import Shodan
import requests
import subprocess

IP = ""
api = Shodan('')

def url_ok(url):
    r = requests.head("http://" + url)
    return r.status_code == 200

def check_page(url):
    r = requests.get("http://" + url + "/admin/")
    return "Pi-hole" in r.text

def pruneIPS(vulnerableIPs):
    for i in vulnerableIPs:
        if not url_ok(i):
            if not check_page(i):
                vulnerableIPs.remove(i)
    return vulnerableIPs

result = api.search("pi-hole")

VulnerableIP = []
for service in result['matches']:
    if service['ip_str'] == IP:
       ulnerableIP.append(service['ip_str'])
        print("Yes")
