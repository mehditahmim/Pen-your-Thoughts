from django.urls import path, include
from . import views
app_name = 'userprofile'

urlpatterns = [
    path('<username>/', views.profileView, name='profileView'),
    path('<username>/<title>/', views.postView, name='postView'),

]
