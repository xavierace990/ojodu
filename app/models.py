from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.

class FeedBack(models.Model):
    name=models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField(
    max_length=255,  # Maximum length of the email address (adjust as needed)
    unique=True,     # Ensure email addresses are unique in the database
    blank=False,     # Email is required (set to True if it's optional)
    null=False,      # Email is required (set to True if it can be null)
    help_text="Please enter a valid email address",  # Help text for the field
)
    feedback = models.TextField(null=True)

    
class First(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(
    max_length=255,  # Maximum length of the email address (adjust as needed)
    unique=True,     # Ensure email addresses are unique in the database
    blank=False,     # Email is required (set to True if it's optional)
    null=False,      # Email is required (set to True if it can be null)
    help_text="Please enter a valid email address",  # Help text for the field
)
    phone = PhoneNumberField()
    visit_date = models.DateField()  # Add the "date of visit" field
    how_heard = models.CharField(max_length=100)  # Add the "how did you hear about us" field
    comments=models.TextField()

   #blogpost
class Teaching_sermon(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads')
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk}) 