from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout 
from .models import District, Branch 
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers
# this is a change

def home(request):
    branches = Branch.objects.all()[:5]
    return render(request, 'index.html', {'branches': branches})

def register(request):
    branches = Branch.objects.all()[:5]

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Taken")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                user.save()
                messages.success(request, "Registration successful. You can now log in.")

                user = auth.authenticate(request, username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('banking_app:login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html', {'branches': branches})


def login(request):
    branches = Branch.objects.all()[:5]

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            return redirect('/')  
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'login.html', {'branches': branches})

def logout_view(request):
    auth_logout(request)  
    return redirect('banking_app:login')  

def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def forms(request):
    if request.method == 'POST':
        # Extract the materials provided as a list from request.POST
        materials_provided = request.POST.getlist('materials')

        # Check if at least one material is selected
        if not materials_provided:
            messages.error(request, "Please select at least one material provided.")
            return redirect('banking_app:forms')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district_id = request.POST['district']
        branch_id = request.POST['branch']
        account_type = request.POST['account_type']

        # Check if all the required fields have values
        if (
            first_name and last_name and date_of_birth and age and
            gender and phone_number and email and address and
            district_id and branch_id and account_type
        ):
            try:
                # Create a new User instance using Django's built-in User model
                user = User.objects.create_user(
                    username=email,  # You can use the email as the username
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=None,  # You can set a password here if needed
                )

                # Handle materials provided data as needed
                for material in materials_provided:
                    # You can save this information in your database, associate it with the user, or perform any other action.
                    # For now, let's just print the selected materials.
                    print("Material Provided:", material)

                messages.success(request, "User created successfully.")
                return redirect('banking_app:home')
            except Exception as e:
                messages.error(request, "An error occurred while creating the user.")
        else:
            messages.error(request, "Please fill out all the required form fields.")

    # Load the form template for GET requests
    districts = District.objects.all()
    branches = Branch.objects.all()
    return render(request, 'form.html', {'districts': districts, 'branches': branches})



def get_districts_and_branches(request):

    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district=district_id)

    class BranchSerializer(serializers.ModelSerializer):
        class Meta:
            model = Branch
            fields = '__all__'

    Serializer = BranchSerializer(branches,many=True)

    return JsonResponse({'status':'done','data':Serializer.data})