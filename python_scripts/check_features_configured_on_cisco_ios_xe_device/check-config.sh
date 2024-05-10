#!/bin/bash

# Author: Story DeWeese (sdeweese)
# Date: November 2022


# Script checks if a string exists in a given config file
# Use:
#   1. Create a folder and add this script and a config file
#   2. Run the following command to ensure you can run the script `chmod 755 check-config.sh`
#   3. Run the following command to check if any features are in the config file

# inputs:
#   file:       Name of file containing config (this file must be in the same folder as this script when running the script)
#   features:   List of features to check for in config file
# TODO: add input file to check certain configs - don't hard code check_features variable
# outputs:
#   yes:        Feature in File
#   no:         Feature not in File
# TODO: add license & version in outputs
#		Include different inputs based on platform C9K, C6K, etc

# TODO: Phase 1: is the feature enabled?
# 	Phase 2: how is the feature used?
#		 for future versions of this script:
# 		 	- see if a feature has been applied to an interface
#			- which grouped configs are needed to ensure a feature is fully enabled / used


declare -A check_features

check_features[0,0]="PNP"
check_features[0,1]="pnp profile"

check_features[1,0]="L3 ROUTING"
check_features[1,1]="ip routing"
check_features[1,2]="ip unicast-routing"
check_features[1,3]="ipv6 unicast-routing"
check_features[1,4]="router ospf"
check_features[1,5]="router eigrp"
check_features[1,6]="router isis"
check_features[1,7]="router bgp"

check_features[2,0]="MULTICAST"
check_features[2,1]="ip multicast-routing"
check_features[2,2]="ipv6 multicast-routing"
check_features[2,3]="ip pim"
check_features[2,4]="ip igmp"
check_features[2,5]="router bgp"
check_features[2,6]="address family ipv4 mvpn"
check_features[2,7]="mdt default"

check_features[3,0]="NETWORK SEGMENTATION"
check_features[3,1]="vrf definition"
check_features[3,2]="ip vrf"

check_features[4,0]="HIGH AVAILABILITY"
# parse for four tuple interface numbering a/b/c/d - for SVL switch num (a) + interface (b/c/d)
# check_features[4,1]="redundancy" # redundancy is enabled by default
#check_features[4,2]="mode sso" # enabled by default ??
check_features[4,3]="provision" #switch <num> provision ------------------------ add placeholder ------------------------
check_features[4,4]="stackwise-virtual" # if this config exists, stackwise-virtual is configured

check_features[5,0]="MACSEC"
check_features[5,1]="mka policy"
check_features[5,2]="macsec-cipher-suite"
check_features[5,3]="macsec"
check_features[5,4]="macsec network-link"

check_features[6,0]="PTP"
check_features[6,1]="ptp mode"
check_features[6,2]="ptp profile"
check_features[6,3]="ptp enable"
check_features[6,4]="ptp transport"

check_features[7,0]="AVB"
check_features[7,1]="avb"
check_features[7,2]="avb vlan"
check_features[7,3]="ptp profile dot1as"

check_features[8,0]="FLEXIBLE NETFLOW" # Note: there are syntax differences for C9K vs C6K
# Define what you're looking for FNF
# Collect data
# Send / export data
check_features[8,1]="mls flow"
check_features[8,2]="flow record"
check_features[8,3]="flow exporter"
check_features[8,4]="flow monitor"
check_features[8,5]="ip flow monitor"
check_features[8,6]="mls netflow interface"

check_features[9,0]="EEM"
check_features[9,1]="event manager"
check_features[9,2]="event syslog pattern"
check_features[9,3]="cli command" # full config: action <num> cli command

check_features[10,0]="PROGRAMMABILITY"
check_features[10,1]="netconf-yang"
check_features[10,2]="restconf"
check_features[10,3]="gnmi"
check_features[10,4]="gnxi"

check_features[11,0]="BONJOUR"
check_features[11,1]="mdns-sd gateway"
check_features[11,2]="mdns-sd service-list"
check_features[11,3]="mdns-sd service-policy"
check_features[11,4]="service-export mdns-sd controller"

check_features[12,0]="FABRIC SDA / EVPN"
check_features[12,2]="address-family l2vpn evpn"
check_features[12,3]="router lisp" # SDA
check_features[12,4]="service ipv4"
check_features[12,5]="service ethernet"
check_features[12,6]="instance-id"
#check_features[12,7]="insterface nve1"
check_features[12,8]="l2vpn evpn" # EVPN
check_features[12,9]="l2vpn evpn instance" #EVPN
#check_features[12,2]="address-family ipv4" ------------------ is this needed ----------------

check_features[13,0]="ACV / EP ANALYTICS"
check_features[13,1]="flow record"
#check_features[13,2]="interface"
check_features[13,3]="ip nbar protocol-discovery"
check_features[13,4]="match application name"

check_features[14,0]="QOS / APP POLICY" # if policy-map, there should be a class-map as well
#check_features[14,1]="class" # matches with too many things..
# For QOS, these are default configs, so they'll match every time
#check_features[14,2]="class-map" # default config
check_features[14,3]="match protocol"
#check_features[14,4]="policy-map" # look for policy name, so we can ignore default
check_features[14,5]="class-map match-any"

check_features[15,0]="IPSEC"
check_features[15,1]="crypto ikev2"
check_features[15,2]="crypto ipsec"
check_features[15,3]="tunnel mode ipsec"
check_features[15,4]="tunnel protoection ipsec"

check_features[16,0]="ERSPAN"
check_features[16,1]="erspan-id"
#check_features[16,2]="monitor session" # DO WE NEED THIS ONE?
check_features[16,3]="type erspan-destination" # full config: monitor session <num> type erspan-destination
check_features[16,4]="type erspan-source" # full config: monitor session <num> type erspan-source

check_features[17,0]="APPLICATION HOSTING"
check_features[17,1]="app-hosting appid"
check_features[17,2]="app-vnic AppGigabitEthernet"
check_features[17,3]="iox"

check_features[18,0]="ENCRYPTED TRAFFIC"
check_features[18,1]="et-analytics"
check_features[18,2]="et-analytics enable"

check_features[19,0]="THOUSANDEYES"
check_features[19,1]="ck_features[21,1]="primary" # full config: address <address> primary
check_features[21,2]="secondary" # full config: address <address> secondaryrun-opts 1 \"-e TEAGENT_ACCOUNT_TOKEN=\""

check_features[20,0]="POE REDUNDANCY"
check_features[20,1]="perpetual-poe-ha"
check_features[20,2]="power inline port"
check_features[20,3]="power inline port poe-ha"

check_features[21,0]="HSRP / VRRP"
check_features[21,1]="primary" # full config: address <address> primary
check_features[21,2]="secondary" # full config: address <address> secondary
check_features[21,2]="preempt delay minimum"
check_features[21,3]="standby"
check_features[21,4]="vrrp"

check_features[22,0]="NAC / TRUST ANALYTICS"
check_features[22,1]="aaa authentication dot1x"
check_features[22,2]="authentication order dot1x mab"
check_features[22,3]="dot1x system-auth-control"
check_features[22,4]="radius server dot1x pae authenticator"


## Uncomment to see the length of check_features
#echo "${#check_features[@]}"

## Uncommnet to see all features that will be checked
#echo "${check_features[@]}"

## Uncomment the following nested for loops to
## see ALL items in the table
#for ((i=0;i<=22;i=i+1)) do
# for ((j=0;j<=10;j=j+1)) do
#  echo "a["$i","$j"]="${check_features[$i,$j]}
# done
#done

#echo
#echo "${check_features[@]}"
# if any / all configs associated with a feature are in config file, add FEATURE to output
features_included=('Features included in config: \n')
features_excluded=('Features NOT included in config: \n')

count=0
for feature in "${check_features[@]}"; do                   # iterate through all items in check_features
    #echo "${check_features[$count,0]}"
    #echo $count
    if grep -qF "$feature" "$1"; then                       # if a feature is in the config file,
        #echo "includes "$feature
  	#echo "${check_features[$count,0]}"
	# TODO: input parameters:
	#		config file
	#		customer name (to populate database)
	# TODO: add which feature is enabled AND which configs
	# TODO: From file name, mark which features & configs are used
	features_included+="${feature}"
	#features_included+="${check_features[$count,0]}" # return feature title
	features_included+='\n'   #   add the feature to the features_included array
    else                                                    # if a feature is NOT in the config file,
        #echo "not "$feature
  	#echo "${check_features[$feature,0]}"
        features_excluded+="${feature}"
        #features_excluded+="${check_features[$count,0]}" # return feature title
	features_excluded+='\n'   #   add the feature to the features_excluded array
    fi
    ((count++))
done

# Remove last comma from each string before printing
#while [ ${features_included: -1} = $'\n'] do
#	echo "${features_included: -1}"
	#features_included=${features_included:0:-1}
#done
#echo "TESTING"
#features_included="${features_included%"${features_included##*[![:space:]]}"}"
#echo "$features_included" | sed -n -e 'l'

features_included=${features_included:0:-1}
features_excluded=${features_excluded:0:-1}
#echo
echo -e ${features_included} # use -e flag to get '\n' read as a newline
#echo
#echo -e ${features_excluded}

#echo -n $(wc -l < $features_included)
#features_included=${features_included%$'\n'}   # Remove a trailing newline.
#echo -e ${features_included}

