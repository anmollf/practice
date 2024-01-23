from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import accCreate
from .views import accDetails
from . import views

urlpatterns = [
    path("",views.Login,name="Login"),
    # path("signup/",views.Signup,name="signup")
    path("signup/",accCreate.as_view(),name = "signup"),
    # path("account/",views.Account,name="Display")
    path("account/<pk>/",accDetails.as_view(),name="Display"),
    path("accounts/",views.getList,name="DisplayAll")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)