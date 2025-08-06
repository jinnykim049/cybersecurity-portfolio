## Lab 
With Static Site Lab, I was able to expereince a little bit of security monitoring tool. 
- Check [Screenshots/2025-06-30_12.25.54_PM.png]  

I could detect from Alert Log that there was a malicious activity on April 16t, 2024, Unauthorized connection attempt detected from IP address 221.181.185.159 to port 22. Then I got to know general steps taken after this detection 



# From this lab, I learned that.. 
There are many open-source databases out there like AbuseIPDB, Cisco Talos Intelligence, where you can perform a reputation and location check for the IP address. Most security analysts use these tools to aid them with alert investigations. You can also make the Internet safer by reporting the malicious IPs, for example, on AbuseIPDB. 

After determining if the IP addess is malicious, then the issue should be escalated to a staff member. 

This issue, "Unauthorized connection attempt", should be escalated to SOC Team Lead, and after getting permission, I can proceed and implement the block rule. 

After blocking it, I could see a message that malicious actor left. "THM{UNTIL-WE-MEET-AGAIN}". - I noticed that malicious actor could leave message to defenders of t 