## cybersecurity-portfolio

# Personal Projects 
**Project 1: Brute-force login attempt detection and response project (Splunk)**
Simulated brute-force attacks using synthetic Windows Event Logs (Event ID 4625) in Splunk.

- Parsed SourceIP, AccountName, LogonType to detect failed logins.
- Flagged IPs with >20 failures/hour -> tagged as High Risk.
- Used 'iplocation' for geolocation enrichment.
- Created dashboards + alert workflows.
- Mapped to MITRE T1110: Brute Force.

* Learned:  
SPL query writing, alerting, threat modeling, data enrichment, SIEM workflows 


**Project 2: Credential Threat Detection & DNS Tunneling Analysis (Wireshark + MITRE)**
Analyzed 3 PCAPs for credential theft & covert exfiltration techniques (DNS Tunneling Attack).

- HTTP Basic Auth -> Decoded credentials (T1040, T1071.001)
- Kerberos -> Detected offline cracking risk via AS-REQ (T1557, T1003.004)
- DNS Tunneling -> Identified TXT abuse & encoded subdomains (T1071.004)

* Learned:  
Wireshark filtering, traffic analysis, MITRE mapping, attacker detection patterns



> These projects (1&2) reflect my skills in threat detection, network forensics, and real-world TTP analysis using Splunk & Wireshark.





# TryHackMe - SOC Level 1 Portfolio
This repository contains my personal write-ups and summaries from completing the **TryHackMe - SOC Level 1 Learning Path**.
All contents are personally executed, documented, and interpreted to demonstrate my understanding of topics such as network security, SIEM, and digital forensics.
Some module names are referenced only for educational purposes. 


The path is designed to simulate real-world SOC (Security Operations Center) analyst responsibilities, including:
- log analysis
- threat detection
- SIEM queries
- attacker behavior investigation

Each directory corresponds to a specific TryHackMe room I completed as part of this path.

* Why I did this: 
Rather than just solving pre-built rooms, I approached each challenge with a real SOC workflow in mind:
- What's the incident?
- Where would I look first as a SOC analyst?
- Which artifacts would confirm the attacker’s behavior?

This repository follows the learning structure from [TryHackMe - SOC Level 1 Learning Path](https://tryhackme.com/path/outline/soc-level-1), which simulates real-world SOC analyst workflows and practical detection tasks.

Note: This portfolio is still on-going. 
 
 
