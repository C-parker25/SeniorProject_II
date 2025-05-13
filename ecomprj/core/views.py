from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import SubscriptionForm, VolunteerInterestForm,DonationForm
from .models import Subscription, Donation
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

User = settings.AUTH_USER_MODEL

# def register_view(request):

#     if request.method =="POST":
#         form = UserRegisterForm(request.POST or None)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get("username")
#             messages.success(request, f"Congratulations {username}. Your account has been created succesfully.")
#             new_user = authenticate(
#                 username=form.cleaned_data["email"],
#                 password=form.cleaned_data["password"]
#             )
#     else:
#         form = UserRegisterForm()

#     context = {
#         'form': form,
#     }
            

def index(request):
    return render('core/home.html')

def getinvolved_view(request):
    return render(request, "core/getinvolved.html")

def donate_view(request):
    success = False
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            recurring = request.POST.get("recurring") == "on"
            subscribe = request.POST.get("subscribe") == "on"


            Donation.objects.create(
                recurring=recurring,
                quick_subscribe=subscribe
            )
            
            subject = "We've recieved your Donation!"
            message = render_to_string('core/emails/donation_confirmation.html', {
                'donation': donation,
            })

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [donation.email],
                fail_silently=False,
            )

        return render(request, "core/donate.html", {'form': form, 'success': True})
    else:
        form = DonationForm()
        return render(request, "core/donate.html", {'form': form})

   

@csrf_protect
def subscribe_view(request):
    if request.method == "POST":
        email = request.POST.get("email_address")
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        consent = request.POST.get("consent") == "on"

        Subscription.objects.create(
            email=email,
            first_name=first,
            last_name=last,
            consent=consent
        )

        referer = request.META.get('HTTP_REFERER', '/subscribe/')
        return redirect(f'{referer}?success=true')

    success = request.GET.get('success') == 'true'
    return render(request, "core/subscribe.html", {"success": success})

def volunteer_view(request):
    success = False
    if request.method == 'POST':
        form = VolunteerInterestForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = VolunteerInterestForm()

    return render(request, 'core/volunteer.html', {'form': form, 'success': success})

def community_view(request):
    return render(request, "core/community.html")

def shop_view(request):
    pass

def cart_view(request):
    pass