# community_app/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

# 完全一致で除外するパス（ログイン不要）
EXEMPT_PATHS = [
    "/",                  # トップページ
    "/signup/",           # ユーザー登録ページ
    "/accounts/login/",   # Django標準ログインURL
    "/accounts/logout/",  # Django標準ログアウトURL
    "/admin/",            # 管理画面
]

# プレフィックスで除外（静的ファイルなど）
EXEMPT_PREFIXES = [
    "/static/",           # CSS/JSなど
    "/favicon.ico",       # ブラウザのアイコン取得
]

class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        # 未ログインかつ、除外対象でなければリダイレクト
        if not request.user.is_authenticated:
            if path not in EXEMPT_PATHS and not any(path.startswith(p) for p in EXEMPT_PREFIXES):
                return redirect(reverse('signup'))

        return self.get_response(request)
