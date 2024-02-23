check_allfeatures_required = {}
check_allfeatures_required["MULTICAST"] = ["ip multicast-routing", "ipv6 multicast-routing", "ip pim"]
check_allfeatures_required["TEST"] = ["Testfeature1", "Testfeature2", "Testfeature3"]

features_in_customer_input = {}

customer_input = "ip vrf vrf forwarding ipv6 multicast-routing service policy-map router bgp default vrf definition ip vrf ip multicast-routing Testfeature1 Testfeature2 Testfeature3"


# Step 2: Iterate through features and check for matches
for feature in check_allfeatures_required:
  compare = []
  for items in check_allfeatures_required[feature]:
    
    if (items in customer_input):
      compare.append(True)
    else:
       compare.append(False)

  if (all(compare)):
    #print("hello")
    features_in_customer_input[feature] = check_allfeatures_required[feature]
   
print(features_in_customer_input)
