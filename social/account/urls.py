from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",views.Login,name="Login"),
    path("signup/",views.Signup,name="signup"),
    path("account/",views.Account,name="Display")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)