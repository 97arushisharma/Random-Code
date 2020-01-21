#!/usr/bin/python3

import sys
import os
import xml.etree.ElementTree as ET
import subprocess


# Function to delete the entire chain.
def delete_chain(chain_name):
    iptable_rules = []
    iptable_rules = (subprocess.check_output("iptables -S | grep "+chain_name+" | cut -f2- -d ' ' | awk 'NR!=1{print}'",shell=True)).strip().split("\n")

    for rules in iptable_rules:
    if(rules == " " or rules == ""):
        continue
    print("WARNING: Deleting Rule: "+rules)
    try:
        os.system("iptables -D "+rules)
    except:
        print("ERROR: Cannot delete rule "+rules)
        print("Exiting...")
        sys.exit()

    if(chain_name == None or chain_name == "" or chain_name == " "):
    return
    os.system("iptables -X "+chain_name)
    
    # Function to delete the entire chain.
def delete_chain2(chain_name):
    if(chain_name == None or chain_name == "" or chain_name == " "):
        return
    try:
    os.system("iptables -t filter -F "+chain_name)
    os.system("iptables -t filter -D INPUT -j "+chain_name)
    os.syetem("iptables -t filter -X "+chain_name)
    except:
    print("ERROR: Could not delete the chain. Kindly verify.")


# Function to add rules for given ips and ports.
def add_rule(chain_name,ip_string,port_string):
    try:
    ip_list = ip_string.strip().split(",")
    for ip in ip_list:
        if(ip == "" or ip == " "):
        continue
        os.system("iptables -t filter -A {} -p tcp --match multiport --dport {} -s {} -j ACCEPT".format(chain_name,port_string,ip.strip()))
        print("INFO: iptable rule added for ip: "+ip.strip())
    os.system("iptables -t filter -A {} -p tcp --match multiport --dport {} -j REJECT".format(chain_name,port_string))
    except:
    print("ERROR: Error while adding the rule.")
    print("Exiting...")
    sys.exit()

# Main function
if __name__ == "__main__":

    try:
    tree = ET.parse('config.xml')
    root = tree.getroot()
    except:
    print("ERROR: Error while parsing the config file. \n")
        sys.exit()


    chain_name = root.find('chain').text

    if(chain_name == None or chain_name == "" or chain_name == " "):
    print("ERROR: No chain name given in the config file.")
    sys.exit()

    delete_chain2(chain_name)

    # Create the new chain once.
    try:
    os.system("iptables -t filter -N "+chain_name)
        os.system("iptables -t filter -A INPUT -j "+chain_name)
    except:
    print("ERROR: Error while adding the chain.")
    print("Exiting...")
        sys.exit()


    # Find the ips and ports of the host that need to be allowed access.
    for rule in root.findall('rule'):
    ips = rule.find('ips').text
    ports = rule.find('ports').text
    if(ips == "" or ips == " " or ips == None):
        print("INFO: There is an empty IP in config. Skipping...")
        continue
    add_rule(chain_name,ips,ports)
