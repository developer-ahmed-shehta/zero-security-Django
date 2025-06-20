# views.py

# Import the Django database connection and rendering function
from django.db import connection
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
