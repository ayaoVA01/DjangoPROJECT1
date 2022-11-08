
from django.shortcuts import render,redirect

from chat_app.models import Chat, Status,Post


from django.contrib import messages,auth

from app.models import CustomUser

# Create your views here.

def p(request):
    return render(request,'before/p.html')

def imformation(request):
    return render(request,'login/imformation.html')


def pos (request):
    post = Post.objects.all().order_by('-pk')
    chat = Chat.objects.all()
    return render(request, 'webfile/post.html',
    {
    'post':post,
    'chat_post':chat
    })
def home(request):
 
    chat = Chat.objects.all()
    # categ_id = request.GET.get('categoryid')
    # if categ_id:
    #     chat = chat.filter(categoryid =categ_id )
    context = {
    "chats":chat,}
    return render(request,'webfile/index.html',context )

   
def status(request):
    satus=Status.objects.all().order_by('-pk')
    return render(request,'appfile/status.html',
    {'status':satus,})
   

def base(request):
    return render(request,'base.html',{
    })

def call(request):
    return render(request,'appfile/call.html')
def calling(request):
    return render(request,'appfile/calling.html')
def callvideo(request):
    return render(request,'appfile/callvideo.html')

def song(request):
    return render(request,'webfile/song.html')
def group(request):
    chatt = Chat.objects.all()
    return render(request,'appfile/grou.html',
    {'chat_friends':chatt})
def friends(request):
    return render(request,'webfile/friends.html')
def login (request):
    return render(request, 'login/login.html')
def signup (request):
    return render(request, 'login/signup.html')
def setting (request):
    return render(request, 'appfile/setting.html')



  

# system's functions 

def addUser(request):
    username = request.POST['username']
    email= request.POST['email']
    password = request.POST['password']
    repassword   = request.POST['repassword']

    
    if password == repassword:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request,'this araaaaaaaaaaaaaa')
            return redirect('/signup')
        elif CustomUser.objects.filter(email = email).exists():
            messages.info(request,"This EMAIL is aready exists! ")
        else:
            new_user = CustomUser(
                username=username,
                email = email,
                password=password,
                user_type=2),         
        new_user.save()
        return redirect('/login')
    else:
        messages.info(request, 'The password do not match! ')
        return redirect('/signup')


def signUpfrom(request):
    username = request.POST['username']
    email= request.POST['email']
    password = request.POST['password']
    repassword   = request.POST['repassword']

    if password == repassword:
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'This username is already exist!')
            return redirect('/signup')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is already exist!')
            return redirect('/signup')
        else:
           new_user = CustomUser.objects.create_user(
                username=username,
                email = email,
                password = password,
             
                user_type=2,
            )
        new_user.save()
        return redirect('/login')
    else:
        messages.info(request, 'the password do not match')
        return redirect('/signup')

def logInform(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username = username, password = password)
    if user is not None:
        auth.login(request,user)
        if user.user_type =="1":
            return redirect('/admin')
        if user.user_type =='2':
            return redirect('/imformation')
    else:
        messages.info(request, 'Not found !')
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect("/")



# def imformationForm(request):
#     firstname = request.POST['firstname']
#     lastname = request.POST['lastname']
#     phone_number = request.POST['phone_number']
#     date = request.POST['date']
#     age = request.POST['age']
#     profile_picture = request.POST['profile_picture']
#     user = auth.authenticate(first_name=firstname,
#                 last_name=lastname,
#                 phone_number=phone_number,
#                 date=date,
#                 age=age,
#                 profile_picture =profile_picture,)
#     if user != None:
#         auth.login(request,user)
#         return redirect('/pos')
#     else:
#         return redirect('/imformation')


def imformationForm(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    phone_number = request.POST.get('phone_number')
    date = request.POST.get('date')
    age = request.POST.get('age')
    profile_picture = request.POST.get('profile_picture')
    if request.method =='POST':
        if CustomUser.objects.filter(first_name=firstname).exists():
            return redirect('/imformation')
        elif CustomUser.objects.filter(last_name = lastname).exists():
             return redirect('/imformation')
        else:
            new = CustomUser(
                first_name=firstname,
                last_name=lastname,
                phone_number=phone_number,
                date=date,
                age=age,
                profile_picture =profile_picture
            )
  
        return redirect('/pos')
    else:
        return redirect('/imformation')
 

        

   
