from botocore.vendored import requests
import os

sites = {
    "us-east-2": ["https://www.airbnb.com"],
    "us-east-1": ["https://www.airbnb.com"],
    "us-west-1": [
        "https://www.airbnb.com.bz", "https://www.airbnb.co.cr",
        "https://www.airbnb.com.sv", "https://www.airbnb.com.gt",
        "https://www.airbnb.com.hn", "https://www.airbnb.mx",
        "https://www.airbnb.com.ni", "https://www.airbnb.com.pa",
        "https://www.airbnb.com"
    ],
    "us-west-2": ["https://www.airbnb.com"],
    "ap-northeast-1": ["https://www.airbnb.jp", "https://www.airbnb.com"],
    "ap-northeast-2": ["https://www.airbnb.co.kr", "https://www.airbnb.com"],
    "ap-south-1": ["https://www.airbnb.co.in", "https://www.airbnb.com"],
    "ap-southeast-1": [
        "https://zh.airbnb.com", "https://www.airbnb.com.hk",
        "https://www.airbnb.co.id", "https://www.airbnb.com.my",
        "https://www.airbnb.com.sg", "https://www.airbnb.com.tw",
        "https://th.airbnb.com", "https://www.airbnb.com"
    ],
    "ap-southeast-2": [
        "https://www.airbnb.com.au", "https://www.airbnb.co.nz",
        "https://www.airbnb.com"
    ],
    "ca-central-1": ["https://www.airbnb.ca", "https://www.airbnb.com"],
    "eu-central-1": [
        "https://www.airbnb.at", "https://www.airbnb.cz",
        "https://www.airbnb.dk", "https://www.airbnb.fi",
        "https://www.airbnb.de", "https://www.airbnb.gr",
        "https://www.airbnb.hu", "https://www.airbnb.it",
        "https://www.airbnb.com.mt", "https://www.airbnb.pl",
        "https://www.airbnb.ru", "https://www.airbnb.ch",
        "https://www.airbnb.com.tr", "https://www.airbnb.com"
    ],
    "eu-west-1": [
        "https://www.airbnb.is", "https://www.airbnb.ie",
        "https://www.airbnb.no", "https://www.airbnb.se",
        "https://www.airbnb.com"
    ],
    "eu-west-2": ["https://www.airbnb.co.uk", "https://www.airbnb.com"],
    "eu-west-3": [
        "https://www.airbnb.be", "https://www.airbnb.fr",
        "https://www.airbnb.nl", "https://www.airbnb.pt",
        "https://www.airbnb.es", "https://www.airbnb.com"
    ],
    "sa-east-1": [
        "https://www.airbnb.com.bo", "https://www.airbnb.com.br",
        "https://www.airbnb.cl", "https://www.airbnb.com.co",
        "https://www.airbnb.com.ec", "https://www.airbnb.gy",
        "https://www.airbnb.com.py", "https://www.airbnb.com.pe",
        "https://www.airbnb.co.ve", "https://www.airbnb.com"
    ],
}


def run(event, context):
    rooms = os.getenv('rooms').split()
    region = os.getenv('region').split()
    for site in sites[region]:
        for room in rooms:
            print(region, site + '/rooms/' + room)
            resp = requests.get(site+'/rooms/'+room)
            print(site, resp.status_code)
