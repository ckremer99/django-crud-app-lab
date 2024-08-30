from django.urls import path
from . import views

urlpatterns = [
   path('animals/', views.index, name="animal-index"),
   path('animals/<int:animal_id>/', views.animal_detail, name='animal-detail'),
   path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
   path('animal/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal-update'),
   path('animal/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal-delete'),
   path('animals/<int:animal_id>/add-feeding', views.add_feeding, name='add-feeding'),
   path('', views.Home.as_view(), name='home'),
   path('accounts/signup/', views.signup, name='signup'), 
]
