from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def account_validator(self, postData):
        errors = {} # creating a dictionary to hold the error messages
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters."
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters."
        if len(postData['username']) < 3:
            errors["username"] = "User name must be at least 3 characters."
        users = self.filter(username=postData['username'])
        if users:
            errors["username"] = "User name already exists."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors["email"] = "E-mail address is NOT valid."
        
        if len(postData['password']) < 4:
            errors["password"] = "Password should be at least 4 characters."
        if postData["password"] != postData["confirmpw"]:
            errors["password"] = "Passwords do NOT match."
        return errors
    
    def loginCheck(self, postData):
        errors = {}
        if not self.filter(username=postData["username"]).exists():
            errors["username"] = "Account does NOT exist."
        else:
            accountpw = self.get(username=postData["username"]).password
            # if not bcrypt.checkpw(postData["password"].encode(), accountpw.encode()):
            #     errors["password"] = "Incorrect password."
        return errors

class ClientManager(models.Manager):
    def client_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['company']) < 3:
            errors["company"] = "Company should be at least 3 characters."
        if len(postData['contactfname']) < 3:
            errors["contactfname"] = "First name should be at least 3 characters."
        if len(postData['contactlname']) < 3:
            errors["contactlname"] = "Last name should be at least 3 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "E-mail address is NOT valid."
        return errors
    
# class JobManager(models.Manager):
#     def job_validator(self, postData):
#         errors = {}
#         # add keys and values to errors dictionary for each invalid field
#         if len(postData['title']) < 3:
#             errors["title"] = "Job title should be at least 3 characters."
#         if len(postData['desc']) < 3:
#             errors["desc"] = "Description should be at least 3 characters."
#         if len(postData['location']) < 3:
#             errors["location"] = "Location should be at least 3 characters."
#         return errors

# class ProjectManager(models.Manager):
#     def project_validator(self, postData):
#         if len(postData['name']) < 3:
#             errors["name"] = "Project name should be at least 3 characters."
    
# class CategoryManager(models.Manager):
#     def category_validator(self, postData):
#         if len(postData['name']) < 3:
#             errors["name"] = "Category name should be at least 3 characters."
    

class User(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # clients
    
class Client(models.Model):
    company = models.CharField(max_length=128)
    contactfname = models.CharField(max_length=128)
    contactlname = models.CharField(max_length=128)
    phone = models.IntegerField()
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    rate = models.FloatField()
    notes = models.TextField()
    users = models.ManyToManyField(User, related_name="clients")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()
    # jobs

class Job(models.Model):
    name =  models.CharField(max_length=128)
    desc = models.TextField()
    date = models.DateField()
    start = models.TimeField()
    stop = models.TimeField()
    duration = models.TimeField()
    client = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = JobManager()
    # projects
    # categories
    
# class Project(models.Model):
#     name = models.CharField(max_length=128)
#     desc = models.CharField(max_length=255)
#     jobs = models.ForeignKey(Job, related_name="projects", on_delete=models.CASCADE)
#     # objects = ProjectManager()
    
# class Category(models.Model):
#     name = models.CharField(max_length=128)
#     desc = models.CharField(max_length=255)
#     jobs = models.ForeignKey(Job, related_name="categories", on_delete=models.CASCADE)
#     # objects = CategoryManager()
    