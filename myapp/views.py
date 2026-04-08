from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
import random

def transfer_form(request):
    if request.method == "POST":
        context = {
            'sender': request.POST['sender'],
            'receiver': request.POST['receiver'],
            'account': request.POST['account'],
            'amount': "{:,.2f}".format(float(request.POST['amount'])),
            'transaction_id': "20800" + str(random.randint(10000000,99999999)),
            'date_time': datetime.now().strftime("%d %b %Y, %I:%M %p")
        }
        return render(request, 'receipt.html', context)

    return render(request, 'form.html')