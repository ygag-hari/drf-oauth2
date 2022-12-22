from django.contrib import admin
from django.urls import path, include
from mysite.views import (
    UserDetails, UserList, GroupList
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]


# 3pJjlRAAwLBOxDFWZXT5dcGev0F9TXF1gl0DtzzR
# Wu2FksYScdFxtHxXCVZWm3CrBVV9J4HN7yYOU8z9Owcvqy2x3hrGW6vA3sT0SnmkGh7rFATJQF5hNIP1DdpDUqWv0iIkEjIgPdxnT4ELfU0OZ5mUfBazeY30PBRiCndY