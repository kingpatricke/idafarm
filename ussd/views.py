from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='kingpatrick250@gmail.com'
api_key ='5cf7044ca84b41d4a8db500c2ec647b618819150a012eb4081c3cd19921ea9ad'
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
        #  main menu for our application
        if text == '':
            response = "CON Murakaza neza kuri IDA Smart Irrigation System \n"
            response = "CON Murakaza neza kuri IDA Smart Irrigation System \n"
            response += "1. Ikinyarwanda \n"
            response += "2. English \n"

        elif text == '1':
            response = "CON Murakaza neza \n"
            response += "1. Amakuru kubijyanye no kuhira \n"
            response += "2. ibikoresho bikoreshwa mu kuhira \n"
            response += "3. Kwiyandikisha \n"
            

        elif text == '1*1':
            fetchProducts = Productsmodels.objects.all()
            response = "CON Hitamo igihingwa \n"
            for products in fetchProducts:
                response += ""+str(products.id)+"."+str(products.title)+"\n"

      
        elif text == '1*1*1':
            product="Ibinyomoro"
            response = "CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Uwo mubufatanyije \n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"


        elif text == '1*2':
            product ="Indimu"
            response ="CON shyiramo ubuso bw'ubutaka bwawe bw' "+str(product)+"\n"
        elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "CON Uwo mubufatanyije \n"
        elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON Hitamo igihe \n "
            response += "1. Rimwe mukwezi \n"
            response += "2. Kabiri Mukwezi \n"
            response += "3. Buri gihe"
        elif text == '2*1':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        elif text == '2*2':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        elif text == '2*3':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')