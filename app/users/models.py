from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User
from django.utils import timezone
import uuid
# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        organization = self.model(email=email, **extra_fields)
        organization.set_password(password)
        organization.save(using=self._db)
        return organization

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    tc = models.BooleanField(null=True,blank=True,default=False)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Student(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    organization = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False,blank=False,default="abc@gmail.com")
    password = models.CharField(max_length=10,blank=False,null=False)

class StudentAuthentication(models.Model):
    student = models.OneToOneField(UserModel, on_delete=models.CASCADE)

class Feedback(models.Model):
    experience = models.CharField(max_length=50,blank=True,null=True)
    feedback = models.CharField(max_length=300,blank=True,null=True)