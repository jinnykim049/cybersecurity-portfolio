# From Section 2.1-2.2, I learned... 
1. Hash values help uniquely identify files and are crucial for malware tracking and detection. But relying solely on hash values is weak because attackers can easily alter them.

2. IP addresses can reveal attacker infrastructure, but they are unstable indicators since they are easily changed.

3. Fast Flux is a sophisticated evasion technique where malware communicates through constantly rotating IP addresses, making detection much harder.

4. Using platforms like Any.run and VirusTotal enhances the ability to detect and understand malware behavior in a real-world context. 


# From Section 2.3,  I learned.. 

1. Domain names are useful for both users and attackers. 
2. Malicious domains are often hidden using URL shorteners. 
3. Punycode attacks trick users into visiting fake websites. 
4. Any.run sandbox helps detect threats through multiple views
5. To detect malicious domains, proxy logs or web server logs can be used. 
6. Attackers usually hide the malicious domains under URL shorteners.


## From Section 2.4, I learned.. 
1. How to trace suspicious behavior from Microsoft Office applications (e.g., Word)

2. How attackers drop and execute malicious payloads through seemingly harmless processes

3. How to correlate multiple host artifacts (processes, files, IP connections) to identify Indicators of Compromise

4. The value of cross-verifying threat data through multiple vendor reports
 

# From Section 2.5, I learned that 
1. Network artifacts like unusual User-Agent strings can be valuable indicators of compromise (IOCs).

2, Emotet often uses spoofed User-Agent strings mimicking Internet Explorer to blend in with normal traffic.

3. PCAP analysis with TShark can quickly extract patterns such as repeated User-Agent strings for threat detection.

4. Detecting such patterns can give defenders a head start in identifying and mitigating malware infections.  


# From Section 2.6 - 2.7, I learned that..
1. Detecting or neutralizing the attacker’s tools (such as custom malware, EXEs, and backdoors) forces them to either rebuild or abandon the attack.

2. Fuzzy hashing (e.g., using ssdeep) is useful for detecting variants of known malware with only small differences.

3. Platforms like SOC Prime and MalwareBazaar help security analysts hunt and respond more effectively by sharing detection rules and malware samples.

4. TTP-level detection is the most effective strategy, as it targets how attackers operate, not just what tools or signatures they use.

5. Understanding frameworks like MITRE ATT&CK empowers defenders to map attacker behavior and break the kill chain early in the process. 





**Reflection**
These sections deepened my understanding of how attackers operate and how defenders can detect and respond effectively. I realized that relying on just one indicator—like hashes or IPs—is naive. Real-world detection needs multiple layers of analysis and cross-verification.  
More than anything, the labs made me appreciate the importance of thinking like an attacker to anticipate their moves and using frameworks like MITRE ATT&CK to stay one step ahead. Researching APT Groups was also fun because it connected theory to real-world threats — seeing how specific TTPs and infrastructure reuse patterns appear across different attack campaigns made the threat landscape feel more tangible and relevant.

This entire section reminded me that being a SOC analyst isn't just about watching alerts, but it's about connecting dots, recognizing patterns, and staying one step ahead of adversaries with smarter, layered defenses. 