from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url="login/")
def home(request):
  return TemplateResponse(request, "home.html")
	
def login_register(request):
  ctx = {}
  ctx['login_form'] = AuthenticationForm()
  ctx['register_form'] = UserCreationForm()
  
  if request.method == "POST":
    # initialize the forms with the POSTed data
    print('Test 1')
    if request.POST.get('login_submit'):
      print('Test 2')
      ctx['login_form'] = AuthenticationForm(request.POST)
      if ctx['login_form'].is_valid():
        print('Test 3')
        login(request, form.get_user())
        return HttpResponseRedirect(request.GET.get('next', '/'))
      
    elif request.POST.get('register_submit'):
      ctx['register_form'] = UserCreationForm(request.POST)
      if ctx['register_form'].is_valid():
        ctx['register_form'].save()
        user = authenticate(username=ctx['register_form'].cleaned_data['username'], password=ctx['register_form'].cleaned_data['password1'])
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', '/'))
        
  print('Final test')
  
  return TemplateResponse(request, "login.html", ctx)
  