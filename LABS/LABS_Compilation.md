## 2.4 First interaction with Snort 
Q. Run the Snort instance and check the build number.
A. 149
(View where I found the answer: Screenshots/Network Security and Traffic Analysis/02/2.4/Screenshot 2025-07-16 at 6.08.38 PM.png)

Q. Test the current instance with "/etc/snort/snort.conf" file and check how many rules are loaded with the current build.
A. 4151

(View where I found the answer: 
After executing "sudo snort -c /etc/snort/snort.conf -T" 
Scroll down to find the answer. 
Screenshots/Network Security and Traffic Analysis/02/2.4/Screenshot 2025-07-16 at 6.15.45 PM.png) 


Q. Test the current instance with "/etc/snort/snortv2.conf" file and check how many rules are loaded with the current build. 
A. 1

(View where I found the answer: 
After executing "sudo snort -c /etc/snort/snortv2.conf -T" 
Scroll down to find the answer.  
Screenshots/Network Security and Traffic Analysis/02/2.4/Screenshot 2025-07-16 at 6.18.59 PM.png) 



## 2.6 Operation Mode 2: Packet Logger 
: Investigate the traffic with the default configuration file with ASCII mode.  
Execute the traffic generator script and choose "TASK-6 Exercise". 
Wait until the traffic ends, then stop the Snort instance. 
Now analyse the output summary and answer the question. Now, you should have the logs in the current directory. Navigate to folder "145.254.160.237".

Q1. What is the source port used to connect port 53?
A1. 3009 

* Here is what I did: 
1. Ran "~/Desktop/Task-Exercises$ sudo snort -dev -K ASCII -l. "
(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 1.33.04 PM.png)

2. Minimized the tab, and at the same time, execute the traffic generator script and choose "TASK-6 Exercise".  
(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 1.48.16 PM.png)

3. Waited until the traffic ended, then went back to the first terminal (that I minimized) and pressed control + C.

(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 1.50.56 PM.png)

4. I navigated to folder "145.254.160.237". However, I couldn't acccess the file due to the permission issue. 

(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 1.54.04 PM.png)

Therefore, I had to change the permission

5. I ran "~/Desktop/Task-Exercises$ sudo chmod 777 145.254.160.237 " first, then ran "cd 145.254.160.237"

*Note: 777 gives read + write + execute permissions to everyone (owner, group, others).
However,.. this command is risky because it gives  everyone full access, making the file vulnerable to misuse, hacking, or accidental damage. I could use it because it was a virtual machine.  


(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.02.21 PM.png)

6. I could see that the source port used to connect port 53 was 3009. 



Q2. Use snort.log.1640048004
Read the snort.log file with Snort; what is the IP ID of the 10th packet? 
A2. 

* Here is what I did: 
1. Navigated to TASK-6 in terminal and ran "sudo snort -r snort.log.1640048004 -n 10"

(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.14.03 PM.png)


2. Scrolled down and found the last packet's (10th packet) IP ID. 

(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.15.07 PM.png)



Q3. Read the "snort.log.1640048004" file with Snort; what is the referer of the 4th packet?
A3. http://www.ethereal.com/development.html

* Here is what I did: 
1. Navigated to TASK-6 in terminal and ran "sudo snort -r snort.log.1640048004 -n 4 -X". I added -X to the command to view the full packet details. 

(View Image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.31.31 PM.png)

2. Then Scrolled down to find the fourth (the last) packet information and its referer. 

(View: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.34.02 PM.png)
  

Q4. Read the "snort.log.1640048004" file with Snort; what is the Ack number of the 8th packet? 
A4. 
A4. 0x38AFFFF3 

* Here is what I did: 
1. Navigated to ../TASK-6 and ran "sudo snort -r snort.log.1640048004 -n 8 -v". 

Note: I added -v to display the packer headers (TCP/IP) in the console. I knew that ACK number (Acknowledgment Number) is a field in the TCP header that tells the sender that it successfully received all data up to this number.

2. Went to the last (8th) packet's details and checked Ack number. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.45.40 PM.png)


Q5. Read the "snort.log.1640048004" file with Snort; what is the number of the "TCP port 80" packets? 
A. 

* Here is how I did: 
1. Navigated to TASK-6 in terminal and ran "sudo snort -r snort.log.1640048004 'tcp and port 80'" 

Note: 'tcp and port 80' -> This is a Berkeley Packet Filter (BPF) expression. It filters for TCP packets that are either source or destination port 80. 


2. Then I found that the total number of the "TCP port 80 packets" is 41. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.6/Screenshot 2025-07-20 at 2.49.50 PM.png)



# From this lab, I learned.. 
1. How to run Snort in logger mode and use its options using parameters. 
I learned Snort can log packets using -l to set the log folder, and -K ASCII to save logs in an easy-to-read text format. It’s cool that I can choose between binary and ASCII logs depending on what I need.

2. The importance of root permissions and file ownership
I faced permission issues when accessing log folders, so I had to use commands like chmod and chown. This made me realize how important Linux file permissions are when working with network tools like Snort.

3. Logs can be analyzed with other tools like tcpdump and Wireshark. 
Snort’s binary logs can be opened with tcpdump or Wireshark, which gives me more flexibility for analysis.
Using Berkeley Packet Filters (BPF) to filter packets
I found it useful that I can filter logs by protocol or port using BPF expressions, like showing only TCP packets on port 80. It helps focus on what matters.  



## 2.7 Operation mode 3: IDS and IPS
Investigate the traffic with the default configuration file.
Execute the traffic generator script and choose "TASK-7 Exercise". Wait until the traffic stops, then stop the Snort instance. Now analyse the output summary and answer the question.
 

Q1. What is the number of the detected HTTP GET methods? 
A1. I first 

* Here is what I did: 
1. I first ran this command "sudo snort -c /etc/snort/snort.conf -A full -l ." in a terminal at ~/Desktop/Task-Exercises/Exercise-Files and minimized it. 

2. I opened a new terminal and ran the traffic generator script than clicked “TASK-7 Exercise.”
(View image: Screenshots/Network Security and Traffic Analysis/02/2.7/Screenshot 2025-07-20 at 4.15.12 PM.png)

3. I went back to the first terminal that I minimized and pressed control + c. 

4. Then scrolled down to find the number of HTTP GET methods. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.7/Screenshot 2025-07-20 at 4.20.44 PM.png)

During this lab, I made sure to start sniffing before the attack and terminate right after the attack. 



# From this lab, I learned..  

1. How to run Snort in IDS/IPS mode and test configurations.
I learned that I can start Snort in IDS/IPS mode using -c to specify the config file and -T to test it. The test helps catch syntax or path issues before launching Snort, which saves time and avoids confusion later.
2. Different alert output modes and their use cases.
Snort can show alerts in several ways using -A. I used console to see alerts directly in the terminal, and cmg to get detailed packet data in hex and ASCII. Modes like fast and full write logs to files instead, which is useful for large captures.
3. How Snort behaves in background or no-logging mode.
Using -D, I can run Snort in the background, which is useful for automation or longer tasks. With -N, Snort won’t write log files, but it still shows traffic on the screen if other flags like -v or -X are used. It’s important to know the effect of each mode on visibility and log storage.
4. Snort can run without a full config file.
I was surprised that I could run Snort with just a rule file instead of the full config. This is handy when testing new or custom rules without loading unnecessary modules.
5. Snort can be used as an IPS with -Q and DAQ modules. 
When I added -Q --daq afpacket -i eth0:eth1, Snort switched to IPS mode and dropped packets. It made me realize Snort can actively protect a system, not just detect threats.



## 2.8 Operation Mode 4: PCAP Investigation 
Use the attached VM and navigate to the Task-Exercises/Exercise-Files/TASK-8 folder to answer the questions. 

Q1. Investigate the mx-1.pcap file with the default configuration file. What is the number of the generated alerts?
A1. 170 

* Here is what I did: 
1. I navigated to Task-Exercises/Exercise-Files/TASK-8 and ran this command: 
sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-1.pcap
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.03.44 PM.png)

2. Then scrolled down to find the number of the generated alerts. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.05.31 PM.png)


Q2. Keep reading the output. How many TCP Segments are Queued? 
A2. 18

Starting from Q1 terminal, I scrolled a little further down to check the number of TCP Segments Queued.
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.09.07 PM.png)


Q3. Keep reading the output.How many "HTTP response headers" were extracted? 
A3. 3

Starting from Q2 terminal, I scrolled a little further down to check the number of HTTP response headers extracted. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.11.26 PM.png)


Q4. Investigate the mx-1.pcap file with the second configuration file.
What is the number of the generated alerts?
A4. 68

* Here is what I did: 
1. I navigated to Task-Exercises/Exercise-Files/TASK-8 and ran this command: 
"sudo snort -c /etc/snort/snortv2.conf -A full -l . -r mx-1.pcap"
2. Then I scrolled down to find the number of the generated alerts. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.19.09 PM.png)



Q5. Investigate the mx-2.pcap file with the default configuration file.
What is the number of the generated alerts?
A. 340 

* Here is what I did: 
1. I navigated to Task-Exercises/Exercise-Files/TASK-8 and ran this command: 
"sudo snort -c /etc/snort/snort.conf -A full -l . -r mx-2.pcap"
2. Then I scrolled down to find the number of the generated alerts. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.22.09 PM.png)


Q6. Keep reading the output. What is the number of the detected TCP packets?
A6. 82

Starting from Q5 terminal, I scrolled a little further down to check the number of the detected TCP packets.
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.25.09 PM.png)


Q7. Investigate the mx-2.pcap and mx-3.pcap files with the default configuration file.
What is the number of the generated alerts?
A7. 1020

* Here is what I did: 
1. I navigated to Task-Exercises/Exercise-Files/TASK-8 and ran this command: 
"sudo snort -c /etc/snort/snort.conf -A full -l . --pcap-list="mx-2.pcap mx-3.pcap""
2. Then I scrolled down to find the number of the generated alerts. 
(View image: Screenshots/Network Security and Traffic Analysis/02/2.8/Screenshot 2025-07-20 at 5.30.26 PM.png)


## From this lab, I learned..   
1. How to run Snort in PCAP investigation mode using different parameters.
Now I know how to analyze both single and multiple .pcap files with Snort using -r, --pcap-list, and --pcap-show. 
These options help in managing large traffic captures and associating alerts with the correct files.
2. Snort leverages rule-based detection even in offline PCAP analysis
Snort still applies the ruleset to offline traffic in PCAP mode, allowing me to identify malicious or suspicious patterns without live capture. This helps speed up forensic investigations.
3. Reading logs beyond alerts gives deeper insights. 
Looking past the alerts, I found useful details like the number of TCP segments queued and HTTP response headers. These metrics help build context around the alert behavior.