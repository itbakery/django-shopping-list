from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from listitems.models import ListItem

def home(request):
    return auth_view(request)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/shopping_list/')
    else:
        return HttpResponseRedirect('/invalid/')

def shopping_list(request):
    print 'GOT HERE'
    list_items = ListItem.objects.order_by('listitem')
    return render_to_response('shopping_list.html',
        {
            'list_items': list_items,
            'username': request.user.username
        })
    # return render_to_response('shopping_list.html',
    #                           {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


