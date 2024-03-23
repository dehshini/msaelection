from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm #, UserTestForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote
#from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.db.models import Count
#from django.http import Http404
from django.contrib.auth.hashers import make_password
import csv, os #, io
from msa import settings


# Create your views here.
def HomeView(request):
    president = Candidate.objects.filter(Category=2)
    vicePresident = Candidate.objects.filter(Category=3)
    healthOfficer = Candidate.objects.filter(Category=5)
    exchangeOfficer = Candidate.objects.filter(Category=6)
    secretary = Candidate.objects.filter(Category=1)
    organizer = Candidate.objects.filter(Category=7)
    treasurer = Candidate.objects.filter(Category=4)
    pro = Candidate.objects.filter(Category=8)
    context = {
        'president': president,
        'secretary': secretary,
        'organizer': organizer,
        'treasurer': treasurer,
        'exchangeOfficer': exchangeOfficer,
        'healthOfficer': healthOfficer,
        'vicePresident': vicePresident,
        'pro': pro,
    }
#    return render(request, 'home.html', context)
#    context = {
#    }
    return render(request, 'home.html', context)


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


class LoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('home')

class LogoutView(LogoutView):
    template_name = 'logout.html'

    def get_success_url(self):
        return reverse('logout')


@login_required()
def VoteView(request):
    return render(request, 'pollclosed.html', {})

"""    if Vote.objects.filter(User_id=request.user.id).exists():
        votername = request.user
        user_votes = Vote.objects.filter(User_id=request.user).values()
       # user_votes = Vote.objects.filter(User_id=request.user).values()
        context = {
            'votername': votername,
            'user_votes': user_votes,
        }
        return render(request, 'voted.html', context)
    else:
        president = Candidate.objects.filter(Category=2)
        secretary = Candidate.objects.filter(Category=1)
        organizer = Candidate.objects.filter(Category=7)
        treasurer = Candidate.objects.filter(Category=4)
        exchangeOfficer = Candidate.objects.filter(Category=6)
        healthOfficer = Candidate.objects.filter(Category=5)
        vicePresident = Candidate.objects.filter(Category=3)
        pro = Candidate.objects.filter(Category=8)

        context = {
            'president': president,
            'organizer': organizer,
            'treasurer': treasurer,
            'exchangeOfficer': exchangeOfficer,
            'healthOfficer': healthOfficer,
            'vicePresident': vicePresident,
            'pro': pro,
        }

        return render(request, 'vote.html', context) """



@login_required()
def Votepoll(request):
    try:
        username = request.user
        user = User.objects.get(id=username.id)
        pre = request.POST.get('president')
        sec = request.POST.get('secretary')
        org = request.POST.get('organizer')
        tre = request.POST.get('treasurer')
        exc = request.POST.get('exchangeOfficer')
        hea = request.POST.get('healthOfficer')
        vic = request.POST.get('vicePresident')
        pro = request.POST.get('pro')
        Vote.objects.create(User=user, President=pre, Secretary=sec, Organizer=org, Treasurer=tre, ExchangeOfficer=exc, HealthOfficer=hea, VicePresident=vic, Pro=pro,)
    except:
        return render(request, 'failed.html', {})
    return HttpResponseRedirect('voted')


#request not working
@login_required()
def VotesView(request):
    votername = request.user
    user_votes = Vote.objects.filter(User_id=request.user).values()

    context = {
        'votername' : votername,
        'user_votes' : user_votes,
    }
    return render(request, 'votes.html', context)

def VotedView(request):
    return render(request, 'voted.html', {})


def InstructionsView(request):
    return render(request, 'instructions.html', {})


def AboutView(request):
    return render(request, 'about.html', {})


@login_required()
def ResultsView(request):
    #    name = Candidate.LastName
    #    all_votes = Vote.objects.all()
    #    total_votes = all_votes.count()
    #    results_pre = Vote.objects.filter(President='name').count()
    #    results_sec =  Vote.objects.filter(Secretary=name).count()

    #    president = Candidate.objects.filter(Category=2)
    #    secretary = Candidate.objects.filter(Category=4)
    #    organizer = Candidate.objects.filter(Category=5)
    #    treasurer = Candidate.objects.filter(Category=8)
    #    exchangeOfficer = Candidate.objects.filter(Category=7)
    #    healthOfficer = Candidate.objects.filter(Category=6)
    #    vicePresident = Candidate.objects.filter(Category=3)

    total_votes = Vote.objects.count()
    total_votes_per_pre = Vote.objects.annotate(
        vote_count_pre=Count('President'))

    results_pre = str(Vote.objects.values('President').annotate(Count('President')))
    results_sec = Vote.objects.values('Secretary').annotate(Count('Secretary'))
    results_org = Vote.objects.values('Organizer').annotate(Count('Organizer'))
    results_pro = Vote.objects.values('Pro').annotate(Count('Pro'))
    results_hea = Vote.objects.values(
        'HealthOfficer').annotate(Count('HealthOfficer'))
    results_exc = Vote.objects.values(
        'ExchangeOfficer').annotate(Count('ExchangeOfficer'))
    results_vic = Vote.objects.values(
        'VicePresident').annotate(Count('VicePresident'))
    results_tre = Vote.objects.values('Treasurer').annotate(Count('Treasurer'))

    context = {
        'total_votes': total_votes,
        'results_pre': results_pre,
        'results_sec': results_sec,
        'results_tre': results_tre,
        'results_vic': results_vic,
        'results_exc': results_exc,
        'results_hea': results_hea,
        'results_pro': results_pro,
        'results_org': results_org,
    }


#   c = Category.objects.get(pk=category_id)
#    votes = c.votes_set.select_related()

#    vote_counts = {}

#    for v in votes:
#        if not vote_counts.has_key(v.):
#            vote_counts[v.item.id] = {
#                'item': v.item,
 #               'count': 0
  #          }

 #       vote_counts[v.item.id]['count'] += 1


#    pre = Votes.objects.values().annotate(Count(''))

#    cat = Category.objects.get(category_id)
 #   votes = cat.votes_set.select_related

    return render(request, 'results.html', context)


def Upload_users(request):
    with open(os.path.join(settings.BASE_DIR, 'p1.csv'), 'r') as f:
        csvf = csv.reader(f)
        data = []
        for row in csvf:
            username=row[0]
            password=make_password(row[1], None, 'md5')
            #email=row[2]
            #user=User(username=username, email=email, password=password)
            user=User(username=username, password=password)
            data.append(user)
        User.objects.bulk_create(data)

    context = {}
    return render(request, "upload_users.html", context)


#def Upload_users(request):
#    with open(os.path.join(settings.BASE_DIR, 'p1.csv'), 'r') as f:
#        csvf = csv.reader(f)
#        data = []
#        for row in csvf:
#            username=row[0]
#            password=make_password(row[1], None, 'md5')
            #email=row[2]
            #user=User(username=username, email=email, password=password)
            #user=User(username=username, password=password)
            #data.append(user)
#            m = User(username=username, password=password)
#            m.save()
#        User.objects.bulk_create(data)

#    context = {}
#    return render(request, "upload_users.html", context)
