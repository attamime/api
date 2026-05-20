from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView,ListView
from .serializers import studentserlizer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import student

class studentlistcreate(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentserlizer

class studentListView(ListView):
    model = student
    template_name = 'homee/home.html'
    context_object_name = 'stud'
 
class creat(CreateView):
    model=student
    fields=['name']
    template_name='homee/add.html'
    success_url = reverse_lazy('home')


#@login_required(login_url='login')
class edit_stu(UpdateView,
              LoginRequiredMixin,):
    model=student
    fields=['name']
    template_name='homee/edit.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class delete_stud(DeleteView):
    model=student
    template_name='homee/delete.html'
    success_url = reverse_lazy('home')


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
        else:
            # 🔥 هنا نعرض الأخطاء
            messages.error(request, "Please correct the errors below")

    else:
        form = UserCreationForm()

    return render(request, 'homee/register.html', {'form': form})
def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form = AuthenticationForm()

    # 🔥 مهم جدًا: لازم return دائمًا
    return render(request, 'homee/login.html', {'form': form})
            
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('login')
    
   
                


    
     




   

# Create your views here.
