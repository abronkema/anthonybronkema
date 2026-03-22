"""
Portfolio Views

Function-based views for the portfolio app.
Starting simple with a single view that renders the homepage.

Learning concepts:
- Function-based views: Simple Python functions that handle HTTP requests
- request parameter: HttpRequest object containing metadata about the request
- render(): Shortcut that loads a template and returns an HttpResponse
- Context dict: Python dictionary passed to templates as variables
- Template rendering: Django finds the template and fills in {{ variables }}

Django request/response cycle:
1. User visits URL (e.g., http://localhost:8000/)
2. Django's URL dispatcher matches URL to this view function
3. View function processes request and prepares data (context)
4. Django renders template with context data
5. View returns HttpResponse with HTML to user's browser
"""

from django.shortcuts import render


def index(request):
    """
    Homepage view for the portfolio.

    Args:
        request: HttpRequest object containing metadata about the request
                 (HTTP method, headers, user info, etc.)

    Returns:
        HttpResponse: Rendered HTML template with context data

    Learning notes:
    - All Django views receive a 'request' parameter as the first argument
    - render() is a shortcut that combines template loading and HttpResponse
    - Context dict keys become template variables (e.g., 'name' becomes {{ name }})
    - render() automatically escapes HTML in variables for security (XSS protection)
    """
    # Context: Dictionary of data to pass to the template
    # These variables will be available in the template as {{ variable_name }}
    context = {
        'name': 'anthony bronkema',
        'job_title': 'Product Manager at University of Virginia',
        'job_description': 'cloud applications and enterprise licensing',
        'email': 'hey@anthonybronkema.com',
        'github_username': 'abronkema',
        'github_url': 'https://www.github.com/abronkema',
    }

    # render() function:
    # 1. Loads the template from portfolio/templates/portfolio/index.html
    # 2. Fills in template variables with context data
    # 3. Returns an HttpResponse with the rendered HTML
    return render(request, 'portfolio/index.html', context)
