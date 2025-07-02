# views.py

# Import the Django database connection and rendering function
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render


# View to render the search form template
def search_form(request):
    # This simply renders the HTML form for input
    return render(request, 'ZeroSecurity/get_user.html')


# View to handle the GET request to fetch user info
def get_user(request):
    # Retrieve the 'username' value from the GET request query parameters
    username = request.GET.get('username')
    result = None  # Variable to store the query result

    # Check if a username was provided
    if username:
        # Open a database cursor to execute raw SQL
        with connection.cursor() as cursor:
            # ⚠️ SECURITY WARNING:
            # The following line is intentionally vulnerable to SQL Injection
            # This is done for demonstration purposes only.
            query = f"SELECT id, username, email FROM auth_user WHERE username = '{username}'"

            # Execute the raw SQL query
            cursor.execute(query)
            # Fetch all matching rows
            result = cursor.fetchall()

        # If no result was found, mark as 'not_found'
        if not result:
            result = "not_found"

    # Render the same template, passing the result to the context
    return render(request, 'ZeroSecurity/get_user.html', {'result': result})


# This view can be for delete your account, but I used transfer for reality
def transfer(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        to_account = request.POST.get("to_account")
        return HttpResponse(f"Transferred ${amount} to {to_account}!")
    return render(request, "ZeroSecurity/transfer.html")


def evil_page(request):
    return render(request, "ZeroSecurity/evil.html")