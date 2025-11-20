# What Is an ORM?

ORM means **Object Relational Mapping**.

It is a technique that allows me to interact with a database using **Python code instead of writing raw SQL**.

In simple terms:

ORM connects **Python objects** to **database tables**.

---

# How It Works

Without ORM, I have to write SQL manually:

```sql
SELECT * FROM users WHERE id = 1;
```

With ORM (for example in Django):

```python
User.objects.get(id=1)
```

Both do the same thing, but ORM lets me write it in Python instead of SQL.

---

# Why ORM Exists

ORM makes it possible to:

1. Talk to the database using Python classes and objects
2. Avoid writing long SQL queries
3. Reduce errors
4. Keep my code cleaner and easier to maintain
5. Switch databases easily (e.g., MySQL → PostgreSQL) without rewriting SQL

---

# How ORM Works in Django

In Django, I create a model class:

```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
```

Django will automatically create this table in the database:

```
products table
-------------------------------------
id | name        | price
-------------------------------------
```

Then I can do CRUD operations in Python.

---

# Examples of ORM Usage

## Create data

```python
Product.objects.create(name="Laptop", price=2000)
```

### Read data

```python
Product.objects.all()
Product.objects.get(id=1)
```

### Update data

```python
product = Product.objects.get(id=1)
product.price = 2500
product.save()
```

### Delete data

```python
product = Product.objects.get(id=1)
product.delete()
```

No SQL needed. ORM converts these Python operations into SQL behind the scenes.

---

# Why ORM Is Useful

* I don’t need to know deep SQL to work with databases
* I write less code and avoid mistakes
* My code becomes cleaner and more readable
* One model class controls the whole table
* I can use relationships (ForeignKey, ManyToMany, OneToOne) easily

---

# Summary

ORM is a tool that lets me:

* Work with my database using Python
* Avoid raw SQL
* Create, update, and delete data through Python classes
* Keep my project organized and consistent

---

