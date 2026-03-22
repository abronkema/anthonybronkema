"""
Portfolio Models

Django models define the structure of your database tables.
Currently, this portfolio doesn't use a database (it's a static portfolio).

However, this file includes commented examples of models you might add later
as you learn more about Django's ORM (Object-Relational Mapping).

Learning concepts:
- Models: Python classes that represent database tables
- Fields: Class attributes that represent table columns
- Meta class: Options for the model (ordering, unique constraints, etc.)
- __str__() method: String representation of model instances

To activate these models:
1. Uncomment the model class you want to use
2. Run: python manage.py makemigrations
3. Run: python manage.py migrate
4. Register in admin.py to manage via Django Admin
"""

from django.db import models


# Future: Project showcase model
# Uncomment this when you're ready to add a projects section to your portfolio
#
# class Project(models.Model):
#     """
#     Model for portfolio projects.
#
#     Each project represents work you want to showcase.
#     Fields include title, description, links, and metadata.
#     """
#     title = models.CharField(
#         max_length=200,
#         help_text="Project name (e.g., 'Django Portfolio')"
#     )
#     description = models.TextField(
#         help_text="Detailed description of the project"
#     )
#     url = models.URLField(
#         blank=True,
#         help_text="Live project URL if deployed"
#     )
#     github_url = models.URLField(
#         blank=True,
#         help_text="GitHub repository URL"
#     )
#     image = models.ImageField(
#         upload_to='projects/',
#         blank=True,
#         help_text="Project screenshot or logo"
#     )
#     technologies = models.CharField(
#         max_length=500,
#         help_text="Comma-separated list of technologies used"
#     )
#     created_date = models.DateField(
#         help_text="When the project was created"
#     )
#     is_featured = models.BooleanField(
#         default=False,
#         help_text="Show on homepage?"
#     )
#
#     class Meta:
#         # Order projects by most recent first
#         ordering = ['-created_date']
#         verbose_name = 'Project'
#         verbose_name_plural = 'Projects'
#
#     def __str__(self):
#         """String representation shown in admin and shell"""
#         return self.title


# Future: Blog post model
# Uncomment this when you're ready to add a blog to your portfolio
#
# class BlogPost(models.Model):
#     """
#     Model for blog posts.
#
#     Allows you to write and publish articles on your portfolio site.
#     Could be used for technical writing, project updates, or thoughts.
#     """
#     title = models.CharField(
#         max_length=200,
#         help_text="Blog post title"
#     )
#     slug = models.SlugField(
#         unique=True,
#         help_text="URL-friendly version of title (e.g., 'my-first-post')"
#     )
#     content = models.TextField(
#         help_text="Blog post content (supports Markdown)"
#     )
#     excerpt = models.TextField(
#         blank=True,
#         max_length=500,
#         help_text="Short summary for post listings"
#     )
#     published_date = models.DateTimeField(
#         help_text="When to publish this post"
#     )
#     updated_date = models.DateTimeField(
#         auto_now=True,
#         help_text="Last time post was updated"
#     )
#     is_published = models.BooleanField(
#         default=False,
#         help_text="Make post publicly visible?"
#     )
#     tags = models.CharField(
#         max_length=200,
#         blank=True,
#         help_text="Comma-separated tags"
#     )
#
#     class Meta:
#         # Order posts by most recent first
#         ordering = ['-published_date']
#         verbose_name = 'Blog Post'
#         verbose_name_plural = 'Blog Posts'
#
#     def __str__(self):
#         """String representation shown in admin and shell"""
#         return self.title
#
#     def get_absolute_url(self):
#         """Return the URL for this post"""
#         from django.urls import reverse
#         return reverse('portfolio:blog_detail', kwargs={'slug': self.slug})


# No active models yet - you'll add them as you learn more Django!
