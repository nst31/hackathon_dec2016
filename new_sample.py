import json
with open('sample.json') as f:
    d = json.load(f)
d["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["protocol"] = "udp"
print (d)
d["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"
d["featureConfigs"]["features"][5]["ospf"]["enabled"] = "true"
d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] =  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] +  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["keepAliveTimer"]

d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] =  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] +  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["keepAliveTimer"]

d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] =  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] +  d["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["keepAliveTimer"]

print (d)


with open("sample.json", "w") as f:
    f.write(json.dumps(d))
