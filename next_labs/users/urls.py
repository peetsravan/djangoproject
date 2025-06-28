from django.urls import path
from .views import register,login_page,logout_page,admin_home,user_home,add_app,review_screenshots,approve_screenshot,submit_task,profile_page

urlpatterns =[
    path('',login_page,name='login_page'),
    path('register/',register,name='register'),
    path('logout/',logout_page,name='logout'),
    path('admin_home/',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('add_app/', add_app, name='add_app'),
    path('review-screenshots/', review_screenshots, name='review_screenshots'),
    path('approve-screenshot/<int:task_id>/', approve_screenshot, name='approve_screenshot'),
    path('submit-task/', submit_task, name='submit_task'),
    path('profile/', profile_page, name='profile'),
]