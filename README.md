# Hoyolab Resin
用来提示和查询原神内树脂、委托、派遣情况的小工具<br>
近期的迭代可能会比较快
## 示例

企业微信

![](https://youngmoe.com/img/hoyolab_resin/5.png)

server酱

![](https://youngmoe.com/img/hoyolab_resin/6.png)

qq

![](https://youngmoe.com/img/hoyolab_resin/7.png)

## 食用方法
* 请确保米游社的实时便笺权限已经打开
* 获取cookie

0. [安装python3环境](https://www.python.org)，版本>=3.9 **如果要使用qqbot，需要安装3.10及以上版本**
    
1. `git clone https://github.com/yaomeng0722/genshin_task-resin-expedition_alert.git`
2. `pip3 install -r requirements.txt`
3  配置config.example.hson 配置方法如下 (\[可选\]修改config.example.json并另存为config.json)
1. `python3 index.py`

如果你的服务器已经有了较低版本的python环境，此处以centos为例：

`yum install epel-release`

`yum install python39`

`pip3.9 install -r requirements.txt`

`python3.9 index.py`

ubuntu、windows作类似修改或安装虚拟环境皆可(大概?)

## Config.json配置

**目前测试了使用server酱和企业微信进行推送的功能**

**tg等其他渠道在慢慢测了**


<s> 以及代部署(咳咳会死的)</s>
### 0. 一些基础信息
1. UID: 你游戏内的uid，填入config -> UID
1. COOKIE: 在[原神米游社社区](https://bbs.mihoyo.com/ys)获取到的cookie 
    <br> 获取方式：</br>
    <br> `javascript:(function(){let domain=document.domain;let cookie=document.cookie;prompt('Cookies: '+domain, cookie)})();`</br>
    <br>  复制上面的代码存储为书签，打开社区之后，点击该书签，复制弹出的信息并填入config -> COOKIE即可</br>

### 1. server酱
<details>
1. 前往[server酱](https://sct.ftqq.com/)官网注册并绑定微信<br>
2. 将获取到的send key填入config -> SCKEY中即可<br>

server酱免费版每天有5次的调用次数上限
</details>

### 2. 企业微信
<details>
1. [注册企业微信](https://work.weixin.qq.com/)(个人即可注册，不需要进行企业身份验证)


2. 在"应用管理"中创建新应用

![](https://youngmoe.com/img/hoyolab_resin/1.png "(个人即可注册，不需要进行企业身份验证)")

3. 在应用中查看agentid与secret分别填入config -> WECOM_AGENT_ID 与 config -> WECOM_SECRET (注：secret需要在手机端的企业微信进行查看)

![](https://youngmoe.com/img/hoyolab_resin/3.png "secret需要在手机端的企业微信进行查看")

4. 在"我的企业"中获取企业id填入config -> WECOM_CORP_ID

![](https://youngmoe.com/img/hoyolab_resin/2.png)

5. 在"通讯录" -> "成员管理" 中获取要收取信息的人员账号填入config -> WECOM_USER_ID

![](https://youngmoe.com/img/hoyolab_resin/4.png)


</details>

### 3.qqbot
<summary>暂时只支持主动查询，只能在windows环境部署，输入/resin xxxx即可获取信息<br>目前支持的有:/resin 树脂/委托/boss/派遣/总览共5项</summary>
**由于使用了match case，所以需要python版本>=3.10**
<details>

qqbot现在的部署有点麻烦= =使用了NoneBot2作为机器人框架,只支持windows平台<br>

目前只有私聊功能，群聊使用可能需要代部署(即由他人来保存你的cookie并发送消息，会有很多不必要的风险，暂时不考虑做)
<br>
[None2bot官方文档参考](https://v2.nonebot.dev/guide/)<br>
1. 安装虚拟环境 此处以virtualenv 为例<br> `pip install virtualenv`<br>
2. cd到你想要安装的文件夹 输入 `virtualenv your-mkdir-name` 创建虚拟环境<br>
3. cd到Scripts目录，使用普通cmd(非powershell)输入`activate`<br>
4. 如果之前有NoneBot v1，需要卸载 `pip uninstall nonebot`<br>
5. `pip install nb-cli`安装脚手架<br>
6. `cd ..` <br>`nb create` <br>创建目录，根据提示输入项目名称、插件存放路径、安装的插件 <br><br>
在选择安装插件时，注意用空格勾选cqhttp之后再回车<br>
<br>项目目录内包含`bot.py`<br>
在命令行使用如下命令即可运行这个NoneBot实例<br>
`nb run`<br>
或者<br>
`python bot.py`
7. [根据服务器版本安装机器人客户端并登录](https://github.com/Mrs4s/go-cqhttp/releases)      <br>
[文档参考](https://v2.nonebot.dev/guide/cqhttp-guide.html)      <br>
        运行.exe文件或者`./go-cqhttp`启动<br>
    
    
        生成默认配置文件并修改默认配置<br>
        
        修改`config.yml`文件<br>
    
        account:<br>
           uin: 机器人QQ号<br>
            password: "机器人密码"<br>
        
        message:<br>
            post-format: array<br>
        
        servers:<br>
          - ws-reverse:<br>
              universal: ws://127.0.0.1:8080/cqhttp/ws<br>

8. 在含有`bot.py`的项目目录中新建目录`plugins/resin_alert`并将源码中的alert文件夹复制进去,配置config\_data/config\_example.json中的UID与COOKIE<br>


9. 将alert/for\_qq文件夹中的\_\_init\_\_.py与config.py移至resin_alert文件夹<br>


10. 修改`bot.py`，在main前添加`nonebot.load_plugins("plugins")`<br>


11. 通过qq发送/resin 总览查看是否有消息返回，如果没有，尝试/echo hello查看是否有"hello"返回,都没有请提交issue

</details>

## config参数

| key                      |                      comment                       |       example        |
| ------------------------ | :------------------------------------------------: | :------------------: |
| UID                      |                      游戏uid                       |      100088888       |
| COOKIE                   |                    米游社cookie                    |         ****         |
| SCKEY                    |                 server酱的sendkey                  |         ****         |
| SCTKEY                   |                   server酱turbo                    |          **          |
| WW_ID                    |                     企业微信id                     |          **          |
| WW_APP_SECRET            |                   企业微信secret                   |          **          |
| WW_APP_USERID            |              企业微信接收消息的用户id              |          **          |
| WW_APP_AGENTID           |                     企业应用Id                     |       10000001       |
| WW_BOT_KEY               |                 企业微信机器人key                  |        未测试        |
| DD_BOT_TOKEN             |                       未测试                       |        未测试        |
| DD_BOT_SECRET            |                       未测试                       |        未测试        |
| DISCORD_WEBHOOK          |                       未测试                       |        未测试        |
| IGOT_KEY                 |                       未测试                       |        未测试        |
| PUSH_PLUS_TOKEN          |                       未测试                       |        未测试        |
| PUSH_PLUS_USER           |                       未测试                       |        未测试        |
| TG_BOT_API               |                    telegram接口                    |   api.telegram.org   |
| TG_BOT_TOKEN             |                       未测试                       |        未测试        |
| TG_USER_ID               |                       未测试                       |        未测试        |
| RESIN_ALERT_NUM          |               树脂达到多少时进行提示               |         150          |
| RECEIVE_RESIN_DATA       |                是否接收树脂溢出提示                |          ON          |
| RECEIVE_BOSS_COUNT       |          是否接收本周boss树脂减半剩余次数          |          ON          |
| RECEIVE_TASK_NUM         |                是否接收每日委托提示                |          ON          |
| REVEIVE_EXPEDITION_NUM   |                是否接收探索派遣提示                |          ON          |
| INCOMPLETE_ALERT         |      在这个时间，如果每日委托未完成，进行提示      | "213030"(即21:30:30) |
| SELLP_TIME               | 程序每轮执行的休眠时间，为避免被封ip，建议稍微长点 |          60          |
| ALERT_SUCCESS_SLEEP_TIME |    提示成功后的休眠时间，为避免扰民可以设置长点    |         1800         |
| 乱                       |                         填                         |          会          |
| 报                       |                         错                         |         哦~          |


## 自定义提示信息：
#### 根据需要修改getinfo中dataanalystic.py与notifiers中的几个文件即可(近几天有空会优化一下，现在有点丑)


## 致谢
[Lycreal](https://github.com/Lycreal) 好看的米游社api调用

[y1ndan](https://www.yindan.me/tutorial/genshin-impact-helper.html) notifiers 多渠道发送消息

[lulu666lulu](https://github.com/lulu666lulu) ds的算法

[Mrs4s](https://github.com/Mrs4s) cqhttp客户端

[nonebot](https://github.com/nonebot/nonebot2) nonebot机器人框架