# Hoyolab Resin
一个用来提示和查询原神内树脂、委托、派遣情况的小工具
## 示例
企业应用

![](https://youngmoe.com/img/hoyolab_resin/5.png)

server酱

![](https://youngmoe.com/img/hoyolab_resin/6.png)

## 食用方法
* 请确保米游社的实时便笺权限已经打开
* 获取cookie

0. [安装python3环境](https://www.python.org)，版本>=3.9
    
1. `git clone https://github.com/yaomeng0722/genshin_task-resin-expedition_alert.git`
1. `pip3 install -r requirements.txt`
1. 配置config.example.hson  (\[可选\]修改config.example.json并另存为config.json)
1. `python3 resin.py`

如果你的服务器已经有了较低版本的python环境，此处以centos为例：

`yum install epel-release`

`yum install python39`

`pip3.9 install -r requirements.txt`

`python3.9 resin.py`

ubuntu、windows作类似修改或安装虚拟环境皆可

## Config.json配置

**目前实现了使用server酱和企业微信进行推送的功能**  (其他的在做了在做了)
### 0. 一些基础信息
1. UID: 你游戏内的uid，填入config -> UID
1. COOKIE: 在[原神米游社社区](https://bbs.mihoyo.com/ys)获取到的cookie 
    <br> 获取方式：</br>
    <br> `javascript:(function(){let domain=document.domain;let cookie=document.cookie;prompt('Cookies: '+domain, cookie)})();`</br>
    <br>  复制上面的代码存储为书签，打开社区之后，点击该书签，复制弹出的信息并填入config -> COOKIE即可</br>

### 1. server酱
1. 前往[server酱](https://sct.ftqq.com/)官网注册并绑定微信
1. 将获取到的send key填入config -> SCKEY中即可
1. 修改 SERVER_CHAN_STATUS 为ON

### 2. 企业微信
1. [注册企业微信](https://work.weixin.qq.com/)(个人即可注册，不需要进行企业身份验证)


2. 在"应用管理"中创建新应用

![](https://youngmoe.com/img/hoyolab_resin/1.png "(个人即可注册，不需要进行企业身份验证)")

3. 在应用中查看agentid与secret分别填入config -> WECOM_AGENT_ID 与 config -> WECOM_SECRET (注：secret需要在手机端的企业微信进行查看)

![](https://youngmoe.com/img/hoyolab_resin/3.png "secret需要在手机端的企业微信进行查看")

4. 在"我的企业"中获取企业id填入config -> WECOM_CORP_ID

![](https://youngmoe.com/img/hoyolab_resin/2.png)

5. 在"通讯录" -> "成员管理" 中获取要收取信息的人员账号填入config -> WECOM_USER_ID

![](https://youngmoe.com/img/hoyolab_resin/4.png)

6. 修改 WECOM_STATUS 为ON

## config参数

key  | comment |example
------------- |:-------------:|:--:
UID|游戏uid|100088888
COOKIE|米游社cookie|****
SENDKEY|server酱的sendkey|****
WECOM_CORP_ID|企业微信的企业id|****
WECOM_SECRET|企业应用的secret|****
WECOM_USER_ID|企业微信收信人id|****
WECOM_AGENT_ID |企业应用的agentid|****
WECOM_STATUS|企业微信收信状态 "ON"为打开，"OFF"为关闭 下同|ON
SERVER_CHAN_STATUS|server酱收信状态 |ON
RESIN_ALERT_NUM|树脂达到多少时进行提示|150
RECEIVE_RESIN_DATA|是否接收树脂溢出提示|ON
RECEIVE_BOSS_COUNT|是否接收本周boss树脂减半剩余次数|ON
RECEIVE_TASK_NUM|是否接收每日委托提示|ON
REVEIVE_EXPEDITION_NUM|是否接收探索派遣提示|ON
INCOMPLETE_ALERT|在这个时间，如果每日委托未完成，进行提示|"213030"(即21:30:30)
SELLP_TIME|程序每轮执行的休眠时间，为避免被封ip，建议稍微长点|60
乱|填|会
报|错|哦~


## 自定义提示信息：
#### 根据需要修改dataanalystic.py等文件即可(过两天有空会优化一下，现在有点丑)

#### server酱与企业微信均支持markdown语法，<br>

server酱: desp直接使用markdown语法就可以<br>
企业微信: 只需给wx.send_message添加参数"markdown"(markdown暂时有bug)<br>




## credits
[Lycreal](https://github.com/Lycreal)
