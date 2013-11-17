from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json

from listitems.models import ListItem

def home(request):
    return auth_view(request)

def login(request):
    c = {}
    c.update(csrf(request))
    c.update({'authenticated': request.user.is_authenticated()})
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/shopping_list/')
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    username = request.POST.get('signup_username', '')
    email    = request.POST.get('signup_email', '')
    password = request.POST.get('signup_password', '')
    confirm = request.POST.get('confirm_password', '')

    user = User.objects.create_user(username, email, password)
    print '*'*40
    print user
    print type(user)
    print '*'*40
    return HttpResponseRedirect('/shopping_list/')

    # if user is not None:
    #     user = auth.authenticate

@login_required
def add_item(request):
    new_item = request.POST.get('newitem', '')
    response_data = {}
    if len(new_item) > 0:
        new_list_item = ListItem(listitem=new_item, purchased=False, user=request.user)
        try:
            new_list_item.save()
            response_data['success'] = True
            response_data['data'] = {'listitem': new_item, 'purchased': False}
        except Exception, e:
            response_data['success'] = False
            response_data['data'] = e
    else:
        response_data['success'] = False
        response_data['data'] = 'no item sent'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required
def shopping_list(request):
    list_items = ListItem.objects.order_by('listitem')
    context = {
        'list_items': list_items,
        'username': request.user.username+"'s ",
        'authenticated': request.user.is_authenticated()
    }
    context.update(csrf(request))
    return render_to_response('shopping_list.html', context)

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
