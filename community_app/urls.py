from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name='top_page'),                      # トップページ
    path('survey/', views.survey_page, name='survey_page'),         # アンケートページ
    path('result/', views.result_page, name='result_page'),         # 結果ページ
    path('logout/', views.logout_view, name='logout'),              # ログアウト
    path('signup/', views.signup, name='signup'),                   # サインアップ
    path('communities/', views.community_list, name='community_list'),  # コミュニティ一覧
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),   # ✅ チャットルーム追加
]
