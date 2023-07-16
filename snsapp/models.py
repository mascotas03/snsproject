from django.db import models

# Create your models here.

class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    #写真を細かくフォルダ分けしたい場合、uplpad_toに指定する。
    #今回は一つのプロジェクトだからsettingsの方でBASE指定したファイルに入れるため、ブランクでいい。
    images = models.ImageField(upload_to="")
    good = models.IntegerField()
    read = models.IntegerField()
    readwho = models.CharField(max_length=200)
    
      
    