
from django.urls import path

from protfolio import views


urlpatterns = [
    path('', views.protfolio  )
    # path('home/', views.home, name="home")
]