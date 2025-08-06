This project provided me with a hands-on investigation into how adversaries exploit unencrypted network protocols and authentication mechanisms to steal credentials or exfiltrate data using covert channels. Using Wireshark, I inspected three different PCAP files, each demonstrating a specific technique aligned with real-world adversary tactics.     


# What I accomplished from this Project 
- Kerberos Traffic Inspection: I successfully isolated AS-REQ packets and identified the encrypted PA-ENC-TIMESTAMP field, which adversaries could capture and use in offline password cracking (T1557).
- HTTP Credential Exposure: I filtered HTTP Basic Auth traffic and decoded Base64 credentials embedded in plaintext Authorization headers (T1040).
- DNS Tunneling Detection: I examined suspicious subdomains and TXT records used in repetitive DNS queries, strongly indicating DNS tunneling behaviors (T1071.004).
- MITRE ATT&CK Mapping: Each scenario was carefully mapped to applicable MITRE techniques to demonstrate how traffic analysis aligns with adversary behaviors. 
 

# What I learned from this Project  
- How to use Wireshark filters (http.authorization, kerberos, dns) to isolate credential-related traffic
- How credentials can be exposed through plaintext HTTP and encrypted Kerberos blobs
- How DNS tunneling is detected using behavioral patterns like long subdomains, repetitive base domains, and TXT record abuse
- How to apply MITRE ATT&CK techniques to validate detection logi
- How Wireshark filters can quickly surface malicious behavior in packet captures
- How credentials can be exposed in plaintext or derived form (even if encrypted) during authentication sequences
- DNS tunneling doesn't look like normal DNS—it has high frequency, long encoded queries, and consistent base domains

# In the future, I will.. 
- Explore more MITRE ATT&CK techniques and simulate PCAPs that demonstrate credential access via SMB, NTLM, or other protocols.
- Use tools like Zeek or Suricata for real-time detection instead of post-capture analysis.
- Build Splunk dashboards or alerts for similar behaviors based on packet captures. 
- Contribute a write-up or PCAP detection lab to the InfoSec community or GitHub 




# Final Reflection – Credential Threat Detection & DNS Tunneling Analysis (Wireshark + MITRE) 

* 1. Credential Theft via HTTP and Kerberos
First, I analyzed the 'http-basic-auth.pcap' file, which demonstrated how basic authentication credentials could be captured over unencrypted HTTP. Using the display filter 'http.authorization', I quickly isolated the relevant packets and decoded the base64-encoded credentials to extract the username and password pair (test:fail). This activity mapped directly to*MITRE ATT&CK Technique T1040: Network Sniffing and T1071.001: Web Protocol Abuse, reinforcing how unencrypted web protocols pose a major vulnerability in network security.

Next, I examined the 'krb-816.cap' file for Kerberos authentication traffic. I applied the display filter 'kerberos' to view Authentication Service Requests (AS-REQ) and observed the 'PA-ENC-TIMESTAMP' field within the pre-authentication data. 
Despite being encrypted, this timestamp is derived deterministically from the user's password. This means that attackers can perform offline brute-force attacks by capturing the blob and attempting decryption using dictionary attacks. This technique aligns with T1557: Adversary-in-the-Middle and T1003.004: Credential Dumping via Kerberos Tickets, demonstrating how pre-authentication traffic can expose users to serious risk even without plaintext credentials.

Through these exercises, I learned the importance of both transport-layer encryption and cryptographic protocol design in preventing credential leakage. I also realized that attackers don't necessarily need access to systems — they only need to intercept the right traffic. Applying filter and look for necessary fields to find evidence of attack was easy, and fun at the same time. 


* 2. DNS Tunneling Detection
The most technical and fascinating part of the project was inspecting 'tunnel_example.pcap' to uncover signs of DNS tunneling. DNS tunneling is a stealthy exfiltration technique in which data is encoded within subdomain queries to bypass firewalls. Using the display filter 'dns', I detected high-frequency DNS TXT queries between two internal IPs. These queries featured highly variable, base64-looking subdomains targeting a consistent base domain ('.tunnel.onetwog.leb.tech').

By analyzing the length, frequency, and structure of these subdomains, I concluded that encoded payloads were likely being exfiltrated over DNS. This activity perfectly maps to MITRE ATT&CK Technique T1071.004: DNS Protocol Abuse and T1040: Network Sniffing. High query volume in short bursts further confirmed the likelihood of tunneling, since typical DNS traffic is sporadic and low-volume.

This analysis taught me how sophisticated data exfiltration can be concealed within legitimate-looking traffic, and why DNS — though often ignored — must be monitored closely in enterprise environments.

* 3. Applying MITRE ATT&CK for Realism
One of the key learning points across all three detections was the integration of *MITRE ATT&CK techniques. By aligning each observed behavior with ATT&CK tactics and techniques, I could relate my packet-level findings to larger adversarial strategies. Whether it was password interception, Kerberos pre-auth cracking, or DNS exfiltration, the framework helped validate my detection logic and made the analysis feel grounded in real-world threat intelligence.

This practice also helped me think more like a threat hunter: recognizing how patterns of seemingly normal behavior—like DNS queries or authentication attempts—can reveal covert adversary activity when viewed with the right lens.

Here is my final thoughts after this project. 
This project expanded my understanding ofcredential threat vector and covert network behaviors, pushing me to look deeper into packet-level analysis. It gave me the tools to not only detect common vulnerabilities but also the confidence to relate them to adversary behavior frameworks like MITRE ATT&CK. 
I feel more prepared to investigate traffic anomalies and design effective detection strategies.
In the future, I hope to scale this kind of work by using Suricata or Zeek for automated detection and eventually build a real-time alerting pipeline that uses these packet indicators for SOC response. For now, Wireshark has been an amazing entry point into the world of network-level threat detection.
 