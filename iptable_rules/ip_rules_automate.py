#!/usr/bin/python3

import sys
import os
import xml.etree.ElementTree as ET
import subprocess
import argparse


# Function to delete the entire chain.
def delete_chain(chain_name):
    if(chain_name == None or chain_name == "" or chain_name == " "):
        return
    try:
        os.system("iptables -t filter -F {}".format(chain_name))
        os.system("iptables -t filter -D INPUT -j {}".format(chain_name))
        os.system("iptables -t filter -X {}".format(chain_name))
    except:
        print("ERROR: Could not delete the chain. Kindly verify.")


# Function to add rules for given source and ports.
def add_rule(chain_name,ip_string,port_string):
    try:
        ip_list = ip_string.strip().split(",")
        for ip in ip_list:
            if(ip == "" or ip == " "):
                continue
            os.system("iptables -t filter -A {} -p tcp --match multiport --dport {} -s {} -j ACCEPT".format(chain_name,port_string,ip.strip()))
        os.system("iptables -t filter -A {} -p tcp --match multiport --dport {} -j REJECT".format(chain_name,port_string))
    except:
        print("ERROR: Error while adding the rule.")
        print("Exiting...")
        sys.exit()

# Main function
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Pass the configuration file', required=True)
    args = parser.parse_args()

    # Read config file from the system
    try:
        config_file = args.config
        tree = ET.parse(config_file)
        root = tree.getroot()
    except:
        print("ERROR: Error while parsing the config file. \n")
        sys.exit()

    chain_name = root.find('chain').text.strip()
    if(chain_name == None or chain_name == "" or chain_name == " "):
        print("ERROR: No chain name given in the config file.")
        sys.exit()
    
    # Take iptables backup before creating new rules
    os.system("/sbin/iptables-save > ./iptables-backup-`date +%FT%T`")

    delete_chain(chain_name)

    # Create the new chain once.
    try:
        os.system("iptables -t filter -N "+chain_name)
        os.system("iptables -t filter -A INPUT -j "+chain_name)
    except:
        print("ERROR: Error while adding the chain.")
        print("Exiting...")
        sys.exit()


    # Find the source and ports of the host that need to be allowed access.
    for rule in root.findall('rule'):
        source = rule.find('source').text
        ports = rule.find('ports').text
        if(source == "" or source == " " or source == None):
            print("INFO: There is an empty IP in config. Skipping...")
            continue
        add_rule(chain_name,source,ports)
