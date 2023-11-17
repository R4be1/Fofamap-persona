import sys
import json
from tqdm import tqdm
from urllib.parse import urlparse
from extract_tld import ExtractTLD


root_domains=list()
targets=open("fofa.txt").readlines()

result_file=open("results.txt","w")
for target in tqdm(targets):
    target=target.strip()
    root_domain = ExtractTLD( urlparse(target).hostname)
    if root_domain==None:
        ip=urlparse(target).hostname
        if ip not in root_domains:
            result_file.write(target+"\n")
            root_domains.append(ip)

    if root_domain not in root_domains:
        result_file.write(target+"\n")
        root_domains.append( ExtractTLD( urlparse(target).hostname) )
print("\noutput: results.txt")


