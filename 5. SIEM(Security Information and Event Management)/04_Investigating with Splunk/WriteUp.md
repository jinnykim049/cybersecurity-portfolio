**Reflection on the Splunk Lab** 
Working through this Splunk lab taught me not only how to use Splunk for threat hunting, but also how attackers behave and hide their tracks within Windows environments.
One of the biggest takeaways for me was understanding how Windows event IDs map to specific actions — for example, how Event ID 4720 signals user account creation, 4688 indicates process creation, and 4104 logs PowerShell script execution. These were key to building accurate Splunk queries and finding anomalies in the logs.

I also learned how attackers attempt to blend in or evade detection by creating backdoor users with names similar to legitimate ones (e.g., "A1berto" vs "Alberto"). This showed me how subtle malicious behavior can be, and how important it is to notice even small irregularities.

One particularly tricky but rewarding moment was decoding the Base64-encoded PowerShell command. At first, the output in CyberChef didn’t make sense — until I realized PowerShell encodes commands using UTF-16LE, not UTF-8. That taught me that understanding the encoding standards and inner workings of tools like PowerShell is critical when reversing encoded or obfuscated scripts.

Another highlight was discovering the remote execution command using WMIC.exe, and seeing how attackers can execute commands across machines on the network. This served as further confirmation that this lateral movement, and also privilege escalation is something often seen in the real world of attacks and detecting them being key to containing early. 

# What I Learned:
-How to effectively query and filter logs in Splunk.
-The importance of Windows Event IDs in forensic investigations.
-Techniques attackers use to evade detection (e.g., obfuscation, encoding, naming tricks).
-How PowerShell and WMIC can be abused for remote code execution.
-That decoding malicious scripts isn’t just about copying and pasting Base64, it’s also about understanding how they were encoded.

# Overall Impression:
This lab helped me think and act like a SOC analyst. It was less about “getting the right answer” and more about asking the right questions, parsing what those logs are actually saying, and connecting disparate events. It has made me comfortable in using Splunk, and more aware of how attackers move around compromised systems. 