from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ← 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ← ログインビュー追加
    path('', include('community_app.urls')),  # ← アプリのURL読み込み
]


