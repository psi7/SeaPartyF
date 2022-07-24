from pickle import TRUE
from django.db import models
from django.forms import CharField
# Create your models here.
class SubCategory(models.Model):
    SubCategories = [
        ('VIP', 'VIP'),
        ('Expensive', 'Exp'),
        ('Cheap', 'chp'),
        ('Free', 'Fr'),
    ]
    SubCategory_name=models.CharField(max_length=15,choices=SubCategories,primary_key=True)
    def __str__(self):
        return f"{self.SubCategory_name} "
class Category(models.Model):
    Categories = [
        ('Family', 'Fam'),
        ('Couple', 'Cpl'),
        ('Solo', 'Sol'),
        ('Children', 'Kid'),
    ]
    Category_name=models.CharField(max_length=15,choices=Categories,primary_key=True)
    SubCategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="SubCategory")
    def __str__(self):
        return f"{self.Category_name} ({self.SubCategory})  "

class Location(models.Model):
    Region_CHOICES = [
        ('Europe', 'Eu'),
        ('Asia', 'As'),
        ('Oceania', 'Oce'),
        ('Africa', 'Afr'),
        ('N.America', 'NAm'),
        ('S.America','SAm'),
    ]
    Location_name = models.CharField(max_length=30, primary_key=True)
    Country= models.CharField(max_length=20)
    Region = models.CharField(max_length=15,choices=Region_CHOICES,blank=True)
    NumberofEvents = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.Location_name} ({self.Country})  ({self.Region})  ({self.NumberofEvents})"

class Events(models.Model):
    Event_Id = models.IntegerField(primary_key=TRUE,)
    Event_Name = models.CharField(max_length=30)
    Event_Cost = models.DecimalField(default=0, decimal_places=2,max_digits=4)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="Event_Category")
    Date = models.DateField(blank=True)
    Capacity= models.IntegerField(default=30)
    CurrentCapacity= models.IntegerField(default=0)
    Event_location= models.ForeignKey(Location, on_delete=models.CASCADE, related_name="Event_Location")
    Event_image = models.ImageField()

     
    def __str__(self):
        return f"{self.Event_Id} {self.Event_Name} ({self.Event_Cost}) ({self.Category}) ({self.Date})  ({self.Capacity}) ({self.CurrentCapacity})  ({self.Event_location})"

class Users(models.Model):
     user_id = models.IntegerField(primary_key=TRUE,)
     first = models.CharField(max_length=64, default='Unknown')
     last = models.CharField(max_length=64,default='Unknown')
     Age = models.IntegerField()
     events = models.ManyToManyField(Events, blank=True, related_name="registered_users")
     phone = models.IntegerField(default=000)
     mail= models.EmailField(default='@')
     admin_status = models.BooleanField(default=False)

     def __str__(self):
        return f"{self.user_id} {self.first} ({self.last})  ({self.Age})  ({self.events})  ({self.phone})  ({self.mail})  ({self.admin_status})"
    





