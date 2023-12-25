from django.urls import path, include

from comment_app.api.views.router import api_router

urlpatterns = [
    path('api/', include(api_router.urls)),
]
