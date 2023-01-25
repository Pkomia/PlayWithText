from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('Hyy re munna u are in ')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Toupper(request):
    # Get text 
    temptext=request.GET.get('text', 'default')
    statusup = request.GET.get('Toupper', 'off')
    statuslower = request.GET.get('Tolower', 'off')
    statusPunc  = request.GET.get('Removepunc', 'off')

    print(temptext)
    print(statusup)
    
    analyzed = temptext
    purpose  = "Error , please check a valid option"
    flag =False

    if statusup=='on':
      flag = True
      analyzed = analyzed.upper()
    if statuslower == 'on':
      flag = True
      analyzed = analyzed.lower()
    if statusPunc == 'on':
      flag = True
      punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

      for ele in analyzed:
        if ele in punc:
            analyzed= analyzed.replace(ele, "")
       
    if(flag):
        purpose= " Analyzed!!"
    
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analysed.html', params)
  
 