from django.db import models

# Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from datetime import datetime, date





# class Post (models.Model):
#     name = models.CharField( max_length=100 )
#     img = models.ImageField(upload_to='pics')
#     desc = models.TextField()
#     price = models.FloatField() 
#     promo = models.BooleanField(default=False)
#     post_date = models.DateField(auto_now_add=True,blank=True, null=True)
#     itemOwnerContact = models.CharField( max_length=100,default="" )
#     itemOwner = models.CharField( max_length=100,default="" )

#     def __str__(self):
#         return self.name + '|' + str(self.img)

#     def get_absolute_url(self):
#         return reverse("affiliate:index")
# class add_post(models.Model):
#     add_post = models.CharField( max_length=100 )