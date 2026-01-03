
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
