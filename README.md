
# Django Vulnerable Web App (Educational Purposes Only)

This project is a deliberately insecure Django web application designed to **demonstrate common web vulnerabilities**. It's ideal for **security training, ethical hacking, CTF practice, and academic use**.

---

##  Vulnerabilities Demonstrated

| Vulnerability               | Status  |
|----------------------------|---------|
|  SQL Injection            | ✅ Built |
|  Cross-Site Scripting (XSS) | Coming Soon |
|  Command Injection        | Coming Soon |
|  CSRF (Cross-Site Request Forgery) | ✅ Built |
|  Insecure Direct Object Reference (IDOR) | Coming Soon |
|  Path Traversal           | Coming Soon |
|  Open Redirects           | Coming Soon |
|  Insecure Deserialization | Coming Soon |
|  Rate Limiting            | Coming Soon |

---

##  Example: SQL Injection

We use Django's built-in `auth_user` table to demonstrate SQL Injection.

###  Vulnerable Endpoint

```http
GET /get_user/?username=' OR '1'='1
```

###  Raw Query Behind the Scenes

```python
query = f"SELECT * FROM auth_user WHERE username = '{username}'"
```

> This allows attackers to bypass authentication and extract user data.

---
##  Example: CSRF (Cross-Site Request Forgery)

We use Django's form submission to demonstrate CSRF vulnerabilities.

###  Vulnerable Endpoint
```http
POST /transfer/
amount=1000&to_account=attacker
```
 Malicious Form Behind the Scenes
```
    <form method="POST" action="/transfer/">
        <!-- INSECURE: No CSRF protection -->
        <input type="text" name="to_account" placeholder="Recipient's Account" required>
        <input type="number" name="amount" placeholder="Amount ($)" required>
        <button type="submit">Transfer Money</button>
    </form>
```


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


