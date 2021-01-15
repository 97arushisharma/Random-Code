# Random-Code
This repo contains random code snippets that might be useful for a developer.

* [getHostname.java](https://github.com/97arushisharma/Random-Code/blob/master/getHostname.java) - It is a code snippet that extracts hostname from a url which can be malformed.
* [getHostname.scala](https://github.com/97arushisharma/Random-Code/blob/master/getHostname.scala) - It is a code snippet that extracts hostname from a url which can be malformed but this time in scala.
* [iptable_rules](https://github.com/97arushisharma/Random-Code/tree/master/iptable_rules) - It contains the steps to create a new iptable rule that accepts the tcp packets only from some particular ip-addresses and over some specific ports. It also contains the steps to verify that the rules are working.
* [Build_structure](https://github.com/97arushisharma/Random-Code/tree/master/Build_structure) - It contains the CMake files and build script to automate the building(creating RPMs) of a project.
* [Encoding.java](https://github.com/97arushisharma/Random-Code/tree/master/Encoding.java) - See the following link [Java Strings](https://javarevisited.blogspot.com/2013/07/java-string-tutorial-and-examples-beginners-programming.html)
* [Calendar.cpp](https://github.com/97arushisharma/Random-Code/blob/master/Calendar.cpp) - A basic day finder by entering the date in C++. It can be any day of any year.
* [replay_pcap.py](https://github.com/97arushisharma/Random-Code/blob/master/replay_pcap.py) - This script is used to send packet data from the pcap filr to the give destination collector host and port. The command to run the given script is:

>     python replay_pcap.py -f <pcap_file_path> -p <destination_port> -c <destination_host_ip>



## Some Useful Commands:

### Networking

1.) *Nmap*: Nmap(Network Mapper) is used to discover hosts and services on a computer network by sending packets and analyzing the responses. To see if a particular host:port is reachable from local host use the following command:
 
 >     nmap -p <port> <remote-host>
  
2.) *Ncat*: Think of it as a free and easy companion tool to use which specializes in the analysis of network packets. It is a utility program supports a wide range of commands to manage networks and monitor the flow of traffic data between systems. Look [here](https://www.varonis.com/blog/netcat-commands/).

 >     nc -u <ip-address> <port>
 
 On the above mentioned ip address listen on the port using below command

 >     nc -l <port>

NOTE: `-u` is used for udp data. Incase the data is tcp remove that flag.

3.) *Telnet*:

### Memory and CPU utilisation

1.) *Top*: Use the following command to view the output of top cammand at fixed time interval:

>     top -d 1.0 -b | grep Cpu
>     top -d 1.0 -b | grep Mem

Refer [this](https://www.geeksforgeeks.org/top-command-in-linux-with-examples/) for details of `top` command.

To see the CPU utilisation of a system you can also use the following command:

>     cpu utlization: diff=$((60 - $(date '+%s') % 60)); sleep $diff; dstat -t -c -l -m -d -n 60

Here `60` is the number of seconds to elapse between two consecutive readings.

To record the CPU and Memory utilisation of a docker container use the following command:

>     while ((1)); do o=$(docker stats --no-stream --format='{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}' <containerID>); \
>     t=$(date '+%F %T'); echo "$t $o"; done

Here `<containerID>` is the container ID fetched using the `docker ps` command.

### Kafka Commands

To list topics:
>     bin/kafka-topics.sh --list --zookeeper localhost:2181

To get topic offset for each partition:
>     bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list <broker-ip>:<broker-port> --topic Topic --time -1

To get total messages for a topic:
>     while true; do bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list <broker-ip>:<broker-port> --topic Topic --time -1 | awk -F ":" '{sum += $3} END {print sum}'; done
 
To get the broker-port see the Kafka broker.conf

To delete a topic:
>     bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic Topic

To create a topic:
>     bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 6 --topic Topic
