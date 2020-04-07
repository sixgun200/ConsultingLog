from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login), #RENDER
    path('register', views.register), #RENDER
    path('authenticate', views.authenticate), #redirect to MAIN
    path('registeruser', views.registerUser), #redirect to MAIN
    path('logout', views.logout),
    path('main', views.main), #RENDER
    path('start', views.startTimer), #redirect to MAIN
    path('stop', views.stopTimer), #redirect to MAIN
    path('job/new', views.addJob), #redirect to EDITJOB
    path('job/create', views.createJob),
    path('job/edit/<int:jobid>', views.editJob), #RENDER, combine add and edit in the same screen
    path('job/edit/update/<int:jobid>', views.updateJob), #redirect to MAIN screen, add or edit to the datebase as required
    path('job/delete/<int:jobid>', views.deleteJob), #redirect to MAIN
    path('client/new', views.addClient), #redirect to EDITJOB
    path('client/create', views.createClient),
    path('client/edit/<int:clientid>', views.editClient), #RENDER, combine add and edit in the same screen
    path('client/edit/update/<int:clientid>', views.updateClient), #redirect to JOB EDIT screen, add or edit to the datebase as required
    path('client/delete/<int:clientid>', views.deleteClient), #redirect to JOB EDIT screen
    # path('project/new', views.addProject), #redirect to EDITJOB
    # path('project/create', views.createProject),
    # path('project/edit/<int:projectid>', views.editProject), #RENDER, combine add and edit in the same screen
    # path('project/edit/update/<int:projectid>', views.updateProject), #redirect to the JOB EDIT screen, add or edit to the datebase as required
    # path('project/delete/<int:projectid>', views.deleteProject), #redirect to JOB EDIT screen
    # path('category/new', views.addCategory), #redirect to EDITJOB
    # path('category/create', views.createCategory),
    # path('category/edit/<int:projectid>', views.editCategory), #RENDER, combine add and edit in the same screen
    # path('category/edit/update/<int:projectid>', views.updateCategory), #redirect to the JOB EDIT screen, add or edit to the datebase as required
    # path('category/delete/<int:projectid>', views.deleteCategory), #redirect to JOB EDIT screen
]