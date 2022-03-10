from django.shortcuts import render

# Create your views here.

def index(request):
    """前端练习页目录
        返回: 页面列表
    """
    return render(request,'fePractice/index.html')

def extendCard(request):
    """延伸卡片
    """
    return render(request,'fePractice/extendCard.html')