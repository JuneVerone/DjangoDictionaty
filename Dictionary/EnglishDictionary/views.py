from django.shortcuts import render, redirect
from django.contrib import messages
from PyDictionary import PyDictionary

wordmeaning = PyDictionary()
# Create your views here.
def dictionary(request):
    
    
    
    if request.method == "POST":
        word = request.POST['word']
        
        mean = PyDictionary.meaning(word)
        return render(request, 'dictionary.html', {'word': word, 'mean' : mean})
    return render(request, 'dictionary.html')
