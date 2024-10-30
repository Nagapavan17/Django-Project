from django.urls import path
from Main import views

#paths

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_reg,name='login'),
    path('register',views.emp_reg,name='emp_register'),
    path('Employee',views.Empl_reg,name='Employee'),
    path('index',views.index,name='index'),
    path('about',views.About,name='about'),
    path('logistic',views.Logistic,name='logistic'),
    path('contact',views.Contact,name='contact'),
    path('logout1',views.logoutemployee,name='logout1'),
    path('logout2',views.logoutUser,name='logout2'),
]