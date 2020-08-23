import urllib.request as req 


req_url =  req.urlopen('https://www.eaglerocketry.club')

print(req_url.read())

"""
url = "http://www.eaglerocketry.club"

site = urllib3.urlopen(url)

print(site.read())

"""
