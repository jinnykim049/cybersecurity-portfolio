# Sumamry of what each field shows: 
**Reconnaisance**
*alert.signature*:
*uri*: to check url 
*http_method*: to check how attackers interact with web servers. (What tool did they use?)


**Exploitation** 
*form_data* : contains the requests sent through the form on the admin panel page, which has a login page. 
*creds*:  stores extracted credentials (username/password) used in login attempts.
*http_user_agent*: reveals whether the attacker is using a script/tool to automate login attempts.  
*uri_path*: helps confirm whether the login page or admin panel was targeted. 
*status_code*: shows whether the login attempt was successful (e.g., 200 = success, 401 = unauthorized)  


**Installation**
*part_filename{}*:  shows the name of the uploaded or downloaded file involved in the attack.
*c_ip*: client ip address (attacker's IP)
*User*: Username who executed the file
*process_name*: reveals what process was launched—can confirm malware execution.  

**Action on Objectives**
*attack*: to get the name of the rule that was triggered during the malicious attempt. 
*URL*: shows the specific resource or endpoint that was modified or targeted.
*file_name / file_path*: helps identify what content was modified or dropped (e.g., defacement image).
*dest_ip / dest_port*: reveals the target system and service involved in the final action phase.  

