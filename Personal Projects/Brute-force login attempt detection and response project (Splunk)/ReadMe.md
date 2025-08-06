# Brute-Force Login Attempt Detection & Response (Splunk)

This project simulates a **real-world brute-force login attack** and demonstrates how to detect and respond using **Splunk** and **Windows Security Logs (Event ID 4625)**.

It walks through an end-to-end workflow from log ingestion, SPL query design, and attack pattern analysis, to visualization, alerting, and threat response simulation. The project is designed to reflect SOC-level security operations, aligned with the MITRE ATT&CK framework (T1110: Brute Force).

---

## Why This Project?
Brute-force login attacks are among the most common and persistent threats in cybersecurity. In real-world environments, detecting these attacks quickly and responding appropriately can prevent account compromise and lateral movement.


---

## Project Goals

- Detect brute-force login attempts using synthetic Event ID 4625 logs
- Extract attacker behavior using SPL queries (SourceIP, AccountName, LogonType, etc.)
- Visualize login failure patterns over time and by source
- Simulate incident response workflows (e.g., alerting, tagging, exporting)
- Align detection with the MITRE ATT&CK framework (T1110: Brute Force)


---

## Tools Used

- Splunk Free Edition
- Synthetic Windows Event Logs (generated using ChatGPT-4o)
- CyberChef 
- SPL (Search Processing Language)
- Markdown (for documentation)

 

