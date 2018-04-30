from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    text = request.GET['origText'].lower()

    translation = ''
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    for word in text.split():
        if word[0] in vowels:
            # vowel
            translation += word
            translation += "way "
        elif word[1] in consonants: 
            # consonant
            translation += word[2:]
            translation += word[0:2] + "ay "
        else:
            translation += word[1:]
            translation += word[0] + "ay "

    return render(request, 'translate.html', {'original': text, 'translation': translation})

def about(request):
    return render(request, 'about.html')