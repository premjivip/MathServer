

from django.shortcuts import render
def squareprism(request):
    context={}
    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        b = request.POST.get('base','0')
        h = request.POST.get('heigth','0')
        print('request=',request)
        print('base=',b)
        print('heigth=',h)
        area = 2*(int(b) **2)  + 4* int(b) *int(h)
        context['area'] = area
        context['b'] = b
        context['h'] = h
        print('Area=',area)
    return render(request,'mathapp/math.html',context)