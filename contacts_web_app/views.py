from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from contacts_web_app.models_dup import Contact,Contacts,Loaddata
from contacts_web_app.models import add_contact_mod,provider





def page(request):
    return render(request, 'contacts_home.html')

def add_contact_form(request):
    message=''
    return render(request, 'add_contact.html', {'message':message})


def add_contact(request):

    if request.method == 'POST':
        try:
            name = request.POST['name']
        except MultiValueDictKeyError:
            name=False
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin_code']

        if add_contact_mod.objects.filter(phone_no=phone_no).exists():
            message='Contact already exist !!!!'
            return HttpResponse(message)
        else:
            add = add_contact_mod(name=name, phone_no=phone_no, email=email, street=street, city=city, state=state,
                                  pin_code=pin_code)
            add.save()

            message = 'Contact successfully added!'
            return HttpResponse(message)



def modify_contact_form(request):

    name = request.POST.get('name')


    phone_no = request.POST.get('phone_no')



    email = request.POST.get('email')



    street = request.POST.get('street')


    city = request.POST.get('city')


    state = request.POST.get('state')


    pin_code = request.POST.get('pin_code')

    return render(request, 'modify_contact.html', {'name': name, 'phone_no':phone_no, 'email':email, 'street':street, 'city':city, 'state':state,
                                                  'pin_code':pin_code})


def modify_contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone_no = request.POST['phone_no']
        email=request.POST['email']
        street=request.POST['street']
        city=request.POST['city']
        state=request.POST['state']
        pin_code=request.POST['pin_code']

        num=add_contact_mod.objects.get(phone_no=phone_no)
        num.name=name
        num.email=email
        num.street=street
        num.city=city
        num.state=state
        num.pin_code=pin_code
        num.save()

        message = 'Contact successfully modified!'
        return HttpResponse(message)





def delete_contact_form(request):
    message = ''
    return render(request, 'delete_contact.html', {'message':message})


def delete_contact(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        num=add_contact_mod.objects.get(phone_no=phone_no)
        if num:
            num.delete()
            message = 'Contact deleted successfully!'
            return HttpResponse(message)
        else:
            message = 'There is no contact with this phone number!'
            return HttpResponse(message)






def get_contact_form(request):
    message = ''
    return render(request, 'get_contact.html', {'message':message})


def get_contact(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']

        if add_contact_mod.objects.filter(phone_no=phone_no).exists():
            #details = contacts.get_contact(phone_no)
            details = add_contact_mod.objects.get(phone_no=phone_no)
            return render(request,'view_contact.html',{'contact':details})
        else:
            message = 'There is no contact with this phone number!'
            return render(request, 'get_contact.html', {'message': message})







def get_provider_form(request):
    message = ''
    return render(request, 'get_provider.html', {'message':message})


def get_provider(request):
    if request.method == 'POST':

        phone_no = request.POST['phone_no']
        try:
            provider_name = provider.objects.get(prov_list__contains=phone_no[0:4])

            if provider_name:
                message=provider_name.prov_name
                #return HttpResponse('Others!!!')
                return HttpResponse(message)
        except:
            return HttpResponse('Others!!!')



    else:
         message = 'Invalid phone number!'
         return HttpResponse(message)


def get_contacts_by_provider_form(request):
    message=''
    return render(request, 'get_contacts_by_provider.html')


def get_contacts_by_provider(request):
    if request.method == 'POST':
        provider_name = request.POST['provider']
        li=[]
        Provider=provider.objects.get(prov_name=provider_name)
        dta=add_contact_mod.objects.all()
        for x in dta:
            if x.phone_no[0:4] in Provider.prov_list:
                li.append(x)
        #records=add_contact_mod.objects.filter(phone_no__istartswith=Provider.prov_list)

       #records = contacts.get_contacts_by_provider(provider_name)
        if li:
            return render(request, 'view_contacts.html', {'contacts': li})

        else:
            message = 'no contacts exist!!!'
            return render(request, 'view_contacts.html', {'message': message})



def get_contacts_by_field_form(request):
    return render(request, 'get_contacts_by_field.html')



def get_contacts_by_field(request):
    if request.method == 'POST':
        string = request.POST.get('string')
        field = request.POST.get('field')
        if field == 'name':
           li=add_contact_mod.objects.filter(name__contains=string)
           return render(request, 'view_contacts.html', {'contacts': li})
        elif field == 'phone_no':
            li = add_contact_mod.objects.filter(phone_no__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})
        elif field == 'email':
            li = add_contact_mod.objects.filter(email__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})
        elif field == 'street':
            li = add_contact_mod.objects.filter(street__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})
        elif field == 'city':
            li = add_contact_mod.objects.filter(city__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})
        elif field== 'state':
            li = add_contact_mod.objects.filter(state__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})
        else:
            li = add_contact_mod.objects.filter(pin_code__contains=string)
            return render(request, 'view_contacts.html', {'contacts': li})








        #li = contacts.get_contacts_by_field(string, field)
        #return render(request, 'view_contacts.html', {'contacts':li})
