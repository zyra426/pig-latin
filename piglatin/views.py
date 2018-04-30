from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    text = request.GET['origText'].lower()

    translation = ''

    for word in text.split():
        if word[0] in ["a", "e", "i", "o", "u"]:
            # vowel
            translation += word
            translation += "way "
        elif word[1] in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]: 
            # consonant
            translation += word[2:]
            translation += word[0:2] + "ay "
        else:
            translation += word[1:]
            translation += word[0] + "ay "

    return render(request, 'translate.html', {'original': text, 'translation': translation})

def about(request):
    return render(request, 'about.html')