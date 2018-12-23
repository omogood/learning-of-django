from django.contrib import admin
from .models import Post

# 以下にモデルを追加し Admin ページから見えるように追加する
admin.site.register(Post)
