from django.urls import path

from accounts.views import sign_up, logout_user, sign_in

app_name = "accounts"

urlpatterns = [
    path('sign-up/', sign_up, name="sign_up"),
    path('sign-in', sign_in, name="sign_in"),
    path('logout/', logout_user, name="logout")
]
