## To create a new iptable rule :

This will create a new custom chain apart from the pre-defined chains(INPUT, FORWARD and OUTPUT) with the name <chain_name>.

     iptables -t filter -N <chain_name>
     
To append the new chain to the INPUT chain, use following command:

     iptables -t filter -A INPUT -j <chain_name>
     
To append a new rule in the new chain that blocks the tcp packets on port `x` and `y` from all hosts except `host_ip` :
     
     iptables -t filter -A <chain_name> -p tcp --match multiport --dport x,y ! -s host_ip -j REJECT
     
Notice above:
* -A : It append the chain rule to the chain mention after it. use `man iptables` command to read more about it.
* -p : It is for the protocol which needs to be affected. Again read the man page.
* --match : It defines that there will be a match ahead. For our case it declares that there will be multiple ports. Read `man iptables-extensions`.
* ! : It is an important flag. It negates the meaning of the option that follows it. In our case it means 'for all source ip-addresses except host_ip REJECT'.
* -j : It stands for jumping to the chain mentioned after it.

Some default actions are ACCEPT, DROP and REJECT.
