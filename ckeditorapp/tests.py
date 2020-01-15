from django.test import TestCase

# Create your tests here.
"""
https://haofly.net/django-admin/index.html

django-ckeditor扩展，使用简单，前端也漂亮

安装pip install django-ckeditor，如果要在富文本里添加图片还需要pip install pillow

注册应用，INSTALLED_APPS里添加ckeditor，图片还需要添加ckeditor_uploader
 
如果要处理图片，还需要在settings.py里面添加如下设置:

# 前面两个可能已经设置了，是存放用户上传文件的地方
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
 
CKEDITOR_UPLOAD_PATH = 'upload/'

CKEDITOR_CONFIGS = {	# 添加个性化的配置
    'default': {
        'image_previewText':' ',	# 替换图片显示区域那一串搞不懂的字符串
        'tabSpaces': 4,
    }
}
"""