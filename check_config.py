# features we're looking for in the config
check_features = {}

check_features["MULTICAST"] = ["ip multicast-routing", "ipv6 multicast-routing", "ip pim", "ip igmp", "router bgp", "address family ipv4 mvpn", "mdt default"]

check_features["VRF"] = ["ip vrf", "vrf definition"]

check_features["VRF_INTERFACE"] = ["vrf forwarding"]

#print(check_features)

# input config from the customer - change this to a text file
customer_input = "router bgp mdt default switching tme team rocks ! interface TenGigabitEthernet1/0/1 vrf forwarding Mgmt-vrf no ip address shutdown negotiation auto ! interface TenGigabitEthernet1/0/2  ! interface TenGigabitEthernet1/0/3 "

#print(check_features)

features_in_customer_input = {}
features_in_customer_input["MULTICAST"] = []
features_in_customer_input["VRF_INTERFACE"] = []

### for features not tied to an interface
for feature in check_features["MULTICAST"]:
    if(feature in customer_input):
        features_in_customer_input["MULTICAST"].append(feature)
        

#print("Features in customer_input['Multicast']")
#print(features_in_customer_input)



### for features that are tied to an interface
# if matches 
# starting point: "InterfaceGig" or "InterfaceTen" ... (such as Gig, Ten, Tw, Hun, etc) -- what are all the int names we want to look for?
# ending point: "!"
# look for the feature
for feature in check_features["VRF_INTERFACE"]:
    
    #print(feature)
    
    
    # iterate through a loop 
    # define start and end point for one interface
    interface = customer_input.split("! interface") # everything after the first occourance of ' interface" for example: TenGigabitEthernet1/0/1 Mgmt-vrf no ip address shutdown negotiation auto ! interface TenGigabitEthernet1/0/2 vrf forwarding ! interface TenGigabitEthernet1/0/3 

    #end = start[1].split("!") # everything between the start and the next '!' for example:  [ 'TenGigabitEthernet1/0/1 Mgmt-vrf no ip address shutdown negotiation auto', ' interface TenGigabitEthernet1/0/2 vrf forwarding ! interface TenGigabitEthernet1/0/3'] 

    for i in interface:
    	if i != 0: # don't check stuff in the 0th place of the list because it's the config before the first interface for example: router bgp mdt default 
        #split_feature = end[0] #  TenGigabitEthernet1/0/1 Mgmt-vrf no ip address shutdown negotiation auto 
            if feature in i: # only check the substring of customer_input
               features_in_customer_input["VRF_INTERFACE"].append(feature)

        
print("Features in customer_input")
print(features_in_customer_input)
    
