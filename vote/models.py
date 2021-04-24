from django.db import models
import PIL.Image
from django.contrib.auth.models import User

from django.db.models import PROTECT, CASCADE, SET_NULL


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Candidate(models.Model):
    year = (('pbl1', 'pbl1'), ('pbl1B', 'pbl1B'), ('pbl2', 'pbl2'), ('pbl3', 'pbl3'), ('pbl3B', 'pbl3B'), ('pbl4', 'pbl4'), ('pbl5', 'pbl5'), ('pbl6', 'pbl6'))
#    category=(('President', 'President'), ('Secretary','Secretary'), ('Organizer','Organizer'), ('Treasurer','Treasurer'), ('VicePresident','VicePresident'), ('HealthOfficer', 'HealthOfficer'), ('ExchangeOfficer', 'ExchangeOfficer'))
    SEX = (('m', 'Male'), ('f', 'Female'))
    FirstName = models.CharField(max_length=50, blank=True)
    LastName = models.CharField(max_length=50, blank=True)
    Gender = models.TextField(max_length=6, default='male', choices=SEX)
    Reg_No = models.AutoField(primary_key=True)
    Year = models.CharField(max_length=5, choices=year)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profilePic = models.ImageField(default='profile_pics/candidate.png', upload_to='profile_pics', null=True, blank=True)
    manifesto = models.FileField(upload_to='manifesto', null=True, blank=True)


    def __str__(self):
        return str(self.Reg_No) + " " + self.Category.category + " " + self.LastName
        
    def save(self):
        super().save()
        img=PIL.Image.open(self.profilePic.path)
        if img.height>300 and img.width > 300:
            cropped=(300,300)
            img.thumbnail(cropped)
            img.save(self.profilePic.path)


class Vote(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    President = models.CharField(max_length=50, blank=True)
    Secretary = models.CharField(max_length=50, blank=True)
    Organizer = models.CharField(max_length=50, blank=True)
    Treasurer = models.CharField(max_length=50, blank=True)
    ExchangeOfficer = models.CharField(max_length=50, blank=True)
    HealthOfficer = models.CharField(max_length=50, blank=True)
    VicePresident = models.CharField(max_length=50, blank=True)
    Pro = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.User) + ' ' + 'Voted' 

