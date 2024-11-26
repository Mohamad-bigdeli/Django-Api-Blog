from django.urls import path
from .. import views
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    # test email send
    path("test-email/", views.TestEmailSend.as_view(), name="test-email"),
    # activision
    path("activision/confirm/<str:token>/", views.ActivisionApiView.as_view(), name="activision"),
    # resend activision
    path("activision/resend/", views.ActivisionResendApiView, name="activision-resend"),
    # change password
    path("change-password/", views.ChangePasswordApiView.as_view(), name="change-password"),
    # reset password
    # login token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    # logout token
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # login jwt
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    ] 