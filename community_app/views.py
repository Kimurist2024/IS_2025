from django.shortcuts import render, redirect
from .models import Question, Choice, UserAnswer, Community
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# 1. トップページ（ログイン済みかどうかで分岐してもよい）
def top_page(request):
    return render(request, 'community_app/top.html')


# 2. アンケートページ（ログイン必須）
@login_required
def survey_page(request):
    questions = Question.objects.all()

    if request.method == "POST":
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                UserAnswer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'choice': choice}
                )
        return redirect('result_page')

    return render(request, 'community_app/survey.html', {'questions': questions})


# 3. 結果ページ（ユーザーの回答とタグでマッチング）
@login_required
def result_page(request):
    user_answers = UserAnswer.objects.filter(user=request.user)
    keywords = [ua.choice.text for ua in user_answers]

    scored_communities = []
    for community in Community.objects.all():
        score = sum(1 for kw in keywords if kw in community.tags)
        scored_communities.append((community, score))

    top_matches = sorted(scored_communities, key=lambda x: x[1], reverse=True)[:3]

    return render(request, 'community_app/result.html', {
        'matches': top_matches,
        'keywords': keywords
    })


# 4. ログアウト処理
def logout_view(request):
    logout(request)
    return redirect('top_page')


# 5. ユーザー登録（サインアップ）ページ
def signup(request):
    # すでにログイン済みならトップページへリダイレクト
    if request.user.is_authenticated:
        return redirect('top_page')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録直後にログイン
            return redirect('top_page')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
