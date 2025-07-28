from django.contrib import admin
from django.urls import path, include
from authenticationApis import views as auth_view
from rest_framework_simplejwt.views import TokenRefreshView
from smApp import views as smApp_view


urlpatterns = [
    path("admin/", admin.site.urls),  # Admin panel
    path( "api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # REST framework login
    # Authentication APIs
    path("api/register/", auth_view.register_user, name="register"),  # api/register/?with_role=devtr for set role
    path("api/login/", auth_view.login_user, name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/update-role/", auth_view.update_user_role, name="update_role"),
    path("api/change-password/", auth_view.change_password, name="change_password"),
    path("api/forgot-password/", auth_view.forgot_password, name="forgot_password"),
    path("api/reset-password/", auth_view.reset_password, name="reset_password"),
    path("api/logout/", auth_view.logout_user, name="logout_user"),

    path("api/users/", auth_view.user_list, name="user_list"),

    # smApp
    path("api/schoolInfo/", smApp_view.schoolInfo_create, name="school Info"),
    path("api/schoolInfo/<int:pk>", smApp_view.schoolInfo_create, name="update or delete Info"),

]
