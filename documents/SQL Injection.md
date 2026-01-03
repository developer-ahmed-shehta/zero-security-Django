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