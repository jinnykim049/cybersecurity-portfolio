# Lab 2.3 
Any.run is a sandboxing service! 
From its service, I could check 
1. HTTP requests tab- dropper / callback (resources being retrieved from a webserver), 
2. Connections tab - C2 traffic, uploading/downloaidng files over FTP etc 
3. DNS Requests tab -  to check for internet connectivity. 
 
Check [Screenshots/02/2.3/Screenshot 2025-06-30 at 2.19.50 PM.png] to see how the report looks like 

From these tabs, I could identify the first suspicious domain request was craftingalegacy.com

(See [Screenshots/02/2.3/Screenshot 2025-06-30 at 2.22.32 PM.png] to check where I found it.)    



# Lab 2.4 
From this section, I was able to check suspicious process execution from Word (Microsoft), Suspicious events followed by opening a malicious application, and the files modified/dropped by the malicious actor. 

The report about the malicious sample from a security vendor [PDF_resources/2.4_Lab.pdf], [Screenshots/02/2.4/Screenshot 2025-06-30 at 3.04.55 PM.png] allowed me to identify 

1. the IP address that indicates a process named regidle.exe which makes a POST request to an IP address based in the United States (US) on port 8080, and that is 96.126.101.6.
*Check [Screenshots/02/2.4/Screenshot 2025-06-30 at 2.53.27 PM.png] to see where I found it. 

2. the name of the malicious executable that the actop drops, which is G_jugk.exe. 
*Check [Screenshots/02/2.4/creenshot 2025-06-30 at 3.02.58 PM.png] to see where I found it. 

3. Number of vendors that determine this host (1,2) to be malicious via Virustotal. There are 9 vendors that determine it to be malicious. 
*Check [Screenshots/02/2.4/Screenshot 2025-06-30 at 3.07.21 PM.png] to see where I found it.  

 



# Lab 2.5 
From the screenshots [Screenshots/02/2.5/Screenshot 2025-06-30 at 3.48.37 PM.png] and [Screenshots/02/2.5/Screenshot 2025-06-30 at 3.29.26 PM.png] which indicates the most common User-Agent strings found for the Emotet Downloader Trojan, 
* Emotet Downloader Trojan: a sophisticated Trojan downloader that primarily spreads through malicious email attachments 


I could identify.. 
1. Internet Explorer uses the User-Agent string, 

From my obervation that the tshark command extracts the http.user_agent field from the pcap file, and the output shows lines like: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

With internet researching, I noticed that 
Mozilla/4.0: A common compatibility token
MSIE 7.0: Microsoft Internet Explorer 7
Windows NT 6.1: Windows 
Trident/7.0: Rendering engine for IE 11
.NET CLR, Media Center PC: Additional system info often spoofed or added by malware

Then I figured out that this string is most likely associated with Internet Explorer 11 running in compatibility mode (as IE 7) — which is commonly spoofed by malware like Emotet.  


2. There are 6 POST requests from the pcap file refer to this screenshot - [Screenshots/02/2.5/Screenshot 2025-06-30 at 3.48.37 PM.png]  
because according to this, there are 6 lines of POST request entries and each of these lines represents a unique HTTP POST request made by the infected host to a Command and Control (C2) server. 



# From this labs, I..  
- Used Any.run sandbox to analyze malware behavior via HTTP requests, DNS queries, and network connections.
- Identified suspicious domain  
- Traced malicious process execution and network traffic (POST requests to suspicious IP 96.126.101.6).
- Recognized malicious files dropped by malware (e.g., G_jugk.exe).
- Verified malware detection using VirusTotal and multiple vendor reports.
- Extracted User-Agent strings from network captures to detect malware spoofing legitimate browsers.
- Counted and analyzed unique POST requests showing malware communication with C2 servers.
- Developed skills in sandbox report interpretation, network traffic analysis, and threat intelligence verification.

