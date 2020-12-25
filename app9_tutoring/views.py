"""views.py for tutorboard """
from django.shortcuts import render, redirect
from app1_user_accounts.models import UserAccount
from .models import TutorRequest
from .forms import TutorReqForm


# Create your views here.


def tutorboard(request):
    """this is a tutor board page loading"""
    res_data = {}
    session_id = request.session.get('session_id')
    if session_id:
        user = UserAccount.objects.get(pk=session_id)
        tutor_reqs = TutorRequest.objects.get(userid=user.id)
        res_data['title'] = tutor_reqs.title
        # will be changed to word searching queries
        res_data['word1'] = tutor_reqs.word1
        res_data['word2'] = tutor_reqs.word2
        res_data['word3'] = tutor_reqs.word3
        res_data['word4'] = tutor_reqs.word4
        res_data['word5'] = tutor_reqs.word5

        res_data['question_txt'] = tutor_reqs.question_txt
        res_data['request_dt'] = tutor_reqs.request_dt

    return render(request, 'tutorboard.html', res_data)


def add_tutor_req(request):
    """this is adding new tutor request"""
    if request.method == 'POST':
        res_data = {}
        form = TutorReqForm(request.POST)
        if form.is_valid():
            session_id = request.session.get('session_id')
            user = UserAccount.objects.get(pk=session_id)
            new_tutor_req = TutorRequest(
                userid=user.userid,
                word1=form.word1,
                word2=form.word2,
                word3=form.word3,
                word4=form.word4,
                word5=form.word5,
                wordlist=str([form.word1, form.word2, form.word3,
                              form.word4, form.word5]),

            )
            new_tutor_req.save()
            res_data['tutor_add_success'] = '질문이 성공적으로 등록되었습니다.'
            return redirect('tutorboard/', res_data)
    else:
        # add user account type(paid/free) check later (unpaid => to subscription page)
        form = TutorReqForm()
    return render(request, 'tutor_request.html', {'form': form})
