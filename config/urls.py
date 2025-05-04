from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ← ログインビュー用

urlpatterns = [
    path('admin/', admin.site.urls),

    # ログイン・ログアウトを Django 標準ビューに任せる（テンプレート配置要）
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # ← 追加

    # アプリURL読み込み
    path('', include('community_app.urls')),
]
