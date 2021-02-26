from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'facial/gallery.html')
    
def viewPhoto(request):
    return render(request, 'facial/photo.html')
    
def addPhoto(request):
    return render(request, 'facial/add.html')