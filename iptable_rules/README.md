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

To verify that the rules have been created run the following command and search for the chain:

     iptables -L -v --line-numbers

To see the rules that have been applied with that particular chain run the following command:

     iptables -S | grep <chain_name>
     
## To delete a chain :

The below command deletes the chain from any referring chain. In our case the chain is removed from INPUT chain.

     iptables -D INPUT -j <chain_name>

Then, flush the entire chain i.e., delete all the rules from the chain.

     iptables -F <chain_name>

Finally, delete the chain.

     iptables -X <chain_name>


**Best Practices** - Inorder not to harm the system iptables configurations or to be able to restore them incase of some problem iptables allow us to save the iptable rules into a file using the iptables-save module:

     /sbin/iptables-save > /opt/miq/firewall/iptables-works-`date +%FT%T`

The file name format are as follows:

     /opt/miq/firewall/iptables-works-2020-01-21T06:45:09

If you do something that prevents your system from working properly, you can quickly restore it using the following command:

     /sbin/iptables-restore < /opt/miq/firewall/iptables-works-2020-01-21T06:45:09
     
To add the new rules keeping the current ones:

     sudo iptables-restore -n < /etc/sysconfig/iptables

