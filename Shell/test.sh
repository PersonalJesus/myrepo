================
cloud@clone:~/test$ cat s2.sh
#!/bin/bash
# $1 ip         $2 hostname

#ip template: astra-root-100
#IP=10.210.0.246

# ip template - astrar-root-20
IP=10.210.0.245

# change-hostname
ssh -t cloud@$IP sudo -- "sh -c 'sed -i 's/astra-template-v1/$2/g' /etc/hostname'"

# cnange hosts file
ssh -t cloud@$IP sudo -- "sh -c 'sed -i 's/astra-template-v1/$2/g' /etc/hosts'"

# change-ip
ssh -t cloud@$IP sudo -- "sh -c 'sed -i 's/$IP/$1/g' /etc/network/interfaces'"
# + gateway
ssh -t cloud@$IP sudo -- "sh -c 'sed -i 's/10.210.0.1/10.210.8.1/g' /etc/network/interfaces'"

#mask
ssh -t cloud@$IP sudo -- "sh -c 'sed -i 's/255.255.254.0/255.255.255.240/g' /etc/network/interfaces'"

# change machine-id
ssh -t cloud@$IP sudo -- "sh -c 'rm /etc/machine-id && dbus-uuidgen --ensure=/etc/machine-id && rm /var/lib/dbus/machine-id && dbus-uuidgen'"

# reboot
ssh -t cloud@$IP sudo -- "sh -c 'reboot'"