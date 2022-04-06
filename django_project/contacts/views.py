from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact

def contact(request):
    global listing_id
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']




        contact = Contact(listing=listing,  listing_id=listing_id, name=name, email=email, phone=phone,
         message=message, user_id=user_id)

        contact.save()

        '''send email'''
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for' + listing + 'Check it',
            'mamuka2281488@gmail.com',
            [realtor_email, 'Olena97@gmail.com'],
            fail_silently=False
        )



        messages.add_message(request, messages.SUCCESS, 'Your request has been submitted, a realtor will get back to you')


        return redirect('/listings/'+listing_id)
