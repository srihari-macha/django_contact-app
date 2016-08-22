from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from contacts_web_app.models_dup import Contact, Contacts, Loaddata

data = Loaddata()
contact_list = data.get_data_from_jsonfile()
contacts = Contacts(contact_list)


def page(request):
    return render(request, 'contacts_home.html')


def add_contact_form(request):
    message = ''
    return render(request, 'add_contact.html', {'message': message})


def add_contact(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
        except MultiValueDictKeyError:
            name = False
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin_code']

        is_contact_exist = contacts.is_contact_exist(phone_no)
        # is_valid_phone_no = contacts.is_valid_phone_no(phone_no)
        if (not is_contact_exist):  # and is_valid_phone_no:
            contact = Contact(name, phone_no, email, street, city, state, pin_code)
            contacts.add_contact(contact)
            contacts.save_contacts_to_file()
            message = 'Contact successfully added!'
            return HttpResponse(message)

        elif is_contact_exist:
            message = 'Contact already exists!'
            return HttpResponse(message)
        else:
            message = 'Invalid phone number!'
            return HttpResponse(message)


def modify_contact_form(request):
    name = request.POST.get('name')

    phone_no = request.POST.get('phone_no')

    email = request.POST.get('email')

    street = request.POST.get('street')

    city = request.POST.get('city')

    state = request.POST.get('state')

    pin_code = request.POST.get('pin_code')

    return render(request, 'modify_contact.html',
                  {'name': name, 'phone_no': phone_no, 'email': email, 'street': street, 'city': city, 'state': state,
                   'pin_code': pin_code})


def modify_contact(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            fields = request.POST
            contacts.modify_contact(phone_no, fields)
            contacts.save_contacts_to_file()
            message = 'Contact successfully modified!'
            return HttpResponse(message)
        else:
            message = 'There is no contact with this phone number!'
            return HttpResponse(message)


def delete_contact_form(request):
    message = ''
    return render(request, 'delete_contact.html', {'message': message})


def delete_contact(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            contacts.delete_contact(phone_no)
            contacts.save_contacts_to_file()
            message = 'Contact deleted successfully!'
            return HttpResponse(message)
        else:
            message = 'There is no contact with this phone number!'
            return HttpResponse(message)


def get_contact_form(request):
    message = ''
    return render(request, 'get_contact.html', {'message': message})


def get_contact(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        is_contact_exist = contacts.is_contact_exist(phone_no)
        if is_contact_exist:
            details = contacts.get_contact(phone_no)
            return render(request, 'view_contact.html', {'contact': details})
        else:
            message = 'There is no contact with this phone number!'
            return render(request, 'get_contact.html', {'message': message})


def get_provider_form(request):
    message = ''
    return render(request, 'get_provider.html', {'message': message})


def get_provider(request):
    if request.method == 'POST':
        phone_no = request.POST['phone_no']
        provider_name = contacts.get_provider(phone_no[0:4])
        message = provider_name
        return HttpResponse(message)
    else:
        message = 'Invalid phone number!'
        return HttpResponse(message)


def get_contacts_by_provider_form(request):
    message = ''
    return render(request, 'get_contacts_by_provider.html')


def get_contacts_by_provider(request):
    if request.method == 'POST':
        provider_name = request.POST['provider']
        records = contacts.get_contacts_by_provider(provider_name)
        if records:
            return render(request, 'view_contacts.html', {'contacts': records})

        else:
            message = 'no contacts exist!!!'
            return render(request, 'view_contacts.html', {'message': message})


def get_contacts_by_field_form(request):
    return render(request, 'get_contacts_by_field.html')


def get_contacts_by_field(request):
    if request.method == 'POST':
        string = request.POST.get('string')
        field = request.POST.get('field')
        li = contacts.get_contacts_by_field(string, field)
        return render(request, 'view_contacts.html', {'contacts': li})
