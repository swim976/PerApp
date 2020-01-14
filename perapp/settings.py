"""
Django settings for perapp project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!@x=o!wz^z2*tr4r^ogq_btx6nz_^hyb=q-xbu!cxnfzrvr@(h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inxapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'perapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'perapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# simpleui 设置

SIMPLEUI_HOME_ICON = 'el-icon-platform-eleme'


# 自定义simpleui 菜单
# SIMPLEUI_CONFIG = {
#     # 在自定义菜单的基础上保留系统模块
#     'system_keep': True,
#     'menus': [{
#         'name': 'Simpleui',
#         'icon': 'fas fa-code',
#         'url': 'https://gitee.com/tompeppa/simpleui'
#     }, {
#         'app': 'auth',
#         'name': '权限认证',
#         'icon': 'fas fa-user-shield',
#         'models': [{
#             'name': '用户',
#             'icon': 'fa fa-user',
#             'url': 'auth/user/'
#         }]
#     }, {
#         'app': 'myapp',
#         'name': 'imapp',
#         'icon': 'fas fa-user-shield',
#         'models': [{
#             'name': '我的应用',
#             'icon': 'fa fa-user',
#             'url': '/index'
#         }]
#     }, {
#         'name': '测试',
#         'icon': 'fa fa-file',
#         'models': [{
#             'name': 'Baidu',
#             'url': 'http://baidu.com',
#             'icon': 'far fa-surprise'
#         }, {
#             'name': '内网穿透',
#             'url': 'https://www.wezoz.com',
#             'icon': 'fab fa-github'
#         }]
#     }, {
#        'name': 'Iusgithub',
#        'icon': 'fa fa-file',
#        'models': [{
#            'name': 'swim976',
#            'url': 'http://www.lanrenmb.com/',
#            'icon': 'far fa-surprise'
#        }, {
#            'name': 'imip',
#            'url': 'http://restapi.amap.com/v3/weather/weatherInfo?key=f723f48119e78bf2dd098b87cfb7c3a6&city=500000',
#            'icon': 'far fa-surprise'
#        }]
#     }]
# }