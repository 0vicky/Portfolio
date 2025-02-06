from django.shortcuts import render
from .models import Portfolio, Skill, Project

def home(request):
    portfolio = Portfolio.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'portfolio': portfolio,
        'skills': skills,
        'projects': projects,
    })