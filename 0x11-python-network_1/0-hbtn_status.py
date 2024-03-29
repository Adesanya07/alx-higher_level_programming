#!/usr/bin/python3

"""fetches https://alx-intranet.hbtn.io/status."""

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response = response.read()

    print("Body response:")
    print("\t- type {}:".format(type(response)))
    print("\t- content {}:".format(response))
    print("\t- utf8 content {}:".format(response.decode('utf-8')))
