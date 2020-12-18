from django.shortcuts import render

# Create your views here.
def ckeditor(request):
    return render(request, "editor.html")