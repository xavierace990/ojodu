from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index ,name='index'),
    path('feedback/',views.feedback ,name='feedback'),
    path('ourministries/',views.ourministries ,name='ourministries'),
    path('about/',views.about ,name='about'),
    path('livestream/',views.livestream ,name='livestream'),
    path('preacher/',views.preacher ,name='preacher'),
    path('teaching/',views.teaching ,name='teaching'),
    path('success/',views.success ,name='success'),
    path('bulletins/',views.bulletins, name='bulletins'),
    path('donate/',views.donate ,name='donate'),
    path('teaching_sermon/',views.teaching_sermon,name='teaching_sermon'),
    path('<int:pk>/',views.teaching_details ,name='teaching_details'),
    path('heaven_and_hell/',views.heaven_and_hell ,name='heaven_and_hell'),
    path('social_vices/',views.social_vices  ,name='social_vices'),
    path('joy_of_the_lord/',views.joy_of_the_lord,name='joy_of_the_lord'),
    path('couples_cooperation/',views.couples_cooperation,name='couples_cooperation'),
    path('first/',views.first,name='first'),
    path('january/', views.january, name='january'),
    path('february/', views.february, name='february'),
    path('march/', views.march, name='march'),
    path('april/', views.april, name='april'),
    path('may/', views.may, name='may'),
    path('june/', views.june, name='june'),
    path('july/', views.july, name='july'),
    path('august/', views.august, name='august'),
    path('september/', views.september, name='september'),
    path('october/', views.october, name='october'),
    path('november/', views.november, name='november'),
    path('december/', views.december, name='december'),
   
    

    #jan to Dec
    path('jan/', views.jan, name='jan'),
    path('feb/', views.feb, name='feb'),
    path('mar/', views.mar, name='mar'),
    path('apr/', views.apr, name='apr'),
    path('may_b/', views.may_b, name='may_b'),
    path('jun/', views.jun, name='jun'),
    path('jul/', views.jul, name='jul'),
    path('aug/', views.aug, name='aug'),
    path('sep/', views.sep, name='sep'),
    path('oct/', views.oct, name='oct'),
    path('nov/', views.nov, name='nov'),
    path('dec/', views.dec, name='dec'),
    path('feb/', views.feb, name='feb'),
]



