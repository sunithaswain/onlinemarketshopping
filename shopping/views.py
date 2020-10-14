from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import buying_model,sellers_model,products_model,contact_model
from .forms import buying_form,sellers_form,products_form,contacts_form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as signout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.hashers import make_password
from django.conf import settings

def buyings(request):
    ''' this is for displaying data and storing in database '''
    success_message = ""
    #this is for form validation
    name = email = mobile = deliver_address = password1 = password2 =""
    if request.method == "POST":
        form = buying_form(request.POST)
        print ('post method')
        print (request.POST)
        if form.is_valid():
            print ('if form is valid')
            name = request.POST.get('name')
            #username1 = form.cleaned_data.get('name')
            #print ('username is ',username1) 
            email = request.POST.get('email') 
            mobile= request.POST.get('mobile')
            deliver_address=request.POST.get('deliver_address') 
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            user = buying_model.objects.create(name=name,email=email,mobile=mobile,deliver_address=deliver_address,password=password1)
            #password in dotformat
            user.password = make_password(password=password1)
            user.save()
            #search functially
            success_message = "Buyer successfully created"
            from_email = 'sunithaswain9@gmail.com'
            if email:
                try:
                    send_mail("Buyer Registration", success_message, from_email, [email], fail_silently=False)
                    success_message = "User Created and Email sent successfully"
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
        else:
            print('not valid form')
    else:
        print ('else condition')
        form = buying_form()
        print()
    return render(request, 'buyer.html', {'form':form, 'message':success_message,'name':name,'email':email,'deliever_address':deliver_address,
        'mobile':mobile,'password1':password1,'password2':password1})
def sellings(request):
    success_message = ""
    if request.method == "POST":
        form = sellers_form(request.POST)
        print ('post method')
        if form.is_valid():
            print ('if form is valid')
            name = request.POST.get('name') 
            email = request.POST.get('email') 
            password= request.POST.get('password') 
            sellers_contact_address=request.POST.get('sellers_contact_address')
            sellers_contact_number=request.POST.get('sellers_contact_number')
            user = sellers_model.objects.create(name=name,email=email,password=password,sellers_contact_address=sellers_contact_address,sellers_contact_number=sellers_contact_number)
            user.password = make_password(password=password)
            user.save()
            success_message = "Buyer successfully created"
            from_email = 'sunithaswain9@gmail.com'
            if email:
                try:
                    send_mail("Seller Registration", success_message, from_email, [email], fail_silently=False)
                    success_message = "User Created and Email sent successfully"
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            success_message = "User successfully created"
        else:
            print('not valid form')
    else:
        print ('else condition')
        form = sellers_form()
        print()
    return render(request, 'seller.html', {'form':form, 'message':success_message}) 
def productings(request):
    success_message = ""
    if request.method == "POST":
        form = products_form(request.POST, request.FILES)
        print ('post method')
        if form.is_valid():
            print ('if form is valid')
            # sellers_id = request.POST.get('sellers_id') 
            product_name = request.POST.get('product_name') 
            product_images= request.FILES.get('product_images') 
            product_details=request.POST.get('product_details')
            products = products_model.objects.create(sellers_id=1,product_name=product_name,product_images=product_images,product_details=product_details)
            success_message = "User successfully created"
        else:
            print('not valid form')
    else:
        print ('else condition')
        form = products_form()
        
    return render(request, 'product.html', {'form':form, 'message':success_message})            
def contactings(request):
    success_message = ""
    if request.method == "POST":
        form = contacts_form(request.POST)
        print ('post method')
        if form.is_valid():
            print ('if form is valid')

            email = request.POST.get('email') 
            query = request.POST.get('query')
            description=request.POST.get('description')
            product_details=request.POST.get('product_details')
          
            user = User.objects.create(email=email,query=query,description=description,product_details=product_details)
            
            # user.save()
            success_message = "User successfully created"

        else:
            print('not valid form')
    else:
        print ('else condition')
        form = contacts_form()
        print()
    return render(request, 'contact.html', {'form':form, 'message':success_message}) 
def searchings(request):
    print("PPPPPPPP")
    answers = ""
    if request.method == "GET":
        print("<<<<<<<<<<<<<<<<<")
        print(request.GET)
        search_query=request.GET.get("search_box")
        print (search_query,'>>>>>>>>>>>>>')

        result=products_model.objects.filter(product_name__icontains=search_query)
        print(result,"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
        uname=""
        for i in result:
            #getting only productname from product
            uname=i.product_name

        # result_name=products_model.objects.get(product_name__icontains=search_query)
    return render(request,"get.html",{"all":result, 'list1':answers})
def gettings(request):
    result = ""
    answers = products_model.objects.all()#getting all records from Answer table
    
   

    return render(request, "get.html", {'list1':answers,"all":result,'media':settings.MEDIA_URL })
def contactings_detail(request):
    success_message = ""
    if request.method == "POST":
        form = contacts_form(request.POST)
        print ('post method')
        if form.is_valid():
            print ('if form is valid')
            email = request.POST.get('email') 
            query = request.POST.get('query') 
            description= request.POST.get('description') 
            #sellers_contact_address=request.POST.get('sellers_contact_address')
            #sellers_contact_number=request.POST.get('sellers_contact_number')
            user = contact_model.objects.create(email=email,query=query,description=description)
            success_message = "User successfully created"
        else:
            print('not valid form')
    else:
        print ('else condition')
        form = contacts_form()
        print(">>>>>>>>>>>>>>>>>>")
    return render(request, 'contact_det.html', {'form':form, 'message':success_message})
def home(request):
    return render(request, 'home.html')