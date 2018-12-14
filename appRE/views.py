
from django.shortcuts import render
from .models import UserRegister, State , City


# Create your views here.
def openHomePage(request):
    type = "h_User_register"
    return render(request, "index.html", {"type": type})

def openUserLogin(request):
    try:
        sessions = request.session['email']
        if sessions != '':
            token = UserRegister.objects.get(email_id=sessions)
            return render(request,"uwelcome.html",{'udetails':token,"type":"u_home"})
        else:
            type = request.GET.get("type")
            return render(request,"index.html",{"type":type})
    except:
        type = request.GET.get("type")
        return render(request, "index.html", {"type": type})
def openUserRegister(request):
    type = request.GET.get("type")
    res = State.objects.values('name')
    states = ["State"]
    for x in res:
        states.append(x["name"])

    return render(request, "index.html", {"type": type,"states":states})

# def getCityFromState(request):
#     sel_state = request.GET.get("state")
#     res = State.objects.values('id_no').filter(name=sel_state)
#     id_no = 0
#     for x in res:
#         id_no = x["id_no"]
#     res1 = City.objects.values('c_name').filter(s_name=id_no)
#     city_names = ["City"]
#     if not res1:
#         city_names = ["No City Available"]
#     else:
#         for x in res1:
#             city_names.append(x['c_name'])
#
#     res2 = State.objects.values('name')
#     states = ["State"]
#     for x in res2:
#         states.append(x["name"])
#
#     return render(request, "index.html", {"type": 'h_user_register',"city_names":city_names,"states":sel_state,"key":"one"})

def registerUser(request):
    u_name = request.POST.get('u_name')
    u_cno = request.POST.get('u_cno')
    u_email = request.POST.get('u_email')
    u_pass = request.POST.get('u_pass')
    u_age = request.POST.get('u_age')
    u_gender = request.POST.get('u_gender')
    u_occup = request.POST.get('u_occup')
    u_salary = request.POST.get('u_salary')


    user = UserRegister(name=u_name,contact_no=u_cno,email_id=u_email,password=u_pass,age=u_age,gender=u_gender,occupation=u_occup,salary=u_salary)
    user.save()
    return render(request,"index.html",{"type":'h_User_register',"message":"Registered",})

def checkUserLogin(request):
    uname=request.POST.get('uname')
    upass=request.POST.get('psw')
    try:
        ul=UserRegister.objects.get(email_id=uname,password=upass)
        if ul:
            sess = request.session['email']=uname
            return render(request,"uwelcome.html",{"udetails":ul,"type":"u_home"})
        else:
            return render(request,"index.html",{"type":'h_user',"message1":"Invalid Details"},)
    except:
        return render(request, "index.html", {"type": 'h_user', "message1": "Invalid Details"}, )


def checkProfile(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('psw')
    try:

        ul = UserRegister.objects.filter(email_id=uname, password=upass)
        if ul:
            return render(request, "uwelcome.html", {"udetails": ul,"type":"u_home"})
        else:
            return render(request, "index.html", {"type": 'h_user', "message": "Invalid Details"})
    except:
        return render(request, "index.html", {"type": 'h_user', "message": "Invalid Details"})


def UserLogout(request):
    logout = request.session['email']=''
    return render(request,"index.html",{"type":'h_User_register'})


def updateProfile(request):
    email = request.GET.get('email')
    update = UserRegister.objects.get(email_id=email)
    return render(request,"uwelcome.html",{'udetails':update,"type":"userupdate"})


def updatesave(request):
    u_name = request.POST.get('name')
    u_cno = request.POST.get('cno')
    u_email = request.POST.get('email')
    u_pass = request.POST.get('pass')
    u_age = request.POST.get('age')
    u_gender = request.POST.get('gender')
    u_occup = request.POST.get('occup')
    u_salary = request.POST.get('salary')

    UserRegister.objects.filter(email_id=u_email).update(name=u_name, contact_no=u_cno, password=u_pass, age=u_age, gender=u_gender,
                           occupation=u_occup, salary=u_salary)

    update1=UserRegister.objects.get(email_id=u_email)
    return render(request,'uwelcome.html',{'udetails':update1,"type":"u_home"})


def addproperties(request):
    email=request.GET.get('email')
    res=UserRegister.objects.get(email_id=email)
    from  .models import property
    prodetails=property.objects.filter(Customer_Email=email)
    return render(request,"uwelcome.html",{"type":"add_property","udetails":res,"prodetails":prodetails})


def upropertysave(request):
    name=request.POST['name']
    state=request.POST['state']
    price=request.POST['price']
    city=request.POST['city']
    locality=request.POST['locality']
    pin=request.POST['pin']
    email=request.POST['uemail']
    res=UserRegister.objects.get(email_id=email)
    from  .models import property
    property(state=state,city=city,locality=locality,price=price,pincode=pin,Customer_Name=res.name,contact_number=res.contact_no,Customer_Email=email,name=name).save()
    prodetails=property.objects.filter(Customer_Email=email)
    return render(request,"uwelcome.html",{"type":"add_property","udetails":res,"message":"Property Added Successfully","prodetails":prodetails})