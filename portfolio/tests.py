"""
Portfolio App Tests

Tests for the portfolio app using Django's testing framework.
Tests help ensure your code works correctly and doesn't break when you make changes.

Learning concepts:
- TestCase: Django's test class with database setup/teardown
- Client: Simulates HTTP requests to test views
- reverse(): Get URL by name instead of hardcoding path
- Assertions: Methods to check if conditions are true

Running tests:
    python manage.py test                    # Run all tests
    python manage.py test portfolio          # Run tests for portfolio app
    python manage.py test portfolio.tests.IndexViewTests  # Run specific test class

Test-Driven Development (TDD):
1. Write a test (it fails - red)
2. Write code to make it pass (green)
3. Refactor code (keep it green)
"""

from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTests(TestCase):
    """
    Tests for the homepage (index) view.

    Each test method should test one specific behavior.
    Method names must start with 'test_' to be discovered by the test runner.
    """

    def setUp(self):
        """
        Run before each test method.

        setUp() is called before EVERY test method in this class.
        Use it to create test data or set up common objects.

        Here we create a test client to simulate HTTP requests.
        """
        self.client = Client()

    def test_index_view_status_code(self):
        """
        Test that the homepage returns HTTP 200 OK.

        Learning notes:
        - reverse('portfolio:index') gets URL by name (good practice)
        - client.get() simulates a GET request
        - assertEqual() checks if two values are equal
        - 200 is the HTTP status code for "OK" (successful request)
        """
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """
        Test that the homepage uses the correct template.

        Learning notes:
        - assertTemplateUsed() checks which template was rendered
        - Django automatically looks in app/templates/ directories
        - 'portfolio/index.html' is resolved to portfolio/templates/portfolio/index.html
        """
        response = self.client.get(reverse('portfolio:index'))
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_index_view_contains_name(self):
        """
        Test that the homepage contains the portfolio owner's name.

        Learning notes:
        - assertContains() checks if response HTML contains a string
        - This verifies that template rendering is working
        - Case-sensitive by default
        """
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, 'anthony bronkema')

    def test_index_view_contains_job_title(self):
        """
        Test that the homepage contains the job title.

        This ensures context variables are being passed correctly
        from the view to the template.
        """
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, 'Product Manager')

    def test_index_view_contains_github_link(self):
        """
        Test that the homepage contains the GitHub link.

        Verifies that external links are rendered correctly.
        """
        response = self.client.get(reverse('portfolio:index'))
        self.assertContains(response, 'https://www.github.com/abronkema')

    def test_index_view_context_data(self):
        """
        Test that the view passes correct context data to the template.

        Learning notes:
        - response.context is a dictionary of variables passed to template
        - This tests the view's logic, not just the rendered output
        - Good for ensuring data is available even if template changes
        """
        response = self.client.get(reverse('portfolio:index'))

        # Check that context contains expected keys
        self.assertIn('name', response.context)
        self.assertIn('job_title', response.context)
        self.assertIn('email', response.context)
        self.assertIn('github_url', response.context)

        # Check specific values
        self.assertEqual(response.context['name'], 'anthony bronkema')
        self.assertEqual(
            response.context['job_title'],
            'Product Manager at University of Virginia'
        )
        self.assertEqual(
            response.context['email'],
            'hey@anthonybronkema.com'
        )


# Future: Add more test classes as you add features
#
# class ProjectModelTests(TestCase):
#     """Tests for the Project model"""
#     pass
#
# class BlogPostModelTests(TestCase):
#     """Tests for the BlogPost model"""
#     pass
