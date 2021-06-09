from django.http import HttpResponse
from django.shortcuts import render

def name(request):
    return render(request,'index.html')

def about(request):
    getText = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline','off')
    spaceRemover = request.POST.get('spaceRemover','off')
    charCount = request.POST.get('charCount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzer = ''
        for char in getText:
            if char not in punctuations:
                analyzer = analyzer + char
        params = {'EnteredText':getText,'AnalyzedText': analyzer}
        getText = analyzer

    if fullcaps=="on":
        analyzer = ''
        for char in getText:
            analyzer = analyzer + char.upper();
        params = {'EnteredText': getText,'AnalyzedText': analyzer }
        getText = analyzer

    if newline=="on":
        analyzer = ''
        for char in getText:
            if char != '\n' and char != '\r':
                analyzer = analyzer + char
        params = {'EnteredText': getText,'AnalyzedText': analyzer }
        getText = analyzer

    if spaceRemover=="on":
        analyzer = ''
        for index, char in enumerate(getText):
            if getText[index] == ' ' and getText[index+1] == " ":
                pass
            else:
                analyzer = analyzer + char

        params = {'EnteredText': getText,'AnalyzedText': analyzer }
        getText = analyzer

    if charCount == "on":
        analyzer = ''
        analyzer = analyzer + str(len(getText))
        params = {'EnteredText': getText, 'AnalyzedText': analyzer}
        getText = analyzer

    if removepunc != "on" and fullcaps != "on" and newline != "on" and spaceRemover != "on":
        return HttpResponse("Error")

    return render(request,'analyzed.html', params)
