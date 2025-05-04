from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('survey/', views.survey_page, name='survey_page'),
    path('result/', views.result_page, name='result_page'),
    path('logout/', views.logout_view, name='logout'),  # ログアウト
    path('signup/', views.signup, name='signup'),       # ← 追加：ユーザー登録
]
