from django.shortcuts import redirect, render
from . models import User
from . forms import UserForm
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method =='POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # create user using form method
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()

            # create user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,password=password,
            username=username,email=email
            )
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been register successfully')
            return redirect('registerUser')
        else:
            print('Invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form':form,
    }
    return render (request, 'accounts/registerUser.html',context)