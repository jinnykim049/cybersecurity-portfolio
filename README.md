# cybersecurity-portfolio

# TryHackMe - SOC Level 1 Portfolio

This repository contains my personal write-ups and summaries from completing the **TryHackMe - SOC Level 1 Learning Path**.

The path is designed to simulate real-world SOC (Security Operations Center) analyst responsibilities, including:
- log analysis
- threat detection
- SIEM queries
- attacker behavior investigation

Each directory corresponds to a specific TryHackMe room I completed as part of this path.

## 🎯 Why I did this
Rather than just solving pre-built rooms, I approached each challenge with a real SOC workflow in mind:
- What's the incident?
- Where would I look first as a SOC analyst?
- Which artifacts would confirm the attacker’s behavior?

## 🔎 My Focus per Topic
- Windows Logs → focused on correlation between 4624 and 4688 (logon + process creation)
- SIEM → optimized search queries to reduce alert noise
- Phishing → reversed engineered EML headers + tested sandboxed click behavior



## 🧠 What I learned
- How to analyze Windows Event Logs for suspicious behavior
- How to use Splunk and Kibana for log correlation and threat detection
- Common attacker behaviors (brute-force, privilege escalation, etc.)
- Interpreting Sysmon logs, Event IDs, and network artifacts

## ✅ Rooms Completed
| Room Name | Description |
|-----------|-------------|
| `Intro to SOC` | Overview of SOC roles and responsibilities |
| `Windows Logs` | Hands-on analysis of local Windows event logs |
| `Kibana Lab` | Using Kibana to detect attack patterns |
| `Splunk Search` | Basic Splunk query building for SOC analysts |

## 🔧 Tools Used
- Windows Event Viewer / Sysmon
- Kibana / Elasticsearch
- Splunk
- TryHackMe platform

## 🗂️ How to navigate this repo
Each subfolder contains:
- A write-up of the room
- Screenshots of the analysis process
- Key commands/queries used


This repository follows the learning structure from [TryHackMe - SOC Level 1 Learning Path](https://tryhackme.com/path/outline/soc-level-1), which simulates real-world SOC analyst workflows and practical detection tasks.

Each folder corresponds to a learning module in the path:
1. Introduction to SOC
2. Windows Logs
3. Malware Traffic Analysis
4. Kibana
5. Splunk
6. Detection Engineering
 
 
