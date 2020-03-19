# from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from . import latest_news, data_ret


# Create your views here.

def top_news(request):
    auth = request.GET.get('auth', '')
    # print(auth)
    if(auth == 'dota'):
        top_news = latest_news.news().get_data()
        return JsonResponse(top_news)
    else:
        return HttpResponse("Invalid Auth")


def landing_page(request):
    return render(request, 'landing_page.html', {})

def user_data(request):
    auth = request.GET.get('auth', '')
    uid = request.GET.get('uid','')
    print(auth, uid)
    if(auth == "dota"):
        try:
            useful_data = data_ret.logs().get_report(uid)
        except:
            return HttpResponse("Invalid UID")
        return JsonResponse(useful_data)
    else:
        return HttpResponse("Invalid auth")

        # 'etEO6dckE3QrvSu6yEwvVqnPvIG3'
    
    # http://localhost:8000/latest/user_data?auth=dota&uid={uid}