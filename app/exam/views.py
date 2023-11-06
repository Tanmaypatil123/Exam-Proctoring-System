from django.shortcuts import render
# from exam.forms import UserModelForm
# Create your views here.

def home(request):
    return render(request,"exam/index.html")

# def register(request):
#     context = {}

#     form = UserModelForm(
#         request.POST or None
#     )

#     if form.is_valid():
#         form.save()

#     context['form'] = form

#     return render(request,"exam/register.html",context)