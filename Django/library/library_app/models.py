# from django.conf import settings
# from django.db import models
# from django.utils import timezone

# Create your models here.

# Book: a model representing a book, with a title, publish date, and an author (foreign key)
# Author: a model representing an author of a book, one author can have multiple books


# class Book(models.Model):
#     title = models.CharField(max_length=200, default='Title Goes Here')
#     publish_date = models.CharField(max_length=200, default='Publication Date Goes Here')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# class Author(models.Model):
#     name = models.CharField(max_length=200, default='Author\'s Name Goes Here')
#     publication_titles = 


#The new model can have the following fields:

# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in

# class Inventory(models.Model):
#     book =
#     user =
#     checkout =
#     timestamp = 

    # created_date = models.DateTimeField(default = timezone.now)
    # completion_date = models.DateTimeField(blank = True, null = True)
    # is_completed = models.BooleanField(default = False)







