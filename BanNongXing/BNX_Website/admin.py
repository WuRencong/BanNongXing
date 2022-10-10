from django.contrib import admin
from .models import New, NewType, Liaison_cooperation, information, SeedMess, seedImg, SoilMess, SubClassMess, SoilSeedMess

# Register your models here.
@admin.register(NewType)
class NewTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'new_type', 'author', 'created_time')


@admin.register(Liaison_cooperation)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'User_name', 'Company_name', 'Telephone', 'Types_section')


@admin.register(information)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'Whether_helps', 'Detailed', 'Humanize', 'Provide')


class seedImgInline(admin.StackedInline):
    model = seedImg
    extra = 1                                   #默认显示条目的数量


class SeedAdmin(admin.ModelAdmin):
    inlines = [seedImgInline, ]


admin.site.register(SeedMess, SeedAdmin)


@admin.register(SoilMess)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'soilName', 'soilEngName', 'soilClassName', 'soilClassEngName', 'soilDescription', 'createdTime', 'hits')


@admin.register(SubClassMess)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'subgroupId', 'subClassName', 'subClassEngName', 'subClassNatName', 'createdTime', 'hits')


@admin.register(SoilSeedMess)
class LiaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'soilSeedId', 'soilSeedName', 'soilSeedDescript', 'distributionLandform', 'areaHectare', 'areaMu', 'material',
                    'configuration', 'effectSoilDepth', 'mainCharacters', 'barrierFactor', 'productPerformance', 'landUse',
                    'createdTime', 'hits')

