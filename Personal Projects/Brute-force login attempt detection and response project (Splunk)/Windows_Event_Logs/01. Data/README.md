# About Data - Log Source 
The dataset used in this project consists of synthetic Windows Security logs generated using ChatGPT-4o to simulate both normal system activity and potential security incidents. The logs span from August 3, 2025, 12:00:00 to August 3, 2025, 12:59:59, covering approximately one hour of simulated system behavior.
There are total 850 events log, and this dataset includes a diverse set of Windows Event IDs, such as:

4625 – Failed logon attempts (used to simulate brute-force attacks)
4624 – Successful logons
4648 – Explicit credential usage
4672 – Logons with special privileges
4720 – User account creation
4634 – Logoff events
5140 – Network share accesses

All logs follow the standard Microsoft Windows Event Log structure, specifically based on the Microsoft-Windows-Security-Auditing source.
Key fields like EventID, Account Name, Logon Type, Source Network Address, Source Port, and Failure Reason are formatted in realistic Message strings to allow meaningful parsing, field extraction, detection logic, and visualization within Splunk.

This dataset is designed to support a variety of detection scenarios—not limited to brute-force attacks—including lateral movement, privilege escalation, and suspicious account creation, making it suitable for multi-layered security analysis projects for future analysis. 

Note: The reason I chose to use this dataset rather than publicly available samples is explained in the section **First Trouble** found in 'Personal Projects/Brute-force login attempt detection and response project (Splunk)/Windows_Event_Logs/03. Analysis_report/Trouble_Shooting_Note.md'



# Why do I have "Convert_Data" Folder?-
please read **First Trouble** from Personal Projects/Brute-force login attempt detection and response project (Splunk)/Windows_Event_Logs/03. Analysis_report/Trouble_Shooting_Note.md

I first visited the GitHub repository Windows-Event-Samples (https://github.com/d4rk-d4nph3/Windows-Event-Samples), where I downloaded a sample event log containing Windows Event ID 4625, which signifies a failed logon attempt.
However, the file was only available in .log format, which is an unstructured plaintext format that Splunk cannot directly ingest or parse effectively.
To resolve this, I wrote a Python3 script to parse the raw .log file and convert it into structured .json format. 

* Python Script location:
(Personal Projects/Brute-force login attempt detection and response project (Splunk)/Windows_Event_Logs/01. Data/Convert_Data/FuncToConvert.py) 
 