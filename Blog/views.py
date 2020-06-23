from django.shortcuts import render, get_object_or_404
from .models import BlogInformation
# Create your views here.

def all_Blog(request):
    BlogDetails =  BlogInformation.objects.all()
    #BlogDetails =  BlogInformation.objects.order_by('-BlogDate')[:3]
    return render(request, 'BlogHome.html' , { 'BlogDetails' : BlogDetails } )

def Detail(request, Blog_id):
    Bloginfo = get_object_or_404(BlogInformation, pk=Blog_id )
    return render(request,'BlogDetails.html', { 'Bloginfo': Bloginfo })
