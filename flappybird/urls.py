
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Flappybird'),
   # path('download',views.download, name='download'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('flappybird',views.flappybird,name='flappybird')
]

'''
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='OnlineTictac'),
    path('Tictactoe',views.Tictactoe, name='Tictactoe'),
   # path('dashboard',views.dashboard,name='dashboard'),
    #path('products',views.products,name='products')
]'''