from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    # authors
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# from books_app.models import *
# Book.objects.create(
#     title="C sharp",
#     desc="This is a book about C#"
# )

# Book.objects.create(
#     title="Java",
#     desc="This is a book about Java"
# )

# Book.objects.create(
#     title="Python",
#     desc="This is a book about Python"
# )

# Book.objects.create(
#     title="PHP",
#     desc="This is a book about PHP"
# )

# Book.objects.create(
#     title="Ruby",
#     desc="This is a book about Ruby"
# )

# Author.objects.create(
#     first_name="Jane",
#     last_name="Austen"
# )

# Author.objects.create(
#     first_name="Emily",
#     last_name="Dickinson"
# )

# Author.objects.create(
#     first_name="Fyodor",
#     last_name="Dostoevsky"
# )

# Author.objects.create(
#     first_name="William",
#     last_name="Shakespeare"
# )

# Author.objects.create(
#     first_name="Lau",
#     last_name="Tzu"
# )

# c = Book.objects.get(id=1)
# c.title = "C#"
# c.save()

# c = Author.objects.get(id=4)
# c.first_name = "Bill"
# c.save()

# auth1 = Author.objects.get(id=1)

# book1 = Book.objects.get(id=1)

# book2 = Book.objects.get(id=2)

# book1.authors.add(auth1)

# book2.authors.add(auth1)

# auth2 = Author.objects.get(id=2)

# book3 = Book.objects.get(id=3)

# book1.authors.add(auth2)

# book2.authors.add(auth2)

# book3.authors.add(auth2)

# auth3 = Author.objects.get(id=3)

# book4 = Book.objects.get(id=4)

# book1.authors.add(auth3)

# book2.authors.add(auth3)

# book3.authors.add(auth3)

# book4.authors.add(auth3)

# auth4 = Author.objects.get(id=4)

# book5 = Book.objects.get(id=5)

# book1.authors.add(auth4)

# book2.authors.add(auth4)

# book3.authors.add(auth4)

# book4.authors.add(auth4)

# book5.authors.add(auth4)

# book3.authors.all()

# book3.authors.remove(auth2)

# auth5 = Author.objects.get(id=5)

# book2.authors.add(auth5)

# auth3.books.all()

# book5.authors.all()
