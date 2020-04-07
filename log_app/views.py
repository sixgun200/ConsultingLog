from django.shortcuts import render, redirect, HttpResponse
from .models import User, Client, Job #Project, Category
from django.contrib import messages
import bcrypt

def login(request):
    return render(request, "login.html")

def register(request):  
    return render(request, "register.html")

def registerUser(request):
    if request.method == "POST":
        errors = User.objects.account_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags="register")
            return redirect("/c_log/register")
        else:
            username = request.POST["username"]
            userfname = request.POST["fname"]
            userlname = request.POST["lname"]
            useremail = request.POST["email"]
            userpw = request.POST["password"]
            pw_hash = bcrypt.hashpw(userpw.encode(), bcrypt.gensalt()).decode()
            # print("*"*200,pw_hash)
            #CREATE the new user in the database AND assign it to a variable for use later
            user = User.objects.create(username=username, fname=userfname, lname=userlname, email=useremail, password=pw_hash)
            #CREATE a key in the session dictionary called "userid" with a value of the ID of the user from the database
            request.session["userid"] = user.id
            # messages.success(request, "Successfully registered!")
            return redirect("/c_log/main")

def authenticate(request):
    if request.method == "POST":
        errors = User.objects.loginCheck(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags="login")
            return redirect("/c_log/login")
        else:
            login = User.objects.get(username=request.POST["username"])
            # context = {
            #     "user": login
            # }
            #CREATE a key in the session dictionary called "userid" with a value of the ID of the user from the database
            request.session["userid"] = login.id
            # messages.success(request, "Successfully logged in!")
            return redirect("/c_log/main")


def main(request):
    context = {
        "allJobs": Job.objects.all(),
        "user": User.objects.get(id=request.session["userid"]),
    }
    return render(request, "main.html", context)

def logout(request):
    request.session.clear()
    return redirect("/c_log/login")

def startTimer(request):
    pass

def stopTimer(request):
    pass

def addJob(request):
    context = {
        "user": request.session["userid"],
        "clients": Client.objects.all(),
    }
    return render(request, "newjob.html", context)

def createJob(request):
    if request.method=="POST":
        errors = Job.objects.job_validator(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/jobs/new")
        else:
            jobclientid = request.POST["clientid"]
            jobname = request.POST["name"]
            jobdesc = request.POST["desc"]
            jobdate = request.POST["date"]
            jobstart = request.POST["start"]
            jobstop = request.POST["stop"]
            jobduration = request.POST["duration"]
            # jobcat = request.POST["category"]
            # jobproject = request.POST["projects"]
            user = User.objects.get(id=request.session["userid"])
            #CREATE the new job in the database AND assign it to a variable for use later
            job = Job.objects.create(name=jobname, desc=jobdesc, date=jobdate, start=jobstart, stop=jobstop, duration=jobduration, client=jobclientid, created_by= user)
            #CREATE a key in the session dictionary called "helperid" with a value of the ID of the helper from the database
            return redirect("/c_log/main")
    return redirect("/c_log/main")
    
def editJob(request, jobid):
    pass
    # context = {
    #     "user": User.models.get(id=request.session["userid"])
    # }
    # context = {
    # }
    # return render(request, "editjob.html", context)

def updateJob(request):
    # if request.method == "POST":
    pass

def addClient(request):
    context = {
        "user": User.objects.get(id=request.session["userid"])
    }
    return render(request, "addclient.html", context)

def createClient(request):
    pass

def editClient(request):
    pass

def updateClient(request):
    pass

def editProject(request):
    pass

def updateProject(request):
    pass

def editCategory(request):
    pass

def updateCategory(request):
    pass

def deleteJob(request):
    pass

def deleteClient(request):
    pass

def deleteProject(request):
    pass

def deleteCategory(request):
    pass

