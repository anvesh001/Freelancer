from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to = 'assets/images',
        blank=True
    )
    #exper_choice= [(i,i) for i in range(11)]
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='none@email.com')
    birth_date = models.DateField(default='1999-12-31')
    bio = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    favorite_animal = models.CharField(max_length=255, default='')
    hobby = models.CharField(max_length=255, default='')
    qualification=models.CharField(max_length=255, default='')
    keywords=models.CharField(max_length=255,default='')
    area_of_experince=models.TextField(default='')
    price=models.PositiveSmallIntegerField(default=0)
    experince=models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))), default=0)
    cover = models.ImageField(upload_to='asset/',default="/asset/images.png")
    #message=models.CharField(max_length=255, default='hai')
    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
