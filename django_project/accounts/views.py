from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from contacts.models import Contact

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        passsword2 = request.POST['password2']

        if password == passsword2:
            ''' check user in db '''
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.INFO, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password)
                    '''Logining after registration'''
                    user.save()
                    messages.add_message(request, messages.INFO, 'You have already registered')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')



def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.INFO, 'You are now logged in')
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, 'Invalid credentials')

    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.INFO, 'You are now logged out')
        return redirect('index')

def dashboard(request):

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)