from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    beging_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class card:
        db_table = 'card'