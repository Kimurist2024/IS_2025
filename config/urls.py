from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ログイン・ログアウトビュー

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),

    # Django標準のログイン・ログアウトビュー
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # アプリのURL設定
    path('', include('community_app.urls')),
]
