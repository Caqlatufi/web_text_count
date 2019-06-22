#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    total = request.GET['text']
    total_count = len(total)

    word_dict = {}
    
    for word in total:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    NEW = sorted(word_dict.items(), key=lambda w:w[1], reverse=True)


    return render(request, 'count.html', {'count':total_count, 'text':total, 'max':NEW})
    