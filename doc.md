- 图标支持
> element-ui的图标和fontawesome的图标
>
> http://www.fontawesome.com.cn/faicons/
>
>https://element.eleme.cn/#/zh-CN/component/icon

 simpleui 设置

 首页配置
 
 SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
 
 首页标题
 
 SIMPLEUI_HOME_TITLE = '百度一下你就知道'

首页图标,支持element-ui的图标和fontawesome的图标

SIMPLEUI_HOME_ICON = 'el-icon-date'


设置simpleui 点击首页图标跳转的地址

SIMPLEUI_INDEX = 'https://www.88cto.com'


首页显示服务器、python、django、simpleui相关信息

SIMPLEUI_HOME_INFO = False

首页显示快速操作

SIMPLEUI_HOME_QUICK = False

首页显示最近动作

SIMPLEUI_HOME_ACTION = False

自定义SIMPLEUI的Logo


SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'


登录页粒子动画，默认开启，False关闭

SIMPLEUI_LOGIN_PARTICLES = True


让simpleui 不要收集相关信息

SIMPLEUI_ANALYSIS = True


自定义simpleui 菜单

```
SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    'system_keep': True,
    'menus': [{
        'name': 'Simpleui',
        'icon': 'fas fa-code',
        'url': 'https://gitee.com/tompeppa/simpleui'
    }, {
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }, {
        'app': 'myapp',
        'name': 'imapp',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '我的应用',
            'icon': 'fa fa-user',
            'url': '/index'
        }]
    }, {
        'name': '测试',
        'icon': 'fa fa-file',
        'models': [{
            'name': 'Baidu',
            'url': 'http://baidu.com',
            'icon': 'far fa-surprise'
        }, {
            'name': '内网穿透',
            'url': 'https://www.wezoz.com',
            'icon': 'fab fa-github'
        }]
    }, {
       'name': 'Iusgithub',
       'icon': 'fa fa-file',
       'models': [{
           'name': 'swim976',
           'url': 'http://www.lanrenmb.com/',
           'icon': 'far fa-surprise'
       }, {
           'name': 'imip',
           'url': 'http://restapi.amap.com/v3/weather/weatherInfo?key=f723f48119e78bf2dd098b87cfb7c3a6&city=500000',
           'icon': 'far fa-surprise'
       }]
    }]
}
```

 是否显示默认图标，默认=True

SIMPLEUI_DEFAULT_ICON = False


图标设置，图标参考：
```
SIMPLEUI_ICON = {
    '系统管理': 'fab fa-apple',
    '员工管理': 'fas fa-user-tie'
}
```

指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目

不填该项或者为False的时候，默认从第三方的cdn获取

SIMPLEUI_STATIC_OFFLINE = False