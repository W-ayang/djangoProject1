from django.shortcuts import render, HttpResponse,redirect

# Create your views here.

def index(request):
    return HttpResponse('欢迎使用！')

def user_list(request):
    #去app目录下的templates目录寻找user_list(根据app的注册顺序，逐一去他们的templates目录寻找)
    return render(request,"user_list.html")

def user_add(request):
    return render(request,'user_add.html')

def tpl(request):

    name = '马超'
    roles = ["管理员","CEO","保安"]
    user_info = {"name":"阿杨","salary":100000000}
    data_list = [
        {"name":"阿杨","salary":100000000},
        {"name": "柳神", "salary": 100000000},
        {"name": "鬼爷", "salary": 100000000}
    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info,"n4":data_list})

def news(request):
    #1. 定义一些新闻（字典或列表）或 去数据库 网络请求去联通新闻
    # 向地址：
    #第三方模块：requests
    import requests
    res = requests.get("http://127.0.0.1:8080/tpl/")
    data_list = res.json()
    print(data_list)
    return render(request,'news.html')

def something(request):
    # request是一个对象，封装了用户通过浏览器发送过来的所有请求数据
    # 1.获取请求方式
    #print(request.method)

    # 2.在URL上传递一些值
    #print(request.GET)

    # 3.在请求中提交数据
    #print(request.POST)

    # 4.【响应】HttpResponse()，内容字符串返回给请求者
    #return HttpResponse("返回内容")

    #5. 【响应】读取HTML的内容 + 渲染（替换）->字符串，返回给用户浏览器。
    #return render(request,'something.html')

    # 6.【响应】让浏览器重定向到其他页面,这时浏览器和Django网站没有关系，是浏览器直接跳转到百度了
    return redirect("https://www.baidu.com")

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")

    #如果是POST请求，获取用户提交的数据
    #print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == '123':
        #return HttpResponse('登录成功')
        return redirect("https://www.google.com/search?q=%E4%BD%A0%E5%9C%A8%E7%8B%97%E5%8F%AB%E4%BB%80%E4%B9%88&oq=%E4%BD%A0%E5%9C%A8%E7%8B%97%E5%8F%AB%E4%BB%80%E4%B9%88&aqs=chrome.0.0i355i512j46i512j0i512l8.4502j0j15&sourceid=chrome&ie=UTF-8")

    #return HttpResponse("登录失败")
    return render(request,"login.html", {"error_msg":"用户名或密码错误"})

from app01.models import UserInfo
def orm(request):
#
      UserInfo.objects.create(name = '销售部',password=123)
      #UserInfo.objects.all().delete()
#     data_list = UserInfo.objects.all()
#     print(data_list)
#     for obj in data_list:
#         print(obj.name,obj.password,obj.age)
#
#     # obj = UserInfo.objects.filter(name='销售部').first()
#     # print(obj.name, obj.password, obj.age)
#
      return HttpResponse('成功')


def info_list(request):
    # 获取数据库中所有用户的信息
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request,'info_list.html',{'data_list':data_list})

def info_add(request):
    if request.method == 'GET':
        return render(request,'info_add.html')

    #获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')

    # #添加到数据库
    UserInfo.objects.create(name=user,password=pwd,age=age)

    #添加成功后自动跳转到数据库表单那个网页
    return redirect('http://127.0.0.1:8080/info/list/')
    #return HttpResponse('添加成功')

def depart_list(request):


    return render(request,'depart_list.html')


