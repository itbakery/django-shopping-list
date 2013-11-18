from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.db import connection

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
    print 'username: '+username
    print 'password: '+password

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/shopping_list/')
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    username = request.POST.get('username', '')
    email    = request.POST.get('signup_email', '')
    password = request.POST.get('password', '')
    confirm = request.POST.get('confirm_password', '')
    user = User.objects.create_user(username, email, password)
    print 'user=', user
    auth_user = auth.authenticate(username=username, password=password)
    print 'auth_user', auth_user
    auth.login(request, auth_user)
    return HttpResponseRedirect('/shopping_list/')

@login_required
def add_item(request):
    new_item = request.POST.get('newitem', '').capitalize()
    response_data = {}
    if len(new_item) > 0:
        new_list_item = ListItem(listitem=new_item, purchased=False, user=request.user)
        try:
            new_list_item.save()
            response_data['success'] = True
            response_data['listitem'] = new_item
            response_data['item_slug'] = new_item.lower().replace(' ', '-').replace("'",'').strip()
            response_data['purchased'] = False
            print 'OK'
        except Exception, e:
            print 'NOT OK'
            response_data['success'] = False
            response_data['message'] = e
    else:
        response_data['success'] = False
        response_data['message'] = 'no item sent'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required
def delete_item(request):
    item = request.POST.get('item', '').capitalize()
    response_data = {}
    if len(item) > 0:
        try:
            print '____ item = '+item+' ___________'
            print ListItem.objects.filter(user=request.user, listitem=item).delete()
            print '________________________________________________'
            response_data['success'] = True
            response_data['item_slug'] = item.lower().replace(' ', '-').replace("'",'').strip()
        except Exception, e:
            response_data['success'] = False
            response_data['message'] = e
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required
def purchased(request):
    item = request.POST.get('item', '').capitalize()
    purchased = request.POST.get('purchased')
    response_data = {}
    if len(item) > 0:
        purch = None            
        try:
            listitem = ListItem.objects.get(user=request.user, listitem=item)
            if purchased == 'true':
                purch = True
                listitem.purchased = purch
            else:
                purch = False
                listitem.purchased = purch
            listitem.save()
            response_data['success'] = True
            response_data['purchased'] = purch
            response_data['item_slug'] = item.lower().replace(' ', '-').replace("'",'').strip()
        except Exception, e:
            response_data['success'] = False
            response_data['message'] = e
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required
def shopping_list(request):
    list_items = ListItem.objects.filter(user=request.user).order_by('listitem')
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
