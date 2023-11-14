# features we're looking for in the config
check_features = {}
check_features["MULTICAST"]= ["ip multicast-routing", "ipv6 multicast-routing", "ip pim", "ip igmp", "router bgp", "address family ipv4 mvpn", "mdt default"]

# input config from the customer - change this to a text file
customer_input = "router bgp mdt default switching tme team rocks"

print("Hello, AMA!")
print(check_features)

features_in_customer_input = {}
features_in_customer_input["MULTICAST"] = []


### for features not tied to an interface
for feature in check_features["MULTICAST"]:
    if(feature in customer_input):
        features_in_customer_input["MULTICAST"].append(feature)
        

print("Features in customer_input['Multicast']")
print(features_in_customer_input)



### for features that are tied to an interface
# if matches "InterfaceGig" or "InterfaceTen" ... (such as Gig, Ten, Tw, Hun, etc) -- what are all the int names we want to look for?
# look for the feature
