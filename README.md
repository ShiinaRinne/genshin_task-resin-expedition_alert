# 原神提醒小助手 | Genshin Alert Helper

用来检查并推送原神内树脂、委托、周本、探索派遣和洞天宝钱情况的小工具，只支持国服。

## 示例

**企业微信**

![](https://i.loli.net/2021/10/19/uoGFiY7b1fecZhR.png)

**Server 酱**

![](https://i.loli.net/2021/10/19/mVjvS3YTLliXg17.png)

**Telegram Bot**

![](https://i.loli.net/2021/10/19/tTvZgExA1db9uPN.png)

**PUSH PLUS**

![](https://i.loli.net/2021/10/19/OUzfnrJRuxAFwc9.png)

**钉钉群机器人**

![](https://i.loli.net/2021/10/19/P5RLCksmBUfOyJo.png)

**CoolPush**

![](https://i.loli.net/2021/10/21/QpK1Mi3VdwsDml5.png)

**QQ**

![](https://youngmoe.com/img/hoyolab_resin/7.png)

## 食用方法

- 请确保米游社的实时便笺权限已经打开
- 配置推送方式，参见[推送方式配置](#%E6%8E%A8%E9%80%81%E6%96%B9%E5%BC%8F%E9%85%8D%E7%BD%AE)部分
- 填写配置文件或配置环境变量，详情参见[配置文件参数说明](#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)部分

### 1.Docker 运行

1. 点击[链接](https://raw.githubusercontent.com/yaomeng0722/genshin_task-resin-expedition_alert/master/alert/config_data/config.example.json)或本项目路径`alert/config_data/config.example.json`提取示例配置文件并填写，重命名为`config.json`。

2. 运行，`/PATH/config.json`是你本地配置文件的路径，需要根据实际情况填写。

   ```sh
   docker run -d \
   -v /PATH/config.json:/app/alert/config_data/config.json \
   --restart=always \
   --name=genshin-alert \
   xm798/genshin-alert:latest
   ```

### 2.本地运行

1. 安装 [python3](https://www.python.org) 环境，版本>=3.9。

   如果你的服务器已经有了较低版本的 python 环境，此处以 Centos 为例：

   ```shell
   yum install epel-release
   yum install python39
   pip3.9 install -r requirements.txt
   python3.9 index.py
   ```

   其它系统请自行安装 >=3.9 的版本 python。

2. 下载项目并安装依赖
   ```shell
   git clone https://github.com/yaomeng0722/genshin_task-resin-expedition_alert.git
   cd genshin_task-resin-expedition_alert
   pip3 install -r requirements.txt
   ```
3. 修改配置

   复制 `./alert/config_data/config.example.json` 并另存为 `config.json`，填入配置信息。

   ```
   cp ./alert/config_data/config.example.json ./alert/config_data/config.json
   vi ./alert/config_data/config.json
   ```

4. 运行项目
   ```
   python3 index.py
   ```

## 配置文件参数说明

建议使用 [VS Code](https://code.visualstudio.com/) 或其他支持 json-schema 的编辑器编辑配置文件，可自动显示填写提示和进行配置检查。

### 一些基础信息

1. RUN_ENV：指定运行环境，国内云服务商运行使用`cloud`，否则使用`local`。该选项旨在为在国内云服务器运行的用户提供兼容性选项,`cloud`为旧版 API，曾经无法使用，现在又恢复了。但由于米游社已全面更换为新的 API，因此默认使用`local`环境即新 API 运行。
   详情参考：[米游社可能已经禁止国内特定 VPS 服务商的 IP 或 ASN](https://github.com/Arondight/Adachi-BOT/issues/522)

2. COOKIE: 
   1. 打开[米游社社区](https://bbs.mihoyo.com/ys)并登录； 
   2. 按 F12 打开开发者工具； 
   3. 将开发者工具切换至控制台(Console)页签； 
   4. 复制下方的代码，并将其粘贴在控制台中，按下回车，将结果粘贴到配置文件中。

   ```javascript
   javascript:(()=>{_=(n)=>{for(i in(r=document.cookie.split(';'))){var a=r[i].split('=');if(a[0].trim()==n)return a[1]}};c=_('account_id')||alert('无效的Cookie,请重新登录!');c&&confirm('将Cookie复制到剪贴板?')&&copy(document.cookie)})();
   ```

---

| Key                       |                             Comment                             |                      Remark                      |
| ------------------------- | :-------------------------------------------------------------: | :----------------------------------------------: |
| RUN_ENV                   |        运行环境，国内云服务商为`cloud`，其他使用`local`         |                  local / cloud                   |
| UID                       |                            游戏 uid                             |                                                  |
| COOKIE                    |                          米游社 cookie                          |                                                  |
| NAME                      |                            账号别名                             |                   便于区分账号                   |
| RESIN_ALERT_NUM           |                     树脂达到多少时进行提示                      |                       150                        |
| RECEIVE_RESIN_DATA        |                      是否接收树脂溢出提示                       |                      ON/OFF                      |
| RECEIVE_BOSS_COUNT        |               是否接收本周 boss 树脂减半剩余次数                |                      ON/OFF                      |
| RECEIVE_TASK_NUM          |                      是否接收每日委托信息                       |                      ON/OFF                      |
| REVEIVE_EXPEDITION_NUM    |                      是否接收探索派遣信息                       |                      ON/OFF                      |
| RECEIVE_HOMECOIN_ALERT    |                    是否接收洞天宝钱溢出提醒                     |                      ON/OFF                      |
| INCOMPLETE_ALERT          |            在这个时间，如果每日委托未完成，进行提示             |              "213030"(即 21:30:30)               |
| EXPEDITION_COMPLETE_ALERT |                    当探索派遣完成时发送提醒                     |                      ON/OFF                      |
| SELLP_TIME                | 执行每轮检查的等待时间，为避免被封 ip，建议稍微长点（单位：秒） |                        900                       |
| ALERT_SUCCESS_SLEEP_TIME  |    推送成功后的等待时间，为避免扰民可以设置长点（单位：秒）     |                       1800                       |
| SLEEP_START_TIME          |     休眠开始时间，避免深夜扰民，与`SLEEP_END_TIME`配合使用      |              "230000"(即 23:00:00)               |
| SLEEP_END_TIME            |           休眠结束时间，与`SLEEP_START_TIME`配合使用            |              "080000"(即 08:00:00)               |
| WW_ID                     |                           企业微信 id                           |                                                  |
| WW_APP_SECRET             |                         企业微信 secret                         |                                                  |
| WW_APP_USERID             |                    企业微信接收消息的用户 id                    |                                                  |
| WW_APP_AGENTID            |                           企业应用 Id                           |                                                  |
| WW_BOT_KEY                |                       企业微信机器人 key                        |                                                  |
| BARK_URL                  |                         Bark 推送服务器                         |          默认使用`https://api.day.app/`          |
| BARK_KEY                  |                          Bark App KEY                           |                                                  |
| BARK_GROUP                |                        自定义 Bark 分组                         |                不填则使用默认分组                |
| BARK_ICON                 |                      自定义 Bark 通知图标                       |   仅支持 Web URL 图片，不填则不使用自定义图标    |
| BARK_ARCHIVE              |                        自定义 Bark 保存                         |   1 为保存，其他值为不保存，不填则使用默认规则   |
| TG_BOT_API                |                        Telegram API 接口                        |                 api.telegram.org                 |
| TG_BOT_TOKEN              |                       Telegram Bot token                        |                                                  |
| TG_USER_ID                |                      接收消息账号的 userid                      | 可用[@userinfobot](https://t.me/userinfobot)获取 |
| PUSHDEER_KEY              |                       Pushdeer 的 pushkey                       |                                                  |
| CQHTTP_IP                 |                       cq-http 的 ip 地址                        |                                                  |
| CQHTTP_PORT               |                     cq-http 的 HTTP 端口号                      |                    默认 5700                     |
| CQHTTP_MESSAGE_TYPE       |     cq-http 的消息发送方式，`private`为私聊，`group`为群聊      |                  private/group                   |
| CQHTTP_SEND_ID            |                    接收消息的 qq 号码/群号码                    |                                                  |
| CQHTTP_TOKEN              |                     cqhttp 的 CQHTTP_TOKEN                      |                 未设置不需要填写                 |
| DD_BOT_TOKEN              |                     钉钉机器人 access_token                     |                                                  |
| DD_BOT_SECRET             |                       钉钉机器人加签密钥                        |                                                  |
| SCTKEY                    |                            Server 酱                            |                   SCT********                    |
| PUSH_PLUS_TOKEN           |                       PushPlus 推送 token                       |                                                  |
| PUSH_PLUS_USER            |                   PushPlus 一对多推送群组 id                    |                不填则为一对一推送                |
| COOL_PUSH_SKEY            |                            酷推 SKEY                            |                                                  |
| COOL_PUSH_MODE            |                          酷推推送模式                           |             send/psend/group/pgroup              |
| COOL_PUSH_SENDID          |                    酷推指定接收方 QQ 号/群号                    |                                                  |
| QMSG_KEY                  |                         Qmsg 酱推送 KEY                         |                                                  |
| DISCORD_WEBHOOK           |                             未测试                              |                      未测试                      |
| IGOT_KEY                  |                             未测试                              |                      未测试                      |

## 推送方式配置

**目前支持的推送渠道详情如下表**，建议：

- **微信推送**：使用企业微信；
- **系统通知推送**：iOS 用户使用 Bark 或 Pushdeer，MIUI 用户使用 Pushdeer；
- **全平台推送**：使用 Telegram 或企业微信；
- **QQ 推送**：自行部署 go-cqhttp 并使用。

|            推送渠道             | 支持情况  |             推送通道             |          备注           |
| :-----------------------------: | :-------: | :------------------------------: | :---------------------: |
|     [企业微信](#1-企业微信)     |  ✅ 支持  |          微信（全平台）          |         推荐 ⭐         |
|         [Bark](#2-bark)         |  ✅ 支持  |         APP（仅限 iOS）          |         推荐 ⭐         |
| [Telegram Bot](#3-telegram-bot) |  ✅ 支持  |        Telegram（全平台）        |   推荐 ⭐，需科学上网   |
|    [Pushdeer](#4-pusherdeer)    |  ✅ 支持  | 轻 APP(iOS)/APP(安卓)/APP(MacOS) | 推荐 iOS 和小米设备使用 |
|    [go-cqhttp](#5-go-cqhttp)    |  ✅ 支持  |                QQ                |  需自行部署 go-cqhttp   |
| [钉钉群机器人](#6-钉钉群机器人) |  ✅ 支持  |              钉钉群              |                         |
|    [Server 酱](#7-server-酱)    |  ✅ 支持  |        多渠道推送(微信等)        |    免费版每天限 5 条    |
|    [pushplus](#8-push-plus)     |  ✅ 支持  |     多渠道推送(微信/邮件等)      |                         |
|  [Cool Push](#9-coolpush-酷推)  |  ✅ 支持  |                QQ                |                         |
|     [Qmsg 酱](#10-qmsg-酱)      |  ✅ 支持  |                QQ                |                         |
|         Discord_Webhook         | 🛠️ 未测试 |                                  |                         |
|              IGOT               | 🛠️ 未测试 |                                  |                         |

### 1. 企业微信

<details>

> 本部分教程鸣谢 Server 酱。

1. 注册企业：用电脑打开[企业微信官网](https://work.weixin.qq.com/)，注册一个企业。

2. 创建应用：注册成功后，点「管理企业」进入管理界面，选择「应用管理」 → 「自建」 → 「创建应用」。

   ![img](https://s2.loli.net/2022/02/06/j5EZvRV6YtDKr7B.png)

3. 创建完成后进入应用详情页，可以得到应用 ID( `agentid` )，应用 Secret( `secret` )，复制并填到配置文件对应位置（获取应用 Secret 时，可能会将其推送到企业微信客户端，需要在企业微信客户端查看）。

![img](https://s2.loli.net/2022/02/06/1N3rnFVHBqQk2Wh.png)

4. 获取企业 ID：进入「[我的企业](https://work.weixin.qq.com/wework_admin/frame#profile)」页面，拉到最下边，可以看到企业 ID，复制并填到配置文件中。

5. 获取推送用户：在"通讯录" -> "成员管理" 中获取要收取信息的人员账号填入配置文件`WW_APP_USERID`，全员推送填`@all`。如果该应用只有一个人使用，填`@all`即可。

   ![image-20220206142035455](https://s2.loli.net/2022/02/06/XylJe4SAMFEjoYb.png)

6. 推送消息到微信：进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到下边扫描二维码，关注以后即可收到推送的消息。

   ![img](https://s2.loli.net/2022/02/06/wOJ47LAVcX6Par8.png)

注：如果出现`接口请求正常，企业微信接受消息正常，个人微信无法收到消息`的情况：

   1. 进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到最下方，勾选 “允许成员在微信插件中接收和回复聊天消息” ![img](https://s2.loli.net/2022/02/06/sF8MS3ZBUCueN7I.jpg)
   2. 在企业微信客户端 「我」 → 「设置」 → 「新消息通知」中关闭 “仅在企业微信中接受消息” 限制条件 ![img](https://s2.loli.net/2022/02/06/OdyJslVKtekTIAX.jpg)

</details>

### 2. Bark

<details>

1. 从 AppStore 下载并打开 [Bark](https://github.com/Finb/Bark) App，将 App 内提供的 KEY 填入 `BARK_KEY` 即可。
2. 支持部分可选配置，如自定义消息分组 `BARK_GROUP`，自定义通知图标 `BARK_ICON`，自定义消息保存 `BARK_ARCHIVE`。
3. 支持自建服务器`BARK_URL`。

</details>

### 3. Telegram Bot

<details>

1. 创建机器人：打开 [@BotFather](https://t.me/botfather)，输入 `/newbot` 生成新一个的 bot。根据提示，依次输入：Bot 名字、Bot 账号（需要以 bot 结尾），复制获取到的 Token，填入配置文件`TG_BOT_TOKEN`。
   ![image-20220206143711051](https://s2.loli.net/2022/02/06/MBX7EmTJZDtzq93.png)
2. 点击消息框中 `t.me/你的botid `这个链接，跳转到你的 bot，点击`START`以关联你的 bot。
3. 打开 [@userinfobot](https://t.me/userinfobot)，发送`/start`，获取你的 ID，填入配置文件`TG_USER_ID`。
4. 使用 Telegram bot 推送需要配置代理，或搭建反代服务器后填入配置文件`TG_BOT_API`。此处提供一个我基于 CF Workers 反代的 API `tgbotapi.xm.mk` 供使用。

</details>

### 4. Pusherdeer

<details>

[PushDeer](https://github.com/easychen/pushdeer)是一个可以自行架设的无APP推送服务，iOS 端基于轻APP，无需安装APP；Android未来将基于快应用（正在开发），目前使用 APP（已接入MI PUSH，因此小米用户可在不开启 APP 的情况下获取通知）。

1. 苹果手机（iOS 14+）用系统相机扫描下方码即可拉起轻应用。亦可在苹果商店搜索「PushDeer」安装（不要安装 PushDeer 自架版）。Android 快应用尚在开发，可下载并安装 Android 测试版 APP([GitHub](https://github.com/easychen/pushdeer/releases/tag/android1.0alpha)|[Gitee](https://gitee.com/easychen/pushdeer/releases/android1.0alpha))。
   ![img](https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png)
2. 通过 apple 账号（或微信账号·仅 Android 版支持）登录。
3. 切换到「设备」标签页，点击右上角的加号，注册当前设备。
4. 切换到「Key」标签页，点击右上角的加号，创建一个 Key，将 Key 填入配置文件`PUSHDEER_KEY`中。

</details>

### 5. GO-CQHTTP

<details>

1. 部署 [GO-CQHTTP](https://github.com/Mrs4s/go-cqhttp)，参见文档[快速开始](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)，也可使用其他兼容 [OneBot-v11](https://github.com/botuniverse/onebot-11) 规范的框架或 SDK。
2. 将 CQHTTP 的服务器 IP/域名填入 `CQHTTP_IP`，端口号填入 `CQHTTP_PORT`。
3. 配置发送模式 `CQHTTP_MESSAGE_TYPE`，`private` 为私聊发送，`group` 为群聊发送。
4. 配置消息接收方的 QQ 号/群号，填入 `CQHTTP_SEND_ID`，与发送模式匹配。
5. 若配置了`Access Token`，需要填写 `CQHTTP_TOKEN`。

</details>

### 6. 钉钉群机器人

<details>

1. 创建钉钉群，并添加自定义机器人，参见 [钉钉开放平台·自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027)。
2. 将生成的 Webhook 地址中的 `access_token`填入 `DD_BOT_TOKEN`。
3. 将创建过程中`加签`的密钥填入`DD_BOT_SECRET`。
</details>

### 7. Server 酱

<details>

1. 前往[Server 酱](https://sct.ftqq.com/) 官网注册并绑定微信。
2. 将获取到的`send key`填入`config.json -> SCKEY`中即可。

注：Server 酱免费版每天有 5 次的调用次数上限。

</details>

### 8. Push Plus

<details>

1. 登录 [pushplus 网站](http://www.pushplus.plus/) ，复制 token 填入 `PUSH_PLUS_TOKEN`。
2. 若要一对多推送，需要创建群组并将群组编号填入 `PUSH_PLUS_USER`，一对一推送无需填写。

</details>

### 9. CoolPush 酷推

<details>

注：现在酷推公共服务不可用，可能需要私有化部署。

1. 登录 [CoolPush](https://cp.xuthus.cc/)，绑定 QQ 号/QQ 群及私有化部署地址，获取`调用代码Skey`。
2. 将 Skey 填入 `COOL_PUSH_SKEY` ，`COOL_PUSH_MODE` 支持 QQ 私聊推送/QQ 群消息推送/QQ 私有化私聊推送/QQ 私有化群聊推送，不支持一对多推送。
3. 如果需要动态的指定推送消息给特定的 QQ 号或者群，将 QQ 号/群号填入 `COOL_PUSH_SENDID` 即可。

</details>

### 10. Qmsg 酱

<details>

登录 [Qmsg 酱](https://qmsg.zendee.cn/)，获取 KEY 填入 `QMSG_KEY` 即可。

注：Qmsg 酱容易被判定违规=\_=，且无法进行群聊推送（审核不通过）。

</details>

### 11. QQBot

该部分不再提供支持，不推荐使用。如需使用，请确保具备一定的 Python 开发能力。

<details>

暂时只支持主动查询，只能在 windows 环境部署，输入/resin xxxx 即可获取信息。目前支持的有:/resin 树脂/委托/boss/派遣/总览共 5 项。

qqbot 现在的部署有点麻烦= =使用了 NoneBot2 作为机器人框架,只支持 windows 平台<br>

目前只有私聊功能，群聊使用可能需要代部署(即由他人来保存你的 cookie 并发送消息，会有很多不必要的风险，暂时不考虑做)
<br>
[None2bot 官方文档参考](https://v2.nonebot.dev/guide/)<br>

1.  安装虚拟环境 此处以 virtualenv 为例<br> `pip install virtualenv`<br>
2.  cd 到你想要安装的文件夹 输入 `virtualenv your-mkdir-name` 创建虚拟环境<br>
3.  cd 到 Scripts 目录，使用普通 cmd(非 powershell)输入`activate`<br>
4.  如果之前有 NoneBot v1，需要卸载 `pip uninstall nonebot`<br>
5.  `pip install nb-cli`安装脚手架<br>
6.  `cd ..` <br>`nb create` <br>创建目录，根据提示输入项目名称、插件存放路径、安装的插件 <br><br>
    在选择安装插件时，注意用空格勾选 cqhttp 之后再回车<br>
    <br>项目目录内包含`bot.py`<br>
    在命令行使用如下命令即可运行这个 NoneBot 实例<br>
    `nb run`<br>
    或者<br>
    `python bot.py`
7.  [根据服务器版本安装机器人客户端并登录](https://github.com/Mrs4s/go-cqhttp/releases) <br>
    [文档参考](https://v2.nonebot.dev/guide/cqhttp-guide.html) <br>
    运行.exe 文件或者`./go-cqhttp`启动<br>

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

8.  在含有`bot.py`的项目目录中新建目录`plugins/resin_alert`并将源码中的 alert 文件夹复制进去,配置 config_data/config_example.json 中的 UID 与 COOKIE<br>

9.  将 alert/for_qq 文件夹中的\_\_init\_\_.py 与 config.py 移至 resin_alert 文件夹<br>

10. 修改`bot.py`，在 main 前添加`nonebot.load_plugins("plugins")`<br>

11. 通过 qq 发送/resin 总览查看是否有消息返回，如果没有，尝试/echo hello 查看是否有"hello"返回,都没有请提交 issue

</details>

## 更新日志

### v1.3.3（2022-02-06）

New Features:

- 新增 Pushdeer 推送通道

### v1.3.2（2022-01-12）

Bug Fixes

### v1.3.1（2022-01-10）

New Features:

- 支持自定义 BARK 推送服务器

Bug Fixes:

- 修复 BARK 推送状态检测错误的问题

### v1.3.0（2022-01-10）

新年新气象~

New Features:

- 加入洞天宝钱信息，支持设置洞天宝钱溢出提醒，配置文件新增`RECEIVE_HOMECOIN_ALERT`字段
- 增加睡前检查，若树脂在休眠期间溢出将在睡眠前发送提醒
- 加入 API 切换选项，支持云服务器运行时指定使用旧版 API
- 优化消息排版

Bug Fixes:

- 修复树脂溢出提示无效的问题
- 更新探索派遣新角色信息
- 修复诺艾尔角色信息错误
- 优化休眠逻辑

### v1.2.5（2021-12-24）

- 同步米游社 API 变动，更换新的 API，请务必更新。

注：若 API 返回“很抱歉，由于您访问的 URL 有可能对网站造成安全威胁，您的访问被阻断”的错误提示，请不要使用腾讯云或阿里云等云服务商的 VPS 运行本项目，尝试使用本地设备部署。

### v1.2.4（2021-11-24）

- Bug Fixes：修复 cookie 出错时的异常退出问题

### v1.2.3（2021-11-23）

- CQHTTP 推送 IP 字段支持协议头，以支持 HTTPS

### v1.2.2（2021-11-10）

优化每日委托提醒

- 优化提醒时间判断逻辑
- 增加奖励领取情况判断，去他人世界做委托领取奖励后不再会被误认为未完成委托。

### v1.2.1（2021-11-01）

修复 CQ-HTTP 推送，请使用 CQ-HTTP 的用户注意**配置文件字段变动**。

- 修复鉴权错误，解决需要鉴权的 CQ-HTTP 不能使用的问题
- 增加群推送模式支持
- 增加自定义端口支持

### v1.2.0 (2021-11-01)

- 支持夜间休眠，再也不会深夜不停扰民了
- 日志增加每轮检查树脂值显示
- 修复 cqhttp 推送错误提示
- 配置文件部分字段改为可选配置

### v1.1.2（2021-10-29）

- 增加 cqhttp 推送
- 更新文档

### v1.1.1 (2021-10-28)

- 增加探索派遣完成提醒
- 优化提醒标题

### v1.1.0 (2021-10-28)

- 修复休眠时间不正确的问题
- 优化提醒逻辑
- 增加账号信息显示

## 致谢

- [Lycreal](https://github.com/Lycreal) 好看的米游社 api 调用

- [y1ndan](https://www.yindan.me/tutorial/genshin-impact-helper.html) notifiers 多渠道发送消息

- [lulu666lulu](https://github.com/lulu666lulu) ds 的算法

- [Mrs4s](https://github.com/Mrs4s) cqhttp 客户端

- [nonebot](https://github.com/nonebot/nonebot2) nonebot 机器人框架

## License

[MIT](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE)
