from django.urls import path,include
from myapp import views


urlpatterns = [
    path('dashboard/', views.DashBoardPage.as_view(), name='dashboard'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('oauth/', include('social_django.urls')),
]
