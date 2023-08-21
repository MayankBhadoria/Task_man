from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as loginuser, authenticate,logout
from taskman.models import todo
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404
User = get_user_model()
# Create your views here.
def home(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                loginuser(request, user)
                 
                return redirect('add')
        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context=context)


def signup(request):
    
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user = authenticate(username=username, password=password1)
                print(user)
                if user is not None:
                    loginuser(request, user)
                    return redirect('login')
            else:
                # Handle password mismatch error
                return HttpResponse("password didnt match")
                

        return render(request, 'signup.html')
 




def signout(request):
     logout(request)
     return redirect('login')


@login_required(login_url='login')
def add(request):
    user = request.user

    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        

        if title and status:
            new_todo = todo.objects.create(user=user, title=title, status=status)

            return redirect('add')  # Redirect to the same page to show the updated task list

    tasks = todo.objects.filter(user=user)  # Fetch tasks for the logged-in user
    context = {
        'tasks': tasks,
    }
    return render(request, 'add.html', context=context)


@login_required(login_url='login')
def delete(request,id):
    todo.objects.get(pk=id).delete()
    return redirect('add')


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')

        try:
            task = todo.objects.get(id=id)
            task.title = title
            task.status = status
            task.save()
            return redirect('add')
        except todo.DoesNotExist:
            pass

    return render(request, 'add.html')