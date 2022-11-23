from django.urls import path
from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('signup/', RegisterView ),
    path('signin/', LoginView ),
    path('logout/', LogoutView)
]
