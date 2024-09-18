from django.contrib import admin
from django.urls import path
from login_with_otp import views

# username: raj and password: raja
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('accounts/login/', views.login_view, name='login'),  # Updated path
    path('logout/', views.logout_view, name='logout'),
    path('otp/', views.otp_view, name='otp'),
]
