# features we're looking for in the config
check_features = {}

check_features["MULTICAST"] = ["ip multicast-routing", "ipv6 multicast-routing", "ip pim", "ip igmp", "router bgp", "address family ipv4 mvpn", "mdt default"]

check_features["VRF"] = ["ip vrf", "vrf definition"]

check_features["VRF_INTERFACE"] = ["vrf forwarding"]

# input config from the customer - change this to a text file
customer_input = "router bgp mdt default switching tme team rocks ! interface GigabitEthernet0/0 vrf forwarding Mgmt-vrf no ip address shutdown negotiation auto !"

print("Hello, AMA!")
print(check_features)

features_in_customer_input = {}
features_in_customer_input["MULTICAST"] = []
features_in_customer_input["VRF_INTERFACE"] = []

### for features not tied to an interface
for feature in check_features["MULTICAST"]:
    if(feature in customer_input):
        features_in_customer_input["MULTICAST"].append(feature)
        

print("Features in customer_input['Multicast']")
print(features_in_customer_input)



### for features that are tied to an interface
# if matches 
# starting point: "InterfaceGig" or "InterfaceTen" ... (such as Gig, Ten, Tw, Hun, etc) -- what are all the int names we want to look for?
# ending point: "!"
# look for the feature
for feature in check_features["VRF_INTERFACE"]:
    
    print(feature)
    
    ## end at !
    x = customer_input.split("! interface GigabitEthernet0/0")
    print(x)
    y = x[1].split("!") # will it always be the 1st item in list?
    print(y)
    print(y[0])
    split_feature = y[0]
    if(split_feature in customer_input):
       features_in_customer_input["VRF_INTERFACE"].append(feature)
        
print("Features in customer_input")
print(features_in_customer_input)
    
