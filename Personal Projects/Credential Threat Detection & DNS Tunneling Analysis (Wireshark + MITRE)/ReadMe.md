# Credential Threat Detection & DNS Tunneling Analysis (Wireshark + MITRE) 
This project investigates real-world credential theft scenarios using packet capture (PCAP) files and Wireshark. The primary objective is to simulate credential theft and tunneling attacks, analyze the captured traffic, and align the findings with MITRE ATT&CK techniques for better understanding of adversarial behavior. 



* What is WireShark?: a free and open-source network protocol analyzer used to capture, inspect, and analyze network traffic in real time. It allows detailed examination of data packets transmitted over a network and is commonly used for troubleshooting, network performance analysis, and cybersecurity investigations.

* What is MITRE ATT&CK framework?: a globally-accessible knowledge base of adversary tactics and techniques, based on real-world observations of cyberattacks. 

* Why MITRE ATT&CK Mapping Matters: 
MITRE ATT&CK mapping refers to the practice of aligning security detections, logs, and incidents with specific tactics and techniques from the ATT&CK matrix. 
It is crucial because it enhances threat detection coverage by identifying gaps across known attack techniques. 
It enables a threat-in  formed defense, helping security teams prioritize based on real-world adversary behavior rather than theoretical risks. 
During incident response and threat hunting, the mapping offers valuable insight into attacker tactics, speeding up analysis and response. 
By standardizing terminology (e.g., T1110 for brute force), it improves communication across teams, tools, and reports. It also strengthens executive reporting by clearly showing what threats were detected or missed, and supports alignment with compliance frameworks like NIST and ISO 27001. 
 




## Why This Project?
Credential theft remains one of the most exploited tactics by threat actors. Understanding how login data and covert channels appear in real network traffic helps defenders detect and mitigate attacks early. 

This project covers three common attack vectors:
- Credential exposure via Kerberos authentication (T1557, T1003.004)
- Plain-text HTTP authentication over insecure channels (T1040, T1071.001)
- DNS tunneling for covert C2 and exfiltration (T1071.004, T1040) 


---

## Project Goals

-Inspect credential artifacts in Kerberos pre-authentication packets
-Detect plaintext credentials in HTTP traffic
-Identify encoded data exfiltration using DNS tunneling
-Map observed behaviors to MITRE ATT&CK techniques


---

## Tools Used
- Wireshark
- CyberChef  
- Public PCAP datasets from GitHub and Wireshark Wiki
- Markdown (for documentation) 

 