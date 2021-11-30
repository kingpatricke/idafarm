from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='tuganimana01@gmail.com'
api_key ='1526a36fc4c257d18d07bcfd53b0d18324ce969a5cd6981a35abfa6028b259ac'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        if text == '':
            response =  "CON Murakaza neza kuri Idafarm \n"
            response += "1. Kwandikisha igihingwa \n"
            response += "2. Kumenya ingengabihe \n"
            response += "3. Umushahara"
        elif text == '1':

            response = "CON Hitamo igihingwa \n"
            response += "00. SUbira inyuma \n"
        elif text == '1*00':
                text = level-1   

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')