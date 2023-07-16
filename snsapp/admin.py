from django.contrib import admin
from .models import SnsModel
# Register your models here.

#管理画面で読み込ませてあげる必要あり
admin.site.register(SnsModel)