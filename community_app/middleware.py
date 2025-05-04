# community_app/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

# 未ログイン状態でもアクセスを許可するパス一覧
EXEMPT_URLS = [
    "/",              # トップページを許可
    "/signup/",       # ユーザー登録ページ
    "/login/",        # ログインページ
    "/admin/",        # 管理画面
    "/static/",       # 静的ファイル
]

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            # 上記以外のパスはリダイレクト
            if not any(path.startswith(url) for url in EXEMPT_URLS):
                return redirect(reverse('signup'))
        return self.get_response(request)
