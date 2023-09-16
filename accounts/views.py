from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.

class UserRegisterView(View):
    template_name = 'users/register.html'
    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f"Your account has been created! You can login now {username}")
            return redirect("login")
        context = {"form":form}
        return render(
            request=request,
            template_name=self.template_name,
            context=context
        )
            