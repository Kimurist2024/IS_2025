from django.shortcuts import render, redirect
from .models import Question, Choice, UserAnswer, Community
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# 1. トップページ
def top_page(request):
    return render(request, 'community_app/top.html')


# 2. アンケートページ（複数質問を表示）
@login_required
def survey_page(request):
    questions = Question.objects.all()
    if request.method == "POST":
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                UserAnswer.objects.update_or_create(
                    user=request.user,
                    question=question,
                    defaults={'choice_id': choice_id}
                )
        return redirect('result_page')

    return render(request, 'community_app/survey.html', {'questions': questions})


# 3. 結果ページ（マッチングロジック例：タグ一致数が多い団体を上位に）
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

