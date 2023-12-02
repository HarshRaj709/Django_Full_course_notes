from django.shortcuts import render

# Create your views here.
def skills(request):
    context = {'skills':'active'}
    return render(request,'edu/skill.html',context)