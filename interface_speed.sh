#!/bin/bash

# Find active interface used
used_network=`ip link show | grep 'state UP' | awk 'NR<=1 {print $2}' |cut -d ":" -f 1`

# Find IP address
# Currently not used
#ip_addrs=`ip address show "$used_network" |grep 'inet ' |awk '{print $2}' |cut -d'/' -f1`

# Check speed of active interfaced
# The speed in 'Mb/s'
speed=`ethtool "$used_network" 2>&1 |grep Speed |awk '{print $2}' |sed 's#Mb/s##g'`

# Print the speed
echo "$speed"
