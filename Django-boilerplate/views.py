from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        channel_1 = request.POST.get('channel1')
        channel_2 = request.POST.get('channel2')
        channel_3 = request.POST.get('channel3')
        channel_4 = request.POST.get('channel4')
        channel_5 = request.POST.get('channel5')
        channel_6 = request.POST.get('channel6')
        channel_7 = request.POST.get('channel7')
        channel_8 = request.POST.get('channel8')
        

        print(channel_1,channel_2,channel_3,channel_4,channel_5,channel_6,channel_7,channel_8)
        return HttpResponse('data submitted')
    return render(request, 'index.html', {})