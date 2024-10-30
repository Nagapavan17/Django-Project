from django.shortcuts import render,redirect
from .models import Employee 
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,logout,login
from .forms import EmpRegisterForm
from django.contrib import messages

# Create your views here.
app_name='Main'

def home(request):
    return render(request,'home.html')

@login_required(login_url ='login')
def index(request):
    employees=Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def About(request):
    return render(request,'About.html')

@login_required(login_url='login')
def Logistic(request):
    return render(request,'Logistics.html')

def Contact(request):
    return render(request,'contact.html')
def emp_reg(request):
    if request.method=='GET':
        return render(request,'Emp_reg.html')
    else: 
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        user=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password=make_password(password)
        customer=[fn,ln,user,email,password]
        print(customer)
        #validation
        error_msg=None
        sucess_msg=None
        #if(not fn):
            #error_msg="First Name should not be empty"
        ##elif(not ln):
            #error_msg="First Name should not be empty"
       # elif(not user):
           # error_msg="Use Name should not be empty"
        #elif(not email):
            #error_msg="Email should not be empty"
        #elif(not password):
            #error_msg="Password is Required"         
        
        #msg={'error':error_msg,'sucess':sucess_msg}

        emp_data=Employee(firstname=fn,lastname=ln,username=user,email=email,password=password)
        if(emp_data.isexist()):
            error_msg="Email is already Exists"
        if(not error_msg):
            emp_data.save()
            sucess_msg='Account Created Sucessfully '
            return redirect('login')
        
        msg={'error':error_msg,'success':sucess_msg}
        return render(request,'Emp_reg.html',msg)

def login_reg(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username1=request.POST['username']
        password1=request.POST['password']
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('about')

        users=Employee.isuser(username1)
        error_msg=None
        if users:
            check=check_password(password1,users.password)
            if check:
                return redirect('about')
            else:
                error_msg="Password is incorrect"
                msg={'error':error_msg}
                return render(request,'login.html',msg)
        else:
            error_msg="User Not Found"
            msg={'error':error_msg}
            return render(request,'login.html',msg)
        
def Empl_reg(request):
    error_msg=None
    if request.method=='POST':
        form=EmpRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully !')
            return redirect('login')
        else:
            error_msg='Entered Details not reach the requirements !'
            form=EmpRegisterForm()
            return render(request,'Employee.html',{'form':form,'error':error_msg})
    else:
        error_msg='Dear Employee Please Register with Company mail : '
        form=EmpRegisterForm()
        return render(request,'Employee.html',{'form':form,'error':error_msg})

def logoutemployee(request):
    return redirect('login')

def logoutUser(request):
    logout(request)
    return redirect('Employee')
