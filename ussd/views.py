from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='tuganimana0@gmail.com'
api_key ='1526a36fc4c257d18d07bcfd53b0d18324ce969a5cd6981a35abfa6028b259ac'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phoneNumber = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        category = text[:3]
        response =""
        if  text=='':
             response ="CON Murakaza neza kuri Idafarm"
             response +="1. Kwandikisha igihingwa"
             response +="2. Kumenya ingengabihe"
             response +="3. Umushahara"
        elif text == '1':
            response ="CON Hitamo igihingwa"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"


    return HttpResponse('we are on ussd app')