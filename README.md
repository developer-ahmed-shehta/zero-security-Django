
# Django Vulnerable Web App (Educational Purposes Only)

This project is a deliberately insecure Django web application designed to **demonstrate common web vulnerabilities**. It's ideal for **security training, ethical hacking, CTF practice, and academic use**.

---

##  Vulnerabilities Demonstrated

| Vulnerability               | Status  |
|----------------------------|---------|
|  SQL Injection                           | ✅ Built    |
|  Cross-Site Scripting (XSS)              | ✅ Built    |
|  Command Injection                       | Coming Soon |
|  CSRF (Cross-Site Request Forgery)       | ✅ Built    |
|  CORS (Cross-Origin Resource Sharing)    | Coming Soo  |
|  Insecure Direct Object Reference (IDOR) | Coming Soon |
|  Path Traversal                          | Coming Soon |
|  Open Redirects                          | Coming Soon |
|  Insecure Deserialization                | Coming Soon |
|  Rate Limiting (DDOS)                    | Coming Soon |
|  Social Engineering ( phishing)          | Coming Soon |

---
## for more detail look at document Folder
---
##  Tech Stack

- **Framework**: Django 5.2.3
- **Database**: SQLite (default)
- **Language**: Python 3.13+

---

##  Warning

> ⚠️ **This application is intentionally insecure**.  
> Use **only in safe, isolated environments** such as virtual machines, Docker containers, or offline labs.  
> **Never deploy in production!**

---

##  Project Structure

```
security-problems/
├── ZeroSecurity/            # Django app with vulnerable views
│   └── templates/
│       └── ZeroSecurity/
│           └── get_user.html
│           └── transfer.html
│           └── evil.html
├── accounts/ 
├── Cross_Site_Scripting/ 
├── templates/
├── db.sqlite3               # SQLite database
├── manage.py
├── security_problems/      # Project settings and URLs
└── README.md
```

---

##  Coming Soon

We will expand the app with more security flaws like:
- Persistent & Reflected XSS
- Remote Command Execution (RCE)=
- Broken Access Control examples (IDOR)
- Path traversal for file access
- Redirect-based phishing tricks
- Deserialization exploits

---

##  Author

**Ahmed Shehta**, a passionate security learner.  
Want to contribute? Feel free to fork and expand the project.

---






