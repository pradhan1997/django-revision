from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse('learning to unlearn')
    data_dict = {
        'some_content': 'content from view'
    }
    return render(request, 'hacktober/index.html', context=data_dict)

