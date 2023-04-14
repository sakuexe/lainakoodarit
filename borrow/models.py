from django.db import models
import datetime

# Create your models here.


class Product(models.Model):
    # NON NULLABLE values - must be filled
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    amount = models.SmallIntegerField(default=0)
    descrtiption = models.CharField(max_length=250)
    release_date = models.DateField(default=datetime.date.today)
    loaned_amount = models.SmallIntegerField(default=0)
    author = models.ManyToManyField("Author")
    # NULLABLE fields - can be left empty
    genre = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    # we could use a randomly chosen thumbnail for if there is no image provided
    thumbnail_path = models.CharField(max_length=50)
    # category
    # purchase_event

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    works = models.ManyToManyField("Product", related_name='authors') 
    author_name = models.CharField(max_length = 50)
    home_country = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ["author_name"]

    def __str__(self):
        return self.author_name

class User(models.Model):
    username = models.CharField(max_length=20)
    #Hashing is not done here as we remember
    password = models.CharField(max_length=25)
    real_name = models.CharField(max_length=50)
    is_active = models.BooleanField()
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username

class Event(models.Model):
  # constants 
    loaned_state = "Loaned"
    returned_state = "Returned"
    late_state = "Late"
    # first value is what is set as value and latter is the value that is readable
    # might try subclass enum later, lets try this first
    STATE_CHOICES = [
            (loaned_state, "Loan"),
            (returned_state, "Return"),
            (late_state, "Late"),
            ]

    state = models.CharField(
            max_length=10,
            choices=STATE_CHOICES,
            default=loaned_state,
            )
    
    user_id = models.SmallIntegerField()
    product_id = models.SmallIntegerField()
    loaned_date = models.DateField(default=datetime.date.today)
    is_returned = models.BooleanField(default=False)

    current_time = datetime.datetime.now()
    last_update = models.CharField(default=current_time.strftime("%Y/%m/%d %H:%M:%S"), editable=False, max_length=30)

    class Meta:
        ordering = ["last_update"]

    def __str__(self):
        return f'event: {self.state}, user_id: {self.user_id}, last update: {self.last_update}'
