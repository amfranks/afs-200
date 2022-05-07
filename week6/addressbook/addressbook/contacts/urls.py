from django.urls import path
from . import views

add_name = "contact"

urlpatterns = [
    
    path('', views.show_all_contacts ),
    path('<int:contactid>',  views.show_contact ),    

]