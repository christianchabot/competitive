import re

ip = input()

pattern = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}\.){3}25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}"
if re.search(pattern, ip) != None:
    print("%s is a valid IP address." % ip)
else:
    print("%s is not a valid IP address." % ip)
