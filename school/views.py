from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import photo,Event,SchoolCal,testimonials,Term,term_events,Gallery
from .forms import photoform,ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseForbidden



SECRET_TOKEN = "secure-token-12345"  

def superuser_access(request):
    token = request.GET.get('token', '')
    
    if token != SECRET_TOKEN:
        return HttpResponseForbidden("Access Denied!")
    
    # Store the token in the session
    request.session['superuser_token'] = token
    return redirect('/superuser-panel/')


def index(request):
    c_events = SchoolCal.objects.all()
    terms = Term.objects.prefetch_related('events').all()
    context = {
        'c_events': c_events,
        'terms': terms,
         }
    return render(request,'index.html',context)

def gallery_view(request):
    photos = photo.objects.all()
    return render(request,'gallery.html',{'photos':photos})

def upload_photo(request):
    if request.method == 'POST':
        form = photoform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
        
def download_pdf(request):
    return render(request, 'index.html')

def event_list(request):
    events = Event.objects.all()
    
    context = {
        
        'events': events  }
    return render(request, 'events.html', context)

def testimonials_view(request):
    testsms = testimonials.objects.all()
    print(testsms)
    context = {
        'testsms':testsms
    }
    return render(request, 'testimonials.html', context)



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            subject = 'Contact Form Submission'
            message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                message_body,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # The email address to receive the form submissions
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

# views.py
from django.shortcuts import render
from .models import testimonials  # Ensure this is the correct import path

def tlc_view(request):
    return render(request,'tlc.html')

def startaford_view(request):
    return render(request,'strataford.html')

def gallery_list(request): 
    galleries = Gallery.objects.all() 
    return render(request, 'gallery_list.html', {'galleries': galleries}) 

def gallery_detail(request, pk):
     gallery = Gallery.objects.get(pk=pk) 
     return render(request, 'gallery_detail.html', {'gallery':gallery})


