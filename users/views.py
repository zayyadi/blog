from base64 import urlsafe_b64decode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site

from .forms import ProfileUpdateForm, UserUpdateForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from users.models import Profile
from django.http import JsonResponse
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
# from django.utils.encoding import force_bytes, force_str
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string
# from .token import account_activation_token
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.http import HttpResponse


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            form.save()
            # current_site = get_current_site(request)
            # mail_subject = "Activation link has been sent to your email id"
            # message = render_to_string(
            #     "acc_active_email.html",
            #     {
            #         "user": user,
            #         "domain": current_site.domain,
            #         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            #         "token": account_activation_token.make_token(user),
            #     },
            # )
            # to_email = form.cleaned_data.get("email")
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()
            # email.send()
            # return HttpResponse(
            #     "Please confirm your email address to complete the registration"
            # )
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_b64decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")


def logout_view(request):
    logout(request)
    return render(request, "users/logout.html")


def social(request):
    return render(request, "users/social.html")


@login_required
def profile(request):
    created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("users:profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "users/profile.html", context)


@login_required
def view_profile(request, user_id):
    user = get_object_or_404(Profile, user_id=user_id)
    return render(request, "users/view_profile.html", {"user": user})


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider="github")
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider="twitter")
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider="facebook")
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = user.social_auth.count() > 1 or user.has_usable_password()

    return render(
        request,
        "users/settings.html",
        {
            "github_login": github_login,
            "twitter_login": twitter_login,
            "facebook_login": facebook_login,
            "can_disconnect": can_disconnect,
        },
    )


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == "POST":
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("password")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordForm(request.user)
    return render(request, "users/password.html", {"form": form})


def validate_username(request):
    """Check username availability"""
    username = request.GET.get("username", None)
    response = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(response)
