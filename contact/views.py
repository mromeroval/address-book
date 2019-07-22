from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Users
from .forms import ContactForm, SearchContactForm, SearchDepartmentForm, SearchPositionForm
from django.contrib.auth.models import User
from django.db.models import Q
import json
from django.http.response import HttpResponse

# Create your views here.
global title
title = "Contact"

def index(request):
    return render(request, 'index.html')


def validate_user(request):
# Check if user exists in the database    
# Get the user's roles and active status
# If user is active save the user's variables in session and redirect to land page, else, the user is logged out
    username = request.user
    user = Users.objects.filter(username__exact=username)  # @UndefinedVariable
    if(user):
        for data in user:
            request.session['current_user'] = data.username
            request.session['user_id'] = data.id
            if data.admin == 1:
                request.session['is_admin'] = True
            if data.active == 1:
                request.session['is_active'] = True                  
            if 'is_active' in request.session:              
                return redirect('home')
            else:
                return redirect("home")
        
    else:
        return redirect("home")

    
def home(request):
  # Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:
        return render(request, 'home.html')
    # else:
    #     return redirect('index')    

def contact_list_search(request):
    executive = 0 
    executive_assistant = 0 
  # Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:   
        # Gets variables from nameForm
        
    if request.GET.get('first_name'):
        first_name = request.GET.get("first_name")
        queryset_contacts = Users.objects.filter(first_name__iexact=first_name).order_by('last_name')
    elif request.GET.get("last_name"):
        last_name = request.GET.get("last_name")
        queryset_contacts = Users.objects.filter(last_name__icontains =last_name).order_by('last_name')
    elif request.GET.get("first_name") and request.GET.get("last_name"):    
        first_name = request.GET.get("first_name")
        last_name = request.GET.get("last_name")
        queryset_contacts = Users.objects.filter(  # @UndefinedVariable
                                                    Q(first_name__iexact=first_name)&
                                                    Q(last_name__icontains = last_name)
                                                        ).order_by('last_name')
        
    elif request.GET.get("department"):
        department = request.GET.get("department")
        queryset_contacts = Users.objects.filter( department__icontains = department).order_by('last_name')
        
    elif request.GET.get("position"):
        position = request.GET.get("position")  
        queryset_contacts = Users.objects.filter( position__icontains = position).order_by('last_name')  

    else:
        queryset_contacts = ''                                             

    context = {
                    "title"  : "Contact List",
                    "queryset_contacts" : queryset_contacts,
                }
    return render(request,'contactSearchResult.html',context)

    # Commented out for testing purposes
    # else:
    #     return redirect('index')

def contact_list_active(request):
    # Commented out for testing purposes
      # if request.user.is_authenticated and 'current_user' in request.session:
    queryset_contacts= Users.objects.filter(active__iexact=1).order_by('last_name')
    context = {
                    "queryset_contacts" : queryset_contacts,
                }
    return render(request,'contactActiveList.html',context)
    # else:
    #     return redirect('index')

def contact_list_inactive(request):
  # Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:
    queryset_contacts= Users.objects.filter(active__iexact=0).order_by('last_name')
    context = {
                    "queryset_contacts" : queryset_contacts,
                }    
    return render(request,'contactInactiveList.html',context)
# Commented out for testing purposes

def create_contact(request):
# Commented out for testing purposes
# if request.user.is_authenticated and 'current_user' in request.session:
    form = ContactForm(request.POST or None)
    if form.is_valid():
                new_contact = form.save(commit=False)
                new_contact.save()
#                 messages.success(request, "User Created : "+new_user.cas_user)
                return redirect("contact:activelist")
#             return redirect("contact:list", str(new_contact.pk))
    context ={ 
              'title' : 'New Contact',
              'form' : form            
              }   
    return render(request,'contactForm.html', context)
    
    # else:
    #     return redirect('index')


def contact_detail(request, id=None):
# Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:
    contact = get_object_or_404(Users,id=id)
    context ={ 
              'title' : 'Contact Information',
              'contact' : contact
              }
    return render(request, 'contactDetail.html', context)
    # else:
    #     return redirect('index')

def edit_contact(request, id=None):
    # Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:
    contact = get_object_or_404(Users,id=id)
    if contact.executive==0:
        contact.executive = False
    if contact.executive_assistant==0:
        contact.executive_assistant = False
    if contact.active==0:
        contact.active = False
    if contact.admin==0:
        contact.admin = False
    form = ContactForm(request.POST or None, instance = contact)


    if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
#                 messages.success(request, "User Created : "+new_user.cas_user)
                return redirect("contact:detail", str(instance.pk))
    context ={ 
              'title' : 'Edit Contact',
              'form' : form,            
              }   
    return render(request,'contactForm.html', context)
    
    # else:
    #     return redirect('index')

def contact_search(request):
    # Commented out for testing purposes
    # if request.user.is_authenticated and 'current_user' in request.session:  
    nameForm = SearchContactForm(request.POST or None)
    departmentForm = SearchDepartmentForm(request.POST or None)
    positionForm = SearchPositionForm(request.POST or None)       
    
    context ={ 
              'nameForm' : nameForm,
              'departmentForm' : departmentForm,
              'positionForm' : positionForm
              }  
    return render(request, 'contactSearch.html', context)
    
    # else:
    #     return redirect('index')