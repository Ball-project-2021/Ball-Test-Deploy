from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('api/auth/', include('djoser.urls')),
        path('api/auth/', include('djoser.urls.jwt')),
        path('admin/', admin.site.urls),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Authorization URLs,
# api/auth/users/ = create new user, "POST"
# api/auth/users/activation/ = activation user account, "POST" =>{
# uid, token }
# api/auth/jwt/create/ = login, "POST"
# api/auth/users/reset_password/ = reset password "POST" =>{
# email }
# api/auth/users/reset_password_confirm/ = change password =>{
# uid, token, new_password, re_new_password }
