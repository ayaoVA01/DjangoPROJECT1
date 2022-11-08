from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
  
    path('',views.p,name='p_page'),
    path('base/',views.base, name = 'base_page'),
#system sigup
    path('login/',views.login,name='login_page'),
    path('signup/',views.signup,name='signup_page'),
    path('addUser/',views.signUpfrom, name='addUser_page'),
    path('User/',views.logInform, name='User_page'),


    path('imformation/',views.imformation, name='imformation_page'),
    path('logout/',views.logout, name='logout_page'),
    # path('addinfomation/',views.addUser
    path('useImformation/',views.imformationForm, name='useImformationform'),

    path('home/',login_required(views.home, login_url='/login'),name='home_page'),
    path('pos/',login_required(views.pos, login_url='/login'),name='post_page'),
    path('setting/',login_required(views.setting, login_url='/login'),name='setting_page'),
    path('status/',login_required(views.status, login_url='/login'),name='status1_page'),
    path('call/',login_required(views.call, login_url='/login'),name='call1_page'),
    path('calling/',login_required(views.calling, login_url='/login'),name='calling_page'),
    path('callvideo/',login_required(views.callvideo, login_url='/login'),name='callvideo_page'),
    path('song/',login_required(views.song, login_url='/login'),name='song_page'),
    path('group/',login_required(views.group, login_url='/login'),name='group_page'),
    path('friends/',login_required(views.friends, login_url='/login'),name='friends_page'),
  

]