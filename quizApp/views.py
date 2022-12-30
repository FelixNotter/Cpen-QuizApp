from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,SuggestionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.core.cache import cache
import random 
import datetime
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')

def suggestion(request):
    if request.method == "POST":
        forms = SuggestionForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,f"Thanks For Your Suggestion ")
            return redirect('home')
    else:
        forms = SuggestionForm()
    return render(request,'suggestions.html',{'forms':forms})

@login_required
def quiz_view(request, catgry):
    category = Category.objects.filter(name=catgry).first()
    qs = Question.objects.filter(categories=category)
    p = Paginator(qs, 3)
    page = request.GET.get('page')
    page_content = p.get_page(page)

    has_questions = False
    if qs:
        has_questions = True

    context = {
       'page_content':page_content, 
       'has_questions':has_questions
    }
    score = dry(request,"signals",context)
    return render(request,'courses/basequiz.html', context)

@login_required
def progress(request):
    profiles = Profile.objects.all()
    return render(request,'progress.html',{"profiles":profiles})
    
@login_required
def leader(request):
    profiles = sorted(Profile.objects.all(), key= lambda obj: Profile.get_total_score(obj),reverse=True)
    all = []
    for index,profile in enumerate(profiles):
        index +=1
        all.append((index,profile))
    return render(request,'leader.html',{'profiles':all})




# Making My Code Cleaner
def dry(request,name,context):
    score = 0
    if request.method == "POST":
        if 'restart' in request.POST:
            minus = Profile.objects.get(user = request.user)
            minus.nummerical_score -= 5
            minus.signals_score-= 5
            minus.networks_score -= 5
            minus.operate_score -= 5
            minus.programming_score-= 5
            minus.architect_score -= 5
            minus.save
            cache.clear()
            messages.success(request,"Quiz Successfully Restarted!")
            return redirect(name)
        elif 'check' in request.POST:
            user_ans = request.POST.get('option')
            id = request.POST.get('id')
            correct_ans = Question.objects.get(id=id).correct_answer
            context["user_ans"] = user_ans
            context["correct_ans"] = correct_ans
            if cache.get(id):
                messages.warning(request,f"Question {request.POST.get('id')} has Already been answered Move To Next Question")
                return redirect(name)
            if id != None:
                context['id'] = id
            if user_ans == None:
                messages.warning(request,f"Empty Answer,Please try again!")
                return redirect(name)
            elif correct_ans != None and user_ans != correct_ans:
                messages.warning(request,f"Wrong Answer,you score {score} points")
                cache.set(id,True)
                return redirect(name)
            else:
                score = Question.objects.get(id=id).score
                recorded = Profile.objects.get(user = request.user)
                if name == "methods":
                    recorded.nummerical_score += score
                    recorded.save()
                elif name == "programming":
                    recorded.programming_score += score
                    recorded.save()
                elif name == "architect":
                    recorded.architect_score += score
                    recorded.save()
                elif name == "signals":
                    recorded.signals_score += score
                    recorded.save()
                elif name == "networks":
                    recorded.networks_score += score
                    recorded.save()
                elif name == "operate":
                    recorded.operate_score += score
                    recorded.save()
                messages.success(request,f" Correct,you score {score} points")
                cache.set(id,True)
                return redirect(name)
    
