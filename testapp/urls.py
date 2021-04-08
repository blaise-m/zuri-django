from django.urls import path, include
from testapp.views import index


urlpatterns = [
	path('', index, name="index"),
]