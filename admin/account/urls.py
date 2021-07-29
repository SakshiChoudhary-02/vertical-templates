from django.urls import path
from . import views

urlpatterns = [

    path('', views.create, name='create'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('userdetail/', views.UserDetail.as_view(), name='user-detail'),
    path('card/', views.Card.as_view(), name='card'),
    # path('carddetail/', views.CardDetail.as_view(), name='card-detail'),
    path('int:pk/', views.CardDetail.as_view(), name='card-detail'),
    path('addcard/', views.AddCard.as_view(), name='add-card'),
    path('editcard/int:pk/', views.EditCard.as_view(), name='edit-card'),
    path('deletecard/', views.DeleteCard.as_view(), name='delete-card'),

]

