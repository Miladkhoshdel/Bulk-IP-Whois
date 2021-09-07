from ipwhois import IPWhois

def ip_whois(ip):
    ip = ip.strip()
    obj = IPWhois(ip)
    res = obj.lookup_whois()
    if res["asn_description"]:
        res_d = str(res["asn_description"])
    else:
        res_d = "No Description Available"
    if res["asn"]:
        res_n = str(res["asn"])
    else:
        res_n = "No Name Available"
    return str(ip) + "\t" + res_d + "(" + res_n + ")"


f = open("a.txt", "r")
o = open("o.txt", "w")
ll = []
i = 0

for line in f:
    i = i + 1
    a = ip_whois(line)
    print(str(i) + ") " + a)
    ll.append(a)

o = open("o.txt", "w")
for item in ll:
    o.writelines(item + "\n")
o.close()
