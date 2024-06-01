from django.shortcuts import render,redirect
from .models import app
from .forms import appForm
from  django.contrib import messages

# Create your views here.

def index(req):
    item_list = app.objects.order_by('-date')
    if req.method == 'POST':
        form = appForm(req. POST)
        if form.is_valid():
            form.save()
            return redirect('app')
    
    form = appForm()
    page = {
        'forms':form,
        'list':item_list,
        'title':'app LIST',
    }
    return render(req, 'app/index.html', page)


def remove(req, item_id):
    item = app.objects.get(id = item_id)
    item.delete()
    messages.info(req, 'message has been deleted!...')
    return redirect('app')



