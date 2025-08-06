# SPL Query to detect Top Brute-Force Source IPs
source="sample_windows_event_log.json" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| stats count by SourceIP
| sort -count
 


# SPL Query to detect Brute-Force attacks 
 source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| rex field=Message "Logon Type:\t+(?<LogonType>\d+)"
| where LogonType == "3"
| stats count by SourceIP, AccountName
| sort -count



# SPL Query to detect Brute-Force attacks (with GeoIP enrichment): 
source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| rex field=Message "Logon Type:\t+(?<LogonType>\d+)"
| where LogonType == "3"
| iplocation SourceIP
| fillnull value="N/A" City Country Region lat lon
| stats count by SourceIP, AccountName, City, Country, Region, lat, lon
| sort -count 


# SPL Query for Time-Based Analysis
source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| timechart span=1m count 

**SPL Query for Threat Response**  ---------
# SPL Query for flagging High-Risk IPs
source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| stats count by SourceIP
| eval RiskLevel=if(count > 20, "High", "Normal")
| sort -count
 

# SPL Query for flagging High-Risk IPs (with specific time window) 
source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| bin _time span=1m
| stats count by SourceIP, _time
| eval RiskLevel=if(count > 20, "High", "Normal")
| sort -count


# SPL Query to Export Suspicious IPs to a Lookup Table  
source="sample_windows_event_log.json" host="Jinnys-MacBook-Pro.local" index="splunk_project_index" sourcetype="_json"
| spath
| search EventID=4625
| rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
| rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
| bin _time span=1m
| stats count by SourceIP
| eval RiskLevel=if(count > 20, "High", "Normal")
| sort -count
| where RiskLevel="High"
| outputlookup suspicious_ips.csv 


# SPL Query to Reuse Suspicious IPs in Future Detection   
| inputlookup suspicious_ips.csv
| join type=inner SourceIP [
    search index=live_logs EventID=4625 
    | spath
    | rex field=Message "(?s)Account For Which Logon Failed:.*?Account Name:\t(?<AccountName>[^\r\n]+)"
    | rex field=Message "Source Network Address:\t(?<SourceIP>\S+)"
]
 
---------------------------------------------