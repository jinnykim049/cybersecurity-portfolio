SOC Analyst Johny has observed some anomalous behaviours in the logs of a few windows machines. It looks like the adversary has access to some of these machines and successfully created some backdoor. His manager has asked him to pull those logs from suspected hosts and ingest them into Splunk for quick investigation. Our task as SOC Analyst is to examine the logs and identify the anomalies.


# Answer the questions below
* Q1. How many events were collected and Ingested in the index main?
A1. 12256 

Reason: 
I simply ran this query and got the result. -> "index = "main""
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 6.48.49 PM.png)


* Q2. On one of the infected hosts, the adversary was successful in creating a backdoor user. What is the new username?
A2. A1berto

Reason: 
I did some research and found out that Windows event ID for creating a user is 4720. Therefore, I added "EventID = "4720"" to the query and ran it. 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 7.07.45 PM.png)

This (part of) log means James (from domain Cybertees) used his privileges to create a new user account called "A1berto" on WORKSTATION6. (Subject: James, New Account: A1berto). Therefore, the new username is A1berto. 


* Q3. On the same host, a registry key was also updated regarding the new backdoor user. What is the full path of that registry key?
A3. HKLM\SAM\SAM\Domains\Account\Users\Names\A1berto\

Reason: 
From research, I figured out that in Splunk, events generated when there are changes to the Windows Registry, captured by Sysmon (specifically, Event ID 13). 
With this information and since the question said Same  host, I kept "A1berto". Then I finally ran this query. "index="main" EventID=13 A1berto". Then clicked "TargetObject" from the fields, and found the answer. 
(In Sysmon Event ID 13, which logs registry key changes, the TargetObject field contains the full path of the registry key that was modified.)

(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 7.24.52 PM.png)


* Q4. Examine the logs and identify the user that the adversary was trying to impersonate.
A4. Alberto

Reason: 
The answer is clearly Alberto because the name A1berto, the backdoor username looks very similar to the general name Alberto. Here is more support: from User field with query "index="main"", I could see the username "Alberto"
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 7.35.47 PM.png)


* Q5. What is the command used to add a backdoor user from a remote computer? 
A5. "C:\windows\System32\Wbem\WMIC.exe" /node:WORKSTATION6 process call create "net user /add A1berto paw0rd1"

Reason: 
To get the command, I needed to find the window logs that indiciates the creation of a new process, which is Event ID 4688 based on the research. I should include Event ID 1 which also indiciates the creation of a new process in Sysmon. 
Therefore, I ran this query: "index="main" EventID=1 OR EventID=4688 A1berto".

Then I clicked on "CommandLine" from field and got 4 command lines. I could see that the first one is a command to add a backdoor user from a remote computer because this command is using WMIC.exe with the /node:WORKSTATION6 option, which indicates remote execution. 

(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 8.11.52 PM.png)

(More: This command remotely connects to a machine named WORKSTATION6 and runs net user /add A1berto paw0rd1, creating a new local user account named "A1berto" with a preset password. The presence of WMIC and the /node flag clearly differentiates it from the other commands shown, which all executed locally.
About net user- The net user command is a built-in Windows command-line utility used to manage local user accounts. It allows administrators (or attackers) to create, modify, delete, or view user accounts on a computer. For example, the command net user A1berto paw0rd1 /add creates a new local user account named A1berto with the password paw0rd1.) 


* Q6. How many times was the login attempt from the backdoor user observed during the investigation?
A6. 0

Reason: 
I ran this query: "index="main" EventID="4625" OR EventID="4624" A1berto" 

because Event ID 4624 signifies a successful logon to a Windows system, while Event ID 4625 indicates a failed logon attempt. Therefore, this query would give me all  login attempts from the backdoor user A1berto. 
And this is what I saw after running the query: 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 8.17.37 PM.png)
There was no result, so I could assert that there were zero login attempts with the backdoor user. 



* Q7. What is the name of the infected host on which suspicious Powershell commands were executed?
A7. James.browne

Reason: 
I ran this query: "index="main" EventID="4103" OR EventID="4104"" because based on the internet research, I got to know that Event ID 4103 signifies PowerShell Command Line Block Logging and Event ID 4104 signifies PowerShell Script Block Logging. 
Then I clicked on Hostname from field and found only James.browne. 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 8.27.44 PM.png)

- What is PowerShell?: 
PowerShell is a command-line shell, scripting language, and automation framework developed by Microsoft. It’s built on .NET (a software development platform created by Microsoft. It's a framework that provides the tools, libraries, and runtime needed to build and run applications) and designed especially for system administration and automation. 


* Q8. PowerShell logging is enabled on this device. How many events were logged for the malicious PowerShell execution? 
A8. 79

Reason: 
Read the Q7. There were 79 activities with malicious PowerShell execution. 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 8.37.02 PM.png)


* Q9. An encoded Powershell script from the infected host initiated a web request. What is the full URL? 
A9. http://10.10.10.5/news.php 

From Q7-8 log, I could see that SQB.. is Base64-encoded PowerShell script. 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 8.55.47 PM.png)
To extract full URL from it, I needed to decode this string. 
Therefore, I copied the full line of Base64-encoded PowerShell script and went to CyberChef (https://cyberchef.io/) to decode the line from base64. 

I was stuck here because after clicking Bake! the output looked so broken. (View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 9.09.23 PM.png) 

After doing some research, I could resolve this problem. I should have also applied Decode text - encoding: UTF-16LE in the Recipe setting. 
It is because when PowerShell uses the -EncodedCommand (or -enc) flag, it Base64-encodes the script, but it doesn't use UTF-8 or ASCII for the encoding, it uses UTF-16LE. PowerShell Base64-encoded commands use UTF-16LE internally so I must decode the Base64 output as UTF-16LE to get readable script content. 

(View the proper decoded line after applying this configuration: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 9.15.45 PM.png)

The highlighted part is important because it hides the real URL using double encoding (base64 + UTF-16LE).
Malware authors do this to evade detection in plain-text logs or memory. By decoding it, I'll reveal the command and control (C2) or payload server URL.
To do that, I first took this string: aAB0AHQAcAA6AC8ALwAxADAALgAxADAALgAxADAALgA1AA==, and added a new Tab on the CyberChef. Then I applied Defang URL and started Bake. 
After clicking on Bake, I could finally see the full URL - "hxxp[://]10[.]10[.]10[.]5."  
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 9.24.57 PM.png)

It's not the answer yet. From the log, I saw the variables $ser and $t. 
(View image: 5. SIEM(Security Information and Event Management)/Screenshots/04/Screenshot 2025-08-02 at 9.31.42 PM.png) 
I identified that PowerShell was executed with DownloadString($ser + $t). Therefore, I concluded that the full URL is "http://10.10.10.5" + "/news.php", which results in "http://10.10.10.5/news.php". 
 
 