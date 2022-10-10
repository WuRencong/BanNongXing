from django.shortcuts import render, get_object_or_404
# from BNX_Website.models import New, NewType, Liaison_cooperation, information
# from BanNongXing.BNX_Website.models import New, NewType, Liaison_cooperation, information

from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from .models import SeedMess, seedImg, SoilMess, SubClassMess, SoilSeedMess,New,NewType,Liaison_cooperation,information
from django.http import HttpResponse, JsonResponse
import os
import json
import requests


# Create your views here.
def getMasterTemplate(request):
    """
        用途： 返回通用页面模板页面
        参数：
            request: Django内置请求参数
        返回值： 返回渲染页面
        作者： 曾韶程
        日期： 2021：05：25，15：12
    """
    return render(request, 'PageHeadAndTailCommon.html')


def getAboutUsPage(request):
    """
        用途： 返回关于我们页面
        参数：
            request: Django内置请求参数
        返回值： 返回关于我们渲染页面
        作者： 曾韶程
        日期： 2021：05：25，15：37
    """
    return render(request, 'About_us.html')


def getActionnewsPage(request):
    """
        用途： 返回关于新闻快报页面
        参数：
            request: Django内置请求参数
        返回值： 返回关于新闻快报页面
        作者： 曾韶程
        日期： 2021：05：25，15：37
    """
    new_type_list = NewType.objects.all()

    newType_one_list = New.objects.filter(new_type=new_type_list[0])[:5]
    newType_two_list = New.objects.filter(new_type=new_type_list[1])[:5]
    newType_thr_list = New.objects.filter(new_type=new_type_list[2])[:5]
    newType_fou_list = New.objects.filter(new_type=new_type_list[3])[:5]

    new_list_list = (newType_one_list, newType_two_list, newType_thr_list, newType_fou_list)

    content = {
        'new_type_list': new_type_list,
        'new_list_list': new_list_list
    }

    return render(request, 'ActionNews.html', content)


def gatNewTemPage(request, new_pk):
    """
            用途： 返回新闻模板页面
            参数：
                request: Django内置请求参数
            返回值： 返回关于新闻模板页面
            作者： 曾韶程
            日期： 2021：05：25，15：37
    """
    # 获取新闻类型模板页面

    content = {
        'new': get_object_or_404(New, pk=new_pk),
        'previous': New.objects.filter(id__lt=new_pk).first(),
        'previous_list': New.objects.filter(id__lt=new_pk),
        'next': New.objects.filter(id__gt=new_pk).last(),
        'next_list': New.objects.filter(id__gt=new_pk),
        'new_list': New.objects.all(),
    }
    return render(request, 'new_tem.html', content)


def gatNewTypeTemPage(request, new_type_pk):
    """
        用途： 返回新闻根模板页面
        参数：
            request: Django内置请求参数
        返回值： 返回关于新闻根模板页面
        作者： 曾韶程
        日期： 2021：05：25，15：37
    """
    # 获取新闻类型模板页面
    new_type = get_object_or_404(NewType, pk=new_type_pk)

    # 获得页码参数（GET请求）
    page_num = request.GET.get("page", 1)
    new_all = New.objects.filter(new_type=new_type)

    # 每 EACH_PAGE_NEWS_NUMB 篇新闻一页
    paginator = Paginator(new_all, settings.EACH_PAGE_NEWS_NUMB)
    page_of_news = paginator.get_page(page_num)

    # 获得当前页
    current_page_num = page_of_news.number

    # 获得当前页周围两页的 SURROUNDING_PAGE_NUM 个页面数
    current_page_range = list(range(
        max(current_page_num - settings.SURROUNDING_PAGE_NUM, 1),
        min(paginator.num_pages + 1, current_page_num + settings.SURROUNDING_PAGE_NUM + 1)
    ))

    # 加上省略号页面标记
    if current_page_range[0] - 1 >= settings.SURROUNDING_PAGE_NUM:
        current_page_range.insert(0, '...')

    if paginator.num_pages - current_page_range[-1] >= settings.SURROUNDING_PAGE_NUM:
        current_page_range.append('...')

    # 显示第一页和最后一页
    if current_page_range[0] != 1:
        current_page_range.insert(0, 1)

    if current_page_range[-1] != paginator.num_pages:
        current_page_range.append(paginator.num_pages)

    # 设定传输报文
    content = {
        'new_list': New.objects.filter(new_type=new_type),
        'new_type': new_type,
        'current_page_range': current_page_range,
        'page_of_news': page_of_news,
    }

    return render(request, 'new_type_tem.html', content)


def search(request, crop_type_name):
    """
        用途： 返回搜索引擎页面及搜索到的作物
        参数：
            request: Django内置请求参数
        返回值： 返回种子和土壤数据渲染页面
        作者： 曾韶程
        日期： 2021：09：21，9：40s
    """
    keyword = request.GET.get('keyword')
    if crop_type_name == 'seed':
        seedList = SeedMess.objects.all().values().filter(anotherName__icontains=keyword)
        seedImgUrlList = seedImg.objects.all().values()
        for img in seedImgUrlList:
            imgurl = img['photo'].split(",")[0]
            for seed in seedList:
                if seed['id'] == img['seed_id']:
                    seed['photo'] = imgurl
                    break
                    
        seedName = '关于' + '\"' + keyword + '\"' + '的搜索结果'
        return render(request, 'search_seed.html', {
            'seedName': seedName,
            'seedList': seedList
        })
    else:
        soilList = SoilMess.objects.filter(soilName__icontains=keyword)
        soilName = '关于' + '\"' + keyword + '\"' + '的搜索结果'
        return render(request, 'search_soil.html', {
            'soilName': soilName,
            'soilList': soilList
        })


def getSeedMess(request, crop_type_name):
    """
        用途： 返回种子和土壤的数据页面
        参数：
            request: Django内置请求参数
        返回值： 返回种子和土壤数据渲染页面
        作者： 曾韶程
        日期： 2021：07：04，9：40s
    """
    if crop_type_name == 'seed':
        # .values()获取到的结果集是<QuerySet [{'id':3, ...}]>的形式
        seedList = SeedMess.objects.all().values().order_by('-created_time')
        seedImgUrlList = seedImg.objects.all().values()

        for img in seedImgUrlList:
            imgurl = img['photo'].split(",")[0]
            for seed in seedList:
                if seed['id'] == img['seed_id']:
                    seed['photo'] = imgurl
                    break

        p = Paginator(seedList, 3)
        if p.num_pages <= 1:
            pageData = {}
        else:
            page = int(request.GET.get('page', 1))
            seedList = p.page(page)
            left = []
            right = []
            left_has_more = False
            right_has_more = False
            first = False
            last = False
            total_pages = p.num_pages
            page_range = p.page_range
            if page == 1:
                right = page_range[page:page + 2]
                back = False
                next = True
                if right[-1] < total_pages - 1:
                    right_has_more = True
                if right[-1] < total_pages:
                    last = True
            elif page == total_pages:
                left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
                next = False
                back = True
                if left[0] > 2:
                    left_has_more = True
                if left[0] > 1:
                    first = True
            else:
                back = True
                next = True
                left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
                right = page_range[page:page + 2]
                if left[0] > 2:
                    left_has_more = True
                if left[0] > 1:
                    first = True
                if right[-1] < total_pages - 1:
                    right_has_more = True
                if right[-1] < total_pages:
                    last = True

            pageData = {
                'left': left,
                'right': right,
                'left_has_more': left_has_more,
                'right_has_more': right_has_more,
                'first': first,
                'back': back,
                'last': last,
                'next': next,
                'total_pages': total_pages,
                'page': page,
                'backPage': page - 1,
                'nextPage': page + 1
            }

        return render(request, 'Seeds.html', {
            'seedList': seedList,
            'pageData': pageData,
        })
    elif crop_type_name == 'soil':
        soilList = SoilMess.objects.all().values().order_by('-createdTime')
        p = Paginator(soilList, 4)
        if p.num_pages <= 1:
            pageData = {}
        else:
            page = int(request.GET.get('page', 1))
            soilList = p.page(page)
            left = []
            right = []
            left_has_more = False
            right_has_more = False
            first = False
            last = False
            total_pages = p.num_pages
            page_range = p.page_range
            if page == 1:
                right = page_range[page:page + 2]
                back = False
                next = True
                if right[-1] < total_pages - 1:
                    right_has_more = True
                if right[-1] < total_pages:
                    last = True
            elif page == total_pages:
                left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
                next = False
                back = True
                if left[0] > 2:
                    left_has_more = True
                if left[0] > 1:
                    first = True
            else:
                back = True
                next = True
                left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
                right = page_range[page:page + 2]
                if left[0] > 2:
                    left_has_more = True
                if left[0] > 1:
                    first = True
                if right[-1] < total_pages - 1:
                    right_has_more = True
                if right[-1] < total_pages:
                    last = True
            pageData = {
                'left': left,
                'right': right,
                'left_has_more': left_has_more,
                'right_has_more': right_has_more,
                'first': first,
                'back': back,
                'last': last,
                'next': next,
                'total_pages': total_pages,
                'page': page,
                'backPage': page - 1,
                'nextPage': page + 1
            }
        return render(request, 'soils.html', {
            'soilList': soilList,
            'pageData': pageData,
        })


def getSeedDetail(request, crop_seed_id):
    """
        用途： 返回种子的详情页面
        参数：
            request: Django内置请求参数
        返回值： 返回空白渲染页面
        作者： 曾韶程
        日期： 2021：09：19，07：40
    """
    currentSeed = get_object_or_404(SeedMess, id=crop_seed_id)
    currentSeed.hits += 1
    currentSeed.save()
    seedList = SeedMess.objects.all().values().order_by('-hits')[0:3]
    t = SeedMess.objects.all().values().get(id=crop_seed_id)
    seedImgUrlList = seedImg.objects.all().values()
    imgList = []
    for seed in seedList:
        if seed['id'] == t['id']:
            seedList = SeedMess.objects.all().values().order_by('-hits')[0:4]
            idx = 0
            for s in seedList:
                if s['id'] == t['id']:
                    seedList = seedList[0:idx] + seedList[idx+1:len(seedList)]
                idx+=1
            break

    for img in seedImgUrlList:
        imgurl = img['photo'].split(",")
        imgurl = imgurl[0:len(imgurl)-1]
        if len(imgurl) >= 2:
            imgurl = imgurl[0:3]
        if img['id'] == t['id']:
            imgList = imgurl
            break
    
    for img in seedImgUrlList:
        imgurl = img['photo'].split(",")[0]
        for seed in seedList:
            if seed['id'] == img['seed_id']:
                seed['photo'] = imgurl
                break

    return render(request, 'SeedDetail.html', {
        'currentSeed': currentSeed,
        'seedList': seedList,
        'imgList': imgList
    })


def getSoilDetail(request, crop_soil_id):
    """
        用途： 返回土壤的详情页面
        参数：
            request: Django内置请求参数
        返回值： 返回空白渲染页面
        作者： 曾韶程
        日期： 2021：09：19，20：40
    """
    currentsoil = get_object_or_404(SoilMess, id=crop_soil_id)
    currentsoil.hits += 1
    currentsoil.save()

    currentsubsoils = SubClassMess.objects.all().values().filter(subgroupId=crop_soil_id)

    return render(request, 'SoilDetail.html', {
        'soilName': currentsoil.soilName,
        'soilEngName': currentsoil.soilEngName,
        'soilClassName': currentsoil.soilClassName,
        'soilClassEngName': currentsoil.soilClassEngName,
        'soilDescription': currentsoil.soilDescription,
        'currentSoil': currentsoil,
        'currentsubsoils': currentsubsoils
    })


def getSubSoil(request, subsoil_id):
    """
        用途： 返回土壤亚类的分类页面
        参数：
            request: Django内置请求参数
        返回值： 返回空白渲染页面
        作者： 曾韶程
        日期： 2021：11：04，15：59
    """
    currentsoil = get_object_or_404(SubClassMess, id=subsoil_id)
    currentsoil.hits += 1
    currentsoil.save()
    currentsoilseeds = SoilSeedMess.objects.all().values().filter(soilSeedId=subsoil_id)
    return render(request, 'SoilSubclass.html', {
        'subClassName': currentsoil.subClassName,
        'subClassEngName': currentsoil.subClassEngName,
        'subClassNatName': currentsoil.subClassNatName,
        'currentSoil': currentsoil,
        'currentsoilseeds': currentsoilseeds
    })


def getSoilSeed(request, soil_seed_id):
    """
        用途： 返回土种详情页面
        参数：
            request: Django内置请求参数
        返回值： 返回空白渲染页面
        作者： 曾韶程
        日期： 2021：11：04，21：54
    """
    currentsoil = get_object_or_404(SoilSeedMess, id=soil_seed_id)
    currentsoil.hits += 1
    currentsoil.save()
    return render(request, 'SoilseedDetail.html', {
        'soilSeedName': currentsoil.soilSeedName,
        'soilSeedDescript': currentsoil.soilSeedDescript,
        'distributionLandform': currentsoil.distributionLandform,
        'areaHectare': currentsoil.areaHectare,
        'areaMu': currentsoil.areaMu,
        'material': currentsoil.material,
        'configuration': currentsoil.configuration,
        'effectSoilDepth': currentsoil.effectSoilDepth,
        'mainCharacters': currentsoil.mainCharacters,
        'barrierFactor': currentsoil.barrierFactor,
        'productPerformance': currentsoil.productPerformance,
        'landUse': currentsoil.landUse

    })


def getCreatePage(request):
    """
        用途： 返回创建成功页面
        参数：
            request: Django内置请求参数
        返回值： 返回空白渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    return render(request, 'create.html')


def getMapPage(request):
    """
        用途： 返回位置地图页面
        参数：
            request: Django内置请求参数
        返回值： 返回位置地图渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    return render(request, 'map.html')


def getDataPlanPage(req):
    """
        用途： 返回数据规划页面
        参数：
            request: Django内置请求参数
        返回值： 返回数据规划渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    mapPath = os.path.join(os.getcwd(), 'static/map/china.json')
    with open(mapPath, 'rb') as f:
        data = json.load(f) # 获取到的数据时字典格式
    data = json.dumps(data)
    return render(req, 'DataPlanning.html', {
        'mapData': data
    })


def getProductCenterPage(request):
    """
        用途： 返回产品中心页面
        参数：
            request: Django内置请求参数
        返回值： 返回产品中心渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    return render(request, 'ProductCenter.html')


def getLoginPage(request):
    """
        用途： 返回登陆页面
        参数：
            request: Django内置请求参数
        返回值： 返回登陆渲染页面
        作者： 兰可易
        日期： 2021：05：03，20：40
    """
    # 读取 POST 表单数据
    # 登陆表单
    login_User = request.POST.get('login_User', '')
    login_Password = request.POST.get('login_Password', '')
    # 重设表单
    reset_user = request.POST.get('reset_user', '')
    reset_email = request.POST.get('reset_email', '')
    reset_password = request.POST.get('reset_password', '')
    reset_password_again = request.POST.get('reset_password_again', '')
    # 注册表单
    registered_user = request.POST.get('registered_user', '')
    registered_Password = request.POST.get('registered_Password', '')
    registered_Email = request.POST.get('registered_Email', '')

    content ={}
    # 登陆验证
    log_user = auth.authenticate(username=login_User, password=login_Password)
    if log_user:
        auth.login(request, log_user)
        request.session['username'] = log_user.username
        # 设置保持登录时间  参数0表示Cookie将在用户的浏览器关闭时过期，
        # None表示永不过期，整数表示在多少秒后过期
        request.session.set_expiry(0)
        content = {
            'ha': 'ha'
        }

    # 注册账号
    if registered_user and registered_Password and registered_Email:
        reg_user = User.objects.create_user(
            registered_user,
            registered_Email,
            registered_Password,
        )
        reg_user.is_staff = False
        reg_user.save()

    # 重设密码
    if reset_user and reset_email and reset_password and reset_password_again:
        res_user = User.objects.get(username__exact=reset_user)
        res_user.set_password(reset_password_again)
        res_user.save()

    return render(request, 'load.html', content)


def getLiaisonPage(request):
    """
        用途： 返回联系合作页面
        参数：
            request: Django内置请求参数
        返回值： 返回联系合作渲染页面
        作者： 兰可易
        日期： 2021：05：03，20：40
    """
    # 读取 POST 表单数据
    User_name = request.POST.get('User_name', '')
    Company_name = request.POST.get('Company_name', '')
    Telephone = request.POST.get('Telephone', '')
    Types_section = request.POST.get('Types_section', '')
    Project_description = request.POST.get('Project_description', '')

    # 将表单数据添加到后台数据库
    if User_name and Company_name and Telephone and Types_section and Project_description:
        Liaison = Liaison_cooperation(
            User_name=User_name,
            Company_name=Company_name,
            Telephone=Telephone,
            Types_section=Types_section,
            Project_description=Project_description
        )
        Liaison.save()

    return render(request, 'Liaison_cooperation.html', {
        'User_name': User_name,
        'Company_name': Company_name,
        'Telephone': Telephone,
        'Types_section': Types_section,
        'Project_description': Project_description,
    })


def getLegalPage(request):
    """
        用途： 返回法律声明页面
        参数：
            request: Django内置请求参数
        返回值： 返回法律声明渲染页面
        作者： 兰可易
        日期： 2021：05：03，20：40
    """
    return render(request, 'Legal_statement.html')


def getInformationPage(request):
    """
        用途： 返回信息反馈页面
        参数：
            request: Django内置请求参数
        返回值： 返回信息反馈渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    # 读取 POST 表单数据
    Whether_helps = request.POST.get('Whether_helps', '')
    Detailed = request.POST.get('Detailed', '')
    Humanize = request.POST.get('Humanize', '')
    Provide = request.POST.get('Provide', '')
    Other = request.POST.get('Other', '')

    if Whether_helps and Detailed and Humanize and Provide and Other:
        infor = information(
            Whether_helps=Whether_helps,
            Detailed=Detailed,
            Humanize=Humanize,
            Provide=Provide,
            Other=Other
        )
        infor.save()

    return render(request, 'InformationFeedback.html', {
        'Whether_helps': Whether_helps,
        'Detailed': Detailed,
        'Humanize': Humanize,
        'Provide': Provide,
        'Other': Other,
    })


def getIndexPage(request):
    """
        用途： 返回主页页面
        参数：
            request: Django内置请求参数
        返回值： 返回主页渲染页面
        作者： 曾韶程
        日期： 2021：05：03，20：40
    """
    return render(request, 'index.html')
