from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Liaison_cooperation(models.Model):
    id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=30, verbose_name='客户姓名')
    Company_name = models.CharField(max_length=30, verbose_name='单位名称')
    Telephone = models.CharField(max_length=20, verbose_name='联系电话')
    Types_section = models.CharField(max_length=15, verbose_name='合作类型')
    Project_description = models.TextField(verbose_name='项目描述')

    def __str__(self):
        return self.User_name


class information(models.Model):
    id = models.AutoField(primary_key=True)
    Whether_helps = models.CharField(max_length=30, verbose_name='设计方案是否有帮助')
    Detailed = models.CharField(max_length=30, verbose_name='设计方案是否详细')
    Humanize = models.CharField(max_length=30, verbose_name='网站设计是否足够人性化')
    Provide = models.CharField(max_length=80, verbose_name='还需要提供什么服务功能')
    Other = models.TextField(verbose_name='其他想法')

    def __str__(self):
        return self.Whether_helps


class NewType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class New(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name='新闻标题')
    new_type = models.ForeignKey(NewType, on_delete=models.DO_NOTHING, verbose_name='新闻类型')
    image = models.ImageField(upload_to='', verbose_name='图片', blank=True)
    content = models.TextField(verbose_name='新闻内容')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='新闻作者')
    quote = models.TextField(default='', verbose_name='引用', blank=True)
    url = models.URLField(verbose_name='引用链接', blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    hits = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return "<New: %s>" % self.title

    class Meta:
        ordering = ['-created_time']


class SeedMess(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)

    Mesogastropoda = models.CharField(max_length=50, verbose_name='中文科名')
    Littorinidae = models.CharField(max_length=50, verbose_name='中文属名')
    anotherName = models.CharField(max_length=50, verbose_name='别名')
    morphological = models.TextField(max_length=1500, verbose_name='形态特征')
    Geographic = models.TextField(max_length=1500, verbose_name='地理环境及基本生长环境')
    EdibleParts = models.TextField(max_length=50, verbose_name='食用部位')
    seedProductionTechnique = models.TextField(max_length=1500, verbose_name='制种技术')
    seedMorphological = models.TextField(max_length=1500, verbose_name='种子形态')
    germination = models.TextField(max_length=1500, verbose_name='萌发条件')
    drying = models.TextField(max_length=1500, verbose_name='干燥条件')
    StorageAndLife = models.TextField(max_length=1500, verbose_name='储藏和寿命')
    processingMethod = models.TextField(max_length=5100, verbose_name='加工方法')
    identificationMethods = models.TextField(max_length=1500, verbose_name='质量检测和简易鉴别方法')
    SowingPeriod = models.TextField(max_length=1500, verbose_name='播种期、生长期')
    cultivationMeasure = models.TextField(max_length=1500, verbose_name='栽培措施')
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    hits = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return "<SeedMess: %s>" % self.Mesogastropoda

    class Meta:
        verbose_name = u'种子'
        verbose_name_plural = u'种子'
        ordering = ['-created_time']


class seedImg(models.Model):
    seed = models.ForeignKey(SeedMess,
                             related_name='seedImgs',
                             verbose_name='种子',
                             on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='',
                              blank=True,
                              verbose_name='种子图片', )

    class Meta:
        verbose_name = '种子图片'
        verbose_name_plural = '种子图片'


# 土类表
class SoilMess(models.Model):
    id = models.AutoField(primary_key=True)
    soilName = models.CharField(max_length=50, verbose_name='土类名称', blank=True, default='', null=True)
    soilEngName = models.CharField(max_length=50, verbose_name='土类英文名', blank=True, default='', null=True)
    soilClassName = models.CharField(max_length=50, verbose_name='土纲名称', blank=True, default='', null=True)
    soilClassEngName = models.CharField(max_length=50, verbose_name='土纲英文名', blank=True, default='', null=True)
    soilDescription = models.TextField(max_length=5000, verbose_name='土类描述', blank=True, default='', null=True)
    createdTime = models.DateTimeField(verbose_name='创建时间', default=timezone.now, blank=True, null=True)
    hits = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return "<SoilMess: %s>" % self.soilName

    class Meta:
        verbose_name = '土类信息'
        verbose_name_plural = '土类信息'
        ordering = ['-createdTime']


# 亚类表
class SubClassMess(models.Model):
    # 主键
    id = models.AutoField(primary_key=True)
    # subgroupId 外键与 SoilMess 的主键一致
    subgroupId = models.ForeignKey('SoilMess', on_delete=models.CASCADE)
    subClassName = models.CharField(max_length=50, verbose_name='亚类名称', blank=True, default='', null=True)
    subClassEngName = models.CharField(max_length=50, verbose_name='亚类英文名', blank=True, default='', null=True)
    subClassNatName = models.CharField(max_length=50, verbose_name='亚类国标名', blank=True, default='', null=True)
    createdTime = models.DateTimeField(verbose_name='创建时间', default=timezone.now, blank=True, null=True)
    hits = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return "<SubClassMess: %s>" % self.subClassName

    class Meta:
        verbose_name = '亚类信息'
        verbose_name_plural = '亚类信息'
        ordering = ['-createdTime']


# 土种表
class SoilSeedMess(models.Model):
    # 主键
    # Soil_id
    id = models.AutoField(primary_key=True)
    # soilSeedId 外键与 SubClassMess 的主键一致
    # 这个id不确定
    soilSeedId = models.ForeignKey('SubClassMess', on_delete=models.CASCADE)
    # Soil_type_name
    soilSeedName = models.CharField(max_length=50, verbose_name='土种名称', blank=True, default='', null=True)
    # Description
    soilSeedDescript = models.TextField(max_length=2000, verbose_name='描述', blank=True, default='', null=True)
    # Landform
    distributionLandform = models.TextField(max_length=2000, verbose_name='分布和地形地貌', blank=True, default='', null=True)
    # Area_hm
    areaHectare = models.CharField(max_length=50, verbose_name='面积（公顷）', blank=True, default='', null=True)
    # Area_wanmu
    areaMu = models.CharField(max_length=50, verbose_name='面积（万亩）', blank=True, default='', null=True)
    # Parent
    material = models.TextField(max_length=2000, verbose_name='母质', blank=True, default='', null=True)
    # Profile_pattern
    configuration = models.TextField(max_length=2000, verbose_name='剖面构型', blank=True, default='', null=True)
    # Effective_depth
    effectSoilDepth = models.TextField(max_length=2000, verbose_name='有效土体深度', blank=True, default='', null=True)
    # Main_characters
    mainCharacters = models.TextField(max_length=2000, verbose_name='主要性状', blank=True, default='', null=True)
    # Soil_constraint_factor
    barrierFactor = models.TextField(max_length=2000, verbose_name='土壤障碍因子', blank=True, default='', null=True)
    # Production_performance
    productPerformance = models.TextField(max_length=2000, verbose_name='生产性能', blank=True, default='', null=True)
    # Landuse
    landUse = models.TextField(max_length=2000, verbose_name='土地利用', blank=True, default='', null=True)

    createdTime = models.DateTimeField(verbose_name='创建时间', default=timezone.now, blank=True, null=True)
    hits = models.PositiveIntegerField('浏览数', default=0)

    def __str__(self):
        return "<SoilSeedMess: %s>" % self.soilSeedName

    class Meta:
        verbose_name = '土种信息'
        verbose_name_plural = '土种信息'
        ordering = ['-createdTime']
