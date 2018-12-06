
from django.shortcuts import render
from .models import UserRegister, State , City


# Create your views here.
def openHomePage(request):
    type = "h_User_register"
    return render(request, "index.html", {"type": type})

def openUserLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})

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

    user = UserRegister(name=u_name,contact_no=u_cno,email_id=u_email,password=u_pass)
    user.save()
    return render(request,"index.html",{"type":'h_User_register',"message":"Registered",})

def checkUserLogin(request):
    uname=request.POST.get('uname')
    upass=request.POST.get('psw')
    ul=UserRegister.objects.filter(email_id=uname,password=upass)
    if ul:
        return render(request,"uwelcome.html",{"udetails":ul})
    else:
        return render(request,"index.html",{"type":'h_user',"message":"Invalid Details"})

def checkProfile(request):
    uname = request.POST.get('uname')
    upass = request.POST.get('psw')
    ul = UserRegister.objects.filter(email_id=uname, password=upass)
    if ul:
        return render(request, "uwelcome.html", {"udetails": ul})
    else:
        return render(request, "index.html", {"type": 'h_user', "message": "Invalid Details"})