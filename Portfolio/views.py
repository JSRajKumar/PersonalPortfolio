from django.shortcuts import render
from .models import PortfolioModel
# Create your views here.


def Hompage(request):
    PortfolioMdl = PortfolioModel.objects.all()
    return render(request, 'Homepage.html',{'PortfolioModels' : PortfolioMdl})