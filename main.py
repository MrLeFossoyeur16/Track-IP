#Import
import requests

import json
def btrack_ip():
        ip = input("IP: ")
        l_re = {}
        info = ["version", "city", "region", "region_code", "country_code", "country_code_iso3", 
                "country_name", "country_capital", "country_tld", "continent_code", "in_eu",
                "postal", "latitude", "longitude", "timezone", "utc_offset", "country_calling_code",
                "currency", "currency_name", "languages", "country_area", "country_population", "asn",
                "org", ]
                
        for x in range(len(info)):
                re = requests.get(f"https://ipapi.co/{ip}/{info[x]}/")
                l_re[info[x]] = re.text
        print(json.dumps(l_re))

if __name__ == "__main__":
        btrack_ip()


