from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name='top_page'),             # トップページ（要ログイン）
    path('survey/', views.survey_page, name='survey_page'),# アンケートページ（要ログイン）
    path('result/', views.result_page, name='result_page'),# 結果ページ（要ログイン）
    path('logout/', views.logout_view, name='logout'),     # ログアウト
    path('signup/', views.signup, name='signup'),          # ユーザー登録（未ログインOK）
]