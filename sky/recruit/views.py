from django.shortcuts import render,render_to_response
from .models import Students

def recruit(request):
    if request.method == 'POST':
        name = request.POST['name']
        major = request.POST['major']
        grade = request.POST['grade']
        introduction = request.POST['intro']
        selfMedia = request.POST['qq/wechat']
        phone = request.POST['phone']
        depart = request.POST['job']
        Students.objects.create(name = name,
                                major=major,
                                grade=grade,
                                introduction = introduction,
                                selfMedia=selfMedia,
                                phone=phone,
                                depart=depart,
                                )
        return render_to_response('success.html', )

    else:
        return render_to_response('index.html', )
