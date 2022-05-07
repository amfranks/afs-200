from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def show_all_contacts(request):
    try:
        contacts = Contact.objects.all()
        if contacts.count() > 0:
            content = {'contacts': contacts}
            return render(request, 'index.html', content)
            #return HttpResponse(f'<h1>Display all your contacts</h1>')
        else:
            return HttpResponse(f'<h1>Unable to locate any contacts in our database.</h1>')
    except: 
        return HttpResponse(f'<h1>Unable to display the contacts in our database.</h1>')    
    
def show_contact(request,contactid):
    try:
        contact = Contact.objects.get(id=contactid) 
        return render(request, 'index.html', {'contacts': [contact]})
        #return HttpResponse(f'<h1>Showing more details for "{contact}"</h1>')
    except Contact.DoesNotExist:
        return HttpResponse(f'<h1>Unable to locate product whose id is {contactid}</h1>')       
       