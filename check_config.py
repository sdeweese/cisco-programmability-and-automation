# features we're interested (these might or might not be in the customer config)
check_features = {}
check_features["MULTICAST"] = ["ip multicast-routing", "ipv6 multicast-routing", "ip pim", "ip igmp", "router bgp", "address family ipv4 mvpn", "mdt default"]
check_features["VRF"] = ["ip vrf", "vrf definition"]


check_features_configured_on_an_interface = {}
check_features_configured_on_an_interface["VRF"] = ["vrf forwarding"]

# input config from the customer - change this to a text file
customer_input = "router bgp mdt default switching tme team rocks vrf forwarding ! interface TenGigabitEthernet1/0/1 Mgmt-vrf no ip address shutdown negotiation auto ! interface TenGigabitEthernet1/0/2  ! interface TenGigabitEthernet1/0/3 hey ama vrf forwarding ! bgp blahh vrf forwarding "


features_in_customer_input = {}
features_in_customer_input["MULTICAST"] = []
features_in_customer_input["VRF_ON_INTERFACE"] = []

### for features not tied to an interface
### TODO: make more generic for all features (not requiring an interface) by looping through all features in check_features
for feature in check_features["MULTICAST"]:
    if(feature in customer_input):
        features_in_customer_input["MULTICAST"].append(feature)
        

### for features that are configured on an interface
### TODO: make more generic for all features (requiring an interface) by looping through all features in check_features_configured_on_an_interface
for feature in check_features_configured_on_an_interface["VRF"]:
    interface = customer_input.split("! interface") # everything after the first occourance 
    last_interface_with_all_following_config = interface[(len(interface) - 1)]
    last_interface_with_all_following_config_as_a_list = last_interface_with_all_following_config.split("!")
    last_interface = last_interface_with_all_following_config_as_a_list[0] # we only want the first item in the list because everything after that is config outside of an interface
    
    for i in interface:            
        #print(i)
    	if i != interface[0]: # note: no need to check config in the 0th place of the list because it's the config before the first interface for example: router bgp mdt default  
            if(last_interface in i): # we do something a little different for the last element in the list because it contains the last interface config and all the customer config after that
                if(feature in last_interface):
                    features_in_customer_input["VRF_ON_INTERFACE"].append(feature)
        
            elif feature in i: # only check the substring of customer_input for interface
               features_in_customer_input["VRF_ON_INTERFACE"].append(feature)
                       
print("Features in customer_input")
print(features_in_customer_input)
    
