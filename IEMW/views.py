# Create your views here.

from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render
from django.template import loader

from .models import User

def index(request):
    users_list = User.objects.order_by('id')[:2]
    output = ', '.join([u.username for u in users_list])
    return HttpResponse(output)

#def detail(request, user_id):
#    users_list = User.objects.order_by('id')[:2]
#    template = loader.get_template('IEMW/index.html')
#    context = { 'users_list': users_list, }
#    return HttpResponse(template.render(context, request))
    
def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'IEMW/detail.html', {'user': user })



