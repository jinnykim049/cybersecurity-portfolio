# Summary of Splunk Event IDs (Sysmon + Windows Security)
🔹 Sysmon (System Monitor)
* Event ID 1 – Process Creation
Logs detailed information when a process is created, including command-line arguments, parent process, user, hash of the executable, and more.

* Event ID 13 – Registry Value Set
Triggered when a registry value is modified. Useful for detecting changes to the Windows Registry, including persistence techniques.

* Event ID 4103 – PowerShell Command Line Logging
Captures executed PowerShell commands via script block logging.

* Event ID 4104 – PowerShell Script Block Logging
Logs the content of entire PowerShell scripts or blocks, helping detect malicious scripts.


🔹 Windows Security Logs
* Event ID 4688 – New Process Created
Logged when a new process is created. Includes the process name, creator process ID, user context, etc. Less detailed than Sysmon Event ID 1.

* Event ID 4720 – User Account Created
Logged when a new local or domain user account is created.

* Event ID 4624 – Successful Logon
Indicates a successful authentication attempt on a Windows system.

* Event ID 4625 – Failed Logon
Indicates a failed authentication attempt (e.g., wrong password or username). 


----
Notes:
* Windows Security Logs:
Native, built-in logging mechanism in Windows. Captures important security events like logons, account changes, and privilege usage.

* Sysmon (System Monitor): 
A Windows Sysinternals tool by Microsoft that provides deeper visibility into process creation, network connections, registry modifications, etc.
-> Must be manually installed and configured with a rule set (e.g., SwiftOnSecurity config).