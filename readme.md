## Migrations
```
# create migration files
python3 manage.py makemigrations

# run migration files
python3 manage.py migrate 
```

## SQLite in shell
```
# django shell
python3 manage.py shell

# testing sqlite
from bookstore.models import Book
harry_potter = Book(title='HP1', rating=5)
harry_potter.save()
lord_of_the_ring = Book(title='LOTR', rating=8)
lord_of_the_ring.save()

# get all
Book.objects.all()
```

##  On change to db
```
# 1 - Change migrations files
python3 manage.py makemigrations

# 2 - Run migration files
python3 manage.py migrate
```

## Updating value from shell
```
hp = Book.objects.all()[0]
lotr = Book.objects.all()[1]

hp.author = 'JK Rowling'
hp.is_bestselling = True
hp.save()
Book.objects.all()[0].author

lotr.author = 'JRR Tolkien'
lotr.is_bestselling = False
lotr.save()
Book.objects.all()[1].author
```

## Deleting data from shell
```
hp = Book.objects.all()[0]
hp.delete()
```

## Creating entry in sqlite
```
# Two methods, save() and create()

Book.objects.create(title='HP2', rating=6, author='JK Rowling', is_bestselling=True)
Book.objects.create(title='HP3', rating=7, author='JK Rowling', is_bestselling=False)

Book.objects.create(title='Random Book', rating=2, author='Or Ni', is_bestselling=False)
```

## Retrieving entries by field
```
# Retrieving single record
Book.objects.get(id=1)
Book.objects.get(rating=5)

# Retrieving multiple records
Book.objects.filter(author='JK Rowling')
Book.objects.filter(is_bestselling=True, author='JK Rowling')
```

## Retrieving entries with conditional
```
# <, >, >=, =<
Book.objects.filter(rating__lt=8)
Book.objects.filter(rating__lte=7)

# contains vs icontains
Book.objects.filter(rating__lte=7, title__contains="hp")
Book.objects.filter(rating__lte=7, title__icontains="hp")

# or
from django.db.models import Q
Book.objects.filter(Q(rating__lte=7) | Q(title__contains='Tolkien'))
```

## Bulk Operations
- https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects
- https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update
- https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create





