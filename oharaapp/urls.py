from django.urls import path
from . import views
from .views import TokutenView
from .views import Tokuten_post_List,Post_success,MypageView
app_name='oharaapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('tokuten/', TokutenView.as_view(), name='tokuten'),
    path('detail/', Tokuten_post_List.as_view(), name='detail'),  
    path('post_success/', Post_success.as_view(), name='post_success'),  
    path('mypage/', MypageView.as_view(), name='mypage'),  
]
