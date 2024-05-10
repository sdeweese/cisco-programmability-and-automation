# features we're interested (these might or might not be in the customer config)
check_features = {}
check_features["MULTICAST"] = ["ip multicast-routing", "ipv6 multicast-routing", "ip pim", "ip igmp", "router bgp", "address family ipv4 mvpn", "mdt default"]
check_features["VRF"] = ["ip vrf", "vrf definition"]


check_features_configured_on_an_interface = {}
check_features_configured_on_an_interface["VRF"] = ["vrf forwarding"]
check_features_configured_on_an_interface["QOS"] = ["service policy-map"]

# input config from the customer - TODO: change this to a text file
customer_input = "ip vrf vrf forwarding service policy-map router bgp mdt default vrf definition ip vrf switching tme team rocks vrf forwarding ! interface TenGigabitEthernet1/0/1  Mgmt-vrf no ip address shutdown negotiation auto vrf forwarding service policy-map ! interface TenGigabitEthernet1/0/2  ! interface TenGigabitEthernet1/0/3 test123 hey ama x story was here ! bgp blahh vrf forwarding service policy-map my-policy story was here"


features_in_customer_input = {}


### for features not tied to an interface
for feature in check_features:
    #print(feature)
    for i in check_features[feature]:
        #print(i)
        key = feature
        #print(key)
        if(key not in features_in_customer_input): 
            features_in_customer_input[key] = [] # we don't want to reset the list to empty each time we loop through a feature, which happened when we didn't adde the if statment above
        if(i in customer_input):
            features_in_customer_input[feature].append(i)
        

### for features that are configured on an interface
for feature in check_features_configured_on_an_interface:
    #print(feature)
    for i in check_features_configured_on_an_interface[feature]:
        interface = customer_input.split("! interface") # everything after the first occourance    
        last_interface_with_all_following_config = interface[(len(interface) - 1)]
        last_interface_with_all_following_config_as_a_list = last_interface_with_all_following_config.split("!")
        last_interface = last_interface_with_all_following_config_as_a_list[0] # we only want the first item in the list because everything after that is config outside of an interface
    
        for config in interface:            
    	    if config != interface[0]: # note: no need to check config in the 0th place of the list because it's the config before the first interface for example: router bgp mdt default                 
                
                key = feature+"_ON_INTERFACE"
                if(key not in features_in_customer_input): 
                    features_in_customer_input[key] = [] # we don't want to reset the list to empty each time we loop through a feature, which happened when we didn't adde the if statment above
                if(last_interface in config): # we do something a little different for the last element in the list because it contains the last interface config and all the customer config after that
                    if(i in last_interface): 
                        features_in_customer_input[key].append(i)
        
                elif i in config: # only check the substring of customer_input for interface
                   features_in_customer_input[key].append(i)
                       
print("Features in customer_input")
print(features_in_customer_input)
    
