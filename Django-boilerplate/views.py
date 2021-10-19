from django.shortcuts import render
from django.http import HttpResponse
import csv 

from .index import ouptut





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
        header = ['channel1', 'channel2', 'channel3', 'channel4', 'channel5', 'channel6', 'channel7', 'channel8']
        data = [channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, channel_7, channel_8]
        with open('templates/index.csv', 'w', encoding='UTF8',newline='') as file:
            writer = csv.writer(file)

            
            writer.writerow(header)

            # writing data
            writer.writerow(data)
        
        
        
        print(channel_1,channel_2,channel_3,channel_4,channel_5,channel_6,channel_7,channel_8)
        return HttpResponse('data submitted')
    return render(request, 'index.html', {})



def output_view(request):
    returned_data = output()
    context = {'data':returned_data}
    return render(request, 'output.html',context)