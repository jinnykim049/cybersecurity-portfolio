
This repository contains two hands-on cybersecurity projects that simulate common attack behaviors and show how to detect them using industry tools like Splunk and Wireshark.

---

## Project 1: Brute-Force Login Attempt Detection (Splunk)

**Objective:** Detect and respond to brute-force login attempts using synthetic Windows Event Logs (Event ID 4625) and Splunk.

- Design SPL queries for login pattern detection
- threat response simulation 
- Custom dashboards for attacker behavior visualization
- MITRE ATT&CK Mapped (T1110: Brute Force)

---

## Project 2: Credential Threat Detection & DNS Tunneling Analysis (Wireshark + MITRE)

**Objective:** Identify credential theft and covert data exfiltration over DNS using packet analysis with Wireshark.

- Base64 HTTP credential decoding (T1040)
- Kerberos Pre-auth hash analysis (T1557, T1003.004)
- DNS tunneling detection with TXT record and subdomain analysis (T1071.004)
- MITRE ATT&CK mapped for each technique

 
---

## Tools Used
- Wireshark
- Splunk Free Edition
- SPL (Search Processing Language) 
- ChatGPT-4o (for synthetic Windows Event log generation and Project assistance) 
- Public PCAP datasets from GitHub and Wireshark Wiki
- CyberChef (Base64 decoding)
- MITRE ATT&CK Framework
- Markdown (for documentation)