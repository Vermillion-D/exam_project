from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import logging


from .forms import CleanLoginForm, CleanEditProfileForm, CleanSignUpForm, CleanPasswordChangeForm, ProfileDetailsForm

UserModel = get_user_model()


def base(request):
    return render(request, "web/base.html")


logger = logging.getLogger(__name__)


def user_login(request):
    if request.method == 'POST':
        form = CleanLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None and user.is_active:
                login(request, user)
                logger.info(f"User logged in: {user}")
                return redirect('about japan with profile')
    else:
        form = CleanLoginForm(request)

    context = {
        'form': form,
    }
    return render(request, 'web/login.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = CleanSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about japan with profile')
    else:
        form = CleanSignUpForm()

    context = {
        "form": form
    }
    return render(request, "web/sign_up.html", context=context)


@login_required
def profile_page(request):
    current_section = request.GET.get('section', 'details')

    profile_details_form = ProfileDetailsForm(instance=request.user)
    change_password_form = CleanPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if current_section == 'details':
            profile_details_form = ProfileDetailsForm(request.POST, instance=request.user)
            if profile_details_form.is_valid():
                profile_details_form.save()

        elif current_section == 'password':
            change_password_form = CleanPasswordChangeForm(user=request.user, data=request.POST)
            if change_password_form.is_valid():
                user = change_password_form.save()

    context = {
        'current_section': current_section,
        'profile_details_form': profile_details_form,
        'change_password_form': change_password_form,
    }
    return render(request, 'web/profile_page.html', context)


def about_japan(request):
    return render(request, "web/about_japan.html")


@login_required
def about_japan_with_profile(request):
    return render(request, "web/about_japan_with_profile.html")


def japanese_culture(request):
    return render(request, "web/japanese_culture.html")


def japanese_culture_with_profile(request):
    return render(request, "web/japanese_culture_with_profile.html")


def modern_japan(request):
    return render(request, "web/modern_japan.html")


def modern_japan_with_profile(request):
    return render(request, "web/modern_japan_with_profile.html")


def japanese_history(request):
    return render(request, "web/japanese_history.html")


def japanese_history_with_profile(request):
    return render(request, "web/japanese_history_with_profile.html")


@login_required
def emperors_overview(request):
    return render(request, "web/emperors_overview.html")


@login_required
def shogunates_overview(request):
    return render(request, "web/shogunates_overview.html")


@login_required
def samurai_overview(request):
    return render(request, "web/samurai_overview.html")


@login_required
def ninjas_overview(request):
    return render(request, "web/ninjas_overview.html")


def logout_view(request):
    logout(request)

    return redirect('about japan')


def specific_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email


@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('home page')

    return render(request, 'web/profile_delete.html')


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = CleanEditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile page')

    else:
        form = CleanEditProfileForm(instance=user)

    context = {
        'edit_form': form,
    }
    return render(request, "web/profile_page.html", context=context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('profile_page')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'current_section': 'password',
    }
    return render(request, 'web/profile_page.html', context)
