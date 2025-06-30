## 🧾 Objective

간단한 목표 요약. 예:

"Identify suspicious activity using Windows Event Logs and Sysmon."

---

## 🛠️ Tools Used

- Event Viewer
- Sysmon
- TryHackMe virtual machine

---

## 🔍 Key Findings

| Event ID / Signature | Meaning | Why It Matters |
| --- | --- | --- |
| 4625 | Failed logon | Potential brute-force attempt |
| 4688 | New process creation | Indicates script-based execution |
| Sysmon ID 1 | Process execution | Track suspicious binaries |

---

## 🧪 What I Did

- Enabled Sysmon and observed event logging
- Simulated failed login attempts
- Investigated powershell command launches
- Correlated logs with TryHackMe attack scenario

---

## 🧠 What I Learned

- How to read and interpret common Windows event logs
- The importance of Event ID correlation in detecting attacks
- Practical experience using Sysmon and log viewers

---

## 📸 Screenshots

See screenshots/ folder. 
- `screenshots/event-4625.png`: Multiple failed logons within short time
- `screenshots/process-launch.png`: Suspicious PowerShell payload

---

## 📄 References

- TryHackMe: “Windows Logs” room
- Microsoft: [Sysmon Documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- MITRE ATT&CK T1059 – Command and Scripting Interpreter  