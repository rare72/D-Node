#!/bin/bash
#
# This script idempotently sets the vm.swappiness value to 15.
# It checks if the setting already exists in /etc/sysctl.conf.
# If it does, it updates the value. If not, it adds the setting.
# Finally, it applies the setting immediately.

# Define the target swappiness setting
SWAPPINESS_SETTING="vm.swappiness = 15"
SYSCTL_FILE="/etc/sysctl.conf"

# Check if the swappiness setting already exists
if grep -q "^vm\.swappiness" "$SYSCTL_FILE"; then
    # If it exists, update it
    sed -i "s/^vm\.swappiness.*/$SWAPPINESS_SETTING/" "$SYSCTL_FILE"
    echo "Updated vm.swappiness in $SYSCTL_FILE"
else
    # If it does not exist, add it
    echo "$SWAPPINESS_SETTING" >> "$SYSCTL_FILE"
    echo "Added vm.swappiness to $SYSCTL_FILE"
fi

# Apply the sysctl settings immediately
sysctl -p
echo "Applied sysctl settings."