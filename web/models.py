from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user
    def create_superuser(self,email,password=None,**extra_fields):

        if not email:
            raise ValueError('User must have a email')
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff   = True
        user.save(using=self._db)
        return user


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone =models.CharField(max_length=50)  
    password=  models.CharField(max_length=50)



class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD='email'


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    duration =models.IntegerField()
    image = models.FileField(upload_to='ProductImage', null=True, blank=True)
    endingdate = models.DateField(blank=True, null=True)
    startingdate= models.DateField(auto_now=True)
    status=models.CharField(max_length=30,default='On Going')
    @property
    def lifespan(self):
        return '%s - present' % self.endingdate.strftime('%m/%d/%Y')


class BidProduct(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    price = models.IntegerField()
    addeddate= models.DateField(auto_now_add=True)