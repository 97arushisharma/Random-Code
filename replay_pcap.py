#!/usr/bin/env python

import sys
import os

ROOT_DIR = os.path.dirname(__file__)
MODULES_DIR = os.path.join(ROOT_DIR, "modules")
sys.path.append(MODULES_DIR)

import socket
import dpkt
import array
from optparse import OptionParser

START_PACKET = 1
END_PACKET = -1     #-1 to replay all packets

USE_SINGLE_PORT  = False
UDP_IP = "127.0.0.1"
UDP_PORT = 0
PCAP_FILE = ""
CONFIG_DICT = {}
USE_CONFIG_DICT = False

def startReplay():
    if USE_CONFIG_DICT:
        print("UDP target IP: To be read from config file")
        print("UDP target port: To be read from config file")
    else:
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)

    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    with open(PCAP_FILE, "rb") as pcap_fh:
        pcapReader = dpkt.pcap.Reader(pcap_fh)

        count = 0
        for ts, data in pcapReader:
            count += 1
            if count < START_PACKET:
                # Wait till StartPacket is reached
                continue

            if END_PACKET != -1 and count > END_PACKET:
                # Exit if EndPacket is reached
                break

            print("Sending packet of "+ str(count) +" timestamp "+ str(ts))
            #sys.stdout.write("\rSending %d packet with timestamp %s" % (count, ts))
            ether = dpkt.ethernet.Ethernet(data)
            #print(ether)
            #if ether.type != dpkt.ethernet.ETH_TYPE_IP:
            #    continue
            ip = ether.data
            udp = ip.data

            #result = [i for i in (map(ord,udp.data))]
            #print(result)
            #byte_array = array.array('B',ip.data)
            byte_array = udp.data
            print(byte_array)

            if USE_SINGLE_PORT:
                sock.sendto(byte_array, (UDP_IP, UDP_PORT))
            elif USE_CONFIG_DICT:
                sip = socket.inet_ntoa(ip.src)
                for dest_ip_port in CONFIG_DICT.get(sip, []):
                    sock.sendto(byte_array, dest_ip_port)
            else:
                sock.sendto(byte_array, (UDP_IP, udp.dport))
            
    print("\n\nPacket replay complete!!")

def parseConfig(filename):
    config_dict = {}
    with open(filename, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            #140.222.132.166: 127.0.0.1/10001 127.0.0.1/20001 127.0.0.1/30001
            source_ip, destinations = line.split(":")
            config_dict[source_ip] = []
            for dest in destinations.split(" "):
                dest = dest.strip()
                if not dest:
                    continue
                ip, port = dest.split("/")
                config_dict[source_ip].append((ip, int(port)))
    return config_dict


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="file", help="pcap file to replay (Mandatory)")
    parser.add_option("-p", "--port", dest="port", type="int", help="Collector Port to export data (Default: Use Dest ports from pcap file)")
    parser.add_option("-c", "--collector", dest="host", default="127.0.0.1", help="Collector Host IP (Default: 127.0.0.1)")
    parser.add_option("-s", "--start", dest="start", type="int", default=1, help="Start replaying from this packet (Default: 1)")
    parser.add_option("-e", "--end", dest="end", type="int", default=-1, help="Last packet to replay (Default: -1 to replay all)")
    parser.add_option("-r", "--config", dest="config", help="Samplicator config")
    (options, args) = parser.parse_args()

    if not options.file:
        sys.stderr.write("-f/--file is mandatory argument\n")
        parser.print_help()
        sys.exit()

    if options.start <= 0:
        sys.stderr.write("-s/--start should be a positive integer\n")
        parser.print_help()
        sys.exit()

    if options.end <= 0 and options.end != -1:
        sys.stderr.write("-e/--end should be a positive integer or -1\n")
        parser.print_help()
        sys.exit()

    if options.end != -1 and options.end < options.start:
        sys.stderr.write("-e/--end should be greater than start\n")
        parser.print_help()
        sys.exit()

    if options.port and options.config:
        sys.stderr.write("--port and --config are mutually exclusive\n")
        parser.print_help()
        sys.exit()

    if not options.port:
        USE_SINGLE_PORT = False
    else:
        USE_SINGLE_PORT = True

    if options.config:
        USE_CONFIG_DICT = True
        CONFIG_DICT = parseConfig(options.config)

    PCAP_FILE = options.file
    UDP_IP = options.host
    UDP_PORT = options.port
    START_PACKET = options.start
    END_PACKET = options.end

    startReplay()
