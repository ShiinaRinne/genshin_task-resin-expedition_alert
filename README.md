# Hoyolab Resin
用来提示和查询原神内树脂、委托、派遣情况的小工具，近期的迭代可能会比较快。

## 示例

**企业微信**

![](https://i.loli.net/2021/10/19/uoGFiY7b1fecZhR.png)

**Server酱**

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
* 请确保米游社的实时便笺权限已经打开
* 获取cookie

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
0. 安装 [python3](https://www.python.org) 环境，版本>=3.9。

    如果你的服务器已经有了较低版本的 python 环境，此处以 Centos 为例：

    ```shell
    yum install epel-release
    yum install python39
    pip3.9 install -r requirements.txt
    python3.9 index.py
    ```
    Ubuntu、Windows作类似修改或安装虚拟环境皆可(大概?)。

1. 下载项目并安装依赖
    ```shell
    git clone https://github.com/yaomeng0722/genshin_task-resin-expedition_alert.git
    cd genshin_task-resin-expedition_alert
    pip3 install -r requirements.txt
    ```
2. 修改配置

    复制 `./alert/config_data/config.example.json` 并另存为 `config.json`，填入配置信息。
    ```
    cp ./alert/config_data/config.example.json ./alert/config_data/config.json
    vi ./alert/config_data/config.json
    ```
3. 运行项目
    ```
    python3 index.py
    ```



## 推送方式配置

**推送渠道未全部测试完成，详情如下**

| 推送渠道     | 支持情况 | 备注              |
| :----------: | :------: | :---------------: |
| [Server 酱](https://sct.ftqq.com/) | ✅支持    | 免费版每天限制5条 |
| [企业微信](https://work.weixin.qq.com/api/doc/90000/90136/91770) | ✅支持    |                   |
| [钉钉群机器人](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027) | ✅支持    |                   |
| [pushplus](https://www.pushplus.plus/) | ✅支持    |                   |
| [Telegram Bot](https://core.telegram.org/bots) | ✅支持    |                   |
| [Cool Push](https://cp.xuthus.cc/) | ✅支持    |  推荐私有化部署  |
| [Qmsg酱](https://qmsg.zendee.cn/) | ✅支持    |                   |
| [Bark](https://github.com/Finb/Bark) | ✅ 支持   |                     |
| [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) | ✅ 支持   |                     |
| QQ | ✅支持    | 基于 NoneBot2 |
| [Discord_Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) | 🛠️未测试 |                   |
| [IGOT](https://push.hellyw.com/doc/#/) | 🛠️未测试 |                   |

| 自定义推送 | ❌暂不支持 |                   |


### 0. 一些基础信息
1. UID: 你游戏内的uid，填入config -> UID
1. COOKIE: 在[原神米游社社区](https://bbs.mihoyo.com/ys)获取到的cookie 
    获取方式：
    
    ```
    javascript:(function(){let domain=document.domain;let cookie=document.cookie;prompt('Cookies: '+domain, cookie)})();`
    ```
    复制上面的代码存储为书签，打开社区之后，点击该书签，复制弹出的信息并填入config -> COOKIE即可。

### 1. Server 酱
<details>

1. 前往[Server酱](https://sct.ftqq.com/) 官网注册并绑定微信。

2. 将获取到的`send key`填入`config.json -> SCKEY`中即可。

注：Server酱免费版每天有5次的调用次数上限。

</details>

### 2. 企业微信
<details>

1. [注册企业微信](https://work.weixin.qq.com/) ，个人即可注册，不需要进行企业身份验证。

2. 在"应用管理"中创建新应用

![](https://youngmoe.com/img/hoyolab_resin/1.png)

3. 在应用中查看agentid与secret分别填入config -> WECOM_AGENT_ID 与 config -> WECOM_SECRET (注：secret需要在手机端的企业微信进行查看)

![](https://youngmoe.com/img/hoyolab_resin/3.png)

4. 在"我的企业"中获取企业id填入config -> WECOM_CORP_ID

![](https://youngmoe.com/img/hoyolab_resin/2.png)

5. 在"通讯录" -> "成员管理" 中获取要收取信息的人员账号填入config -> WECOM_USER_ID

![](https://youngmoe.com/img/hoyolab_resin/4.png)


</details>

### 3. 钉钉群机器人
<details>

1. 创建钉钉群，并添加自定义机器人，参见 [钉钉开放平台·自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027)。

2. 将生成的 Webhook 地址中的 `access_token`填入 `DD_BOT_TOKEN`。

3. 将创建过程中`加签`的密钥填入`DD_BOT_SECRET`。
</details>

### 4. Push Plus
<details>

1. 登录 [pushplus 网站](http://www.pushplus.plus/) ，复制 token 填入 `PUSH_PLUS_TOKEN`。

2. 若要一对多推送，需要创建群组并将群组编号填入 `PUSH_PLUS_USER`，一对一推送无需填写。
</details>


### 5. CoolPush 酷推
<details>

注：现在酷推公共服务不可用，需要私有化部署。

1. 登录 [CoolPush](https://cp.xuthus.cc/)，绑定QQ号/QQ群及私有化部署地址，获取`调用代码Skey`。

2. 将Skey填入 `COOL_PUSH_SKEY` ，`COOL_PUSH_MODE` 支持QQ私聊推送/QQ群消息推送/QQ私有化私聊推送/QQ私有化群聊推送，不支持一对多推送。

3. 如果需要动态的指定推送消息给特定的QQ号或者群，将QQ号/群号填入 `COOL_PUSH_SENDID` 即可。

</details>

### 6. Qmsg酱
<details>

登录 [Qmsg酱](https://qmsg.zendee.cn/)，获取 KEY 填入 `QMSG_KEY` 即可。

注：Qmsg酱容易被判定违规=_=，且无法进行群聊推送（审核不通过）。

</details>

### 7. Bark
<details>

1. 打开 [Bark](https://github.com/Finb/Bark) App，将 App 内提供的 KEY 填入 `BARK_KEY` 即可。

2. 支持部分可选配置，如自定义消息分组 `BARK_GROUP`，自定义通知图标 `BARK_ICON`，自定义消息保存 `BARK_ARCHIVE`。

</details>

### 8. CQ-HTTP
<details>

1. 将 CQ-HTTP 的服务器IP/域名填入 `CQHTTP_IP`，端口号填入 `CQHTTP_PORT`。

2. 配置发送模式 `CQHTTP_MESSAGE_TYPE`，`private` 为私聊发送，`group` 为群聊发送。

3. 配置消息接收方的QQ号/群号，填入 `CQHTTP_SEND_ID`，与发送模式匹配。

4. 若配置了`Access Token`，需要填写 `CQHTTP_TOKEN`。

</details>

### 9. QQBot
<summary>暂时只支持主动查询，只能在windows环境部署，输入/resin xxxx即可获取信息<br>目前支持的有:/resin 树脂/委托/boss/派遣/总览共5项</summary>


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

## 配置文件参数说明

建议使用 [VS Code](https://code.visualstudio.com/) 或其他支持 json-schema 的编辑器编辑配置文件，可自动显示填写提示和进行配置检查。

| Key                       |                      Comment                       |       Remark         |
| ------------------------- | :------------------------------------------------: | :------------------: |
| UID                       |                      游戏uid                       |      100088888       |
| COOKIE                    |                    米游社cookie                    |         ****         |
| NAME                      |                      账号别名                      |    小号/女朋友的号   |
| SCTKEY                    |                   Server酱                         |     SCT********      |
| WW_ID                     |                     企业微信id                     |                      |
| WW_APP_SECRET             |                   企业微信secret                   |                      |
| WW_APP_USERID             |              企业微信接收消息的用户id              |                      |
| WW_APP_AGENTID            |                     企业应用Id                     |       10000001       |
| WW_BOT_KEY                |                 企业微信机器人key                  |                      |
| DD_BOT_TOKEN              |              钉钉机器人 access_token               |                      |
| DD_BOT_SECRET             |                   钉钉机器人加签密钥               |                      |
| PUSH_PLUS_TOKEN           |                PushPlus推送token                   |                      |
| PUSH_PLUS_USER            |               PushPlus一对多推送群组id             |  不填则为一对一推送  |
| TG_BOT_API                |                  Telegram API接口                  |   api.telegram.org   |
| TG_BOT_TOKEN              |                Telegram Bot token                  |                      |
| TG_USER_ID                |                  接收消息账号的userid              | 可用[@userinfobot](https://t.me/userinfobot)获取 |
| COOL_PUSH_SKEY            |                      酷推SKEY                      |                      |
| COOL_PUSH_MODE            |                   酷推推送模式                     | send/psend/group/pgroup |
| COOL_PUSH_SENDID          |                  酷推指定接收方QQ号/群号           |                      |
| QMSG_KEY                  |                   Qmsg酱推送KEY                    |                      |
| BARK_KEY                  |                   Bark App KEY                     |                      |
| BARK_GROUP                |                  自定义 Bark 分组                  |  不填则使用默认分组  |
| BARK_ICON                 |                自定义 Bark 通知图标                | 仅支持 Web URL 图片，不填则不使用自定义图标  |
| BARK_ARCHIVE              |                  自定义 Bark 保存                  | 1 为保存，其他值为不保存，不填则使用默认规则 |
| DISCORD_WEBHOOK           |                       未测试                       |        未测试        |
| IGOT_KEY                  |                       未测试                       |        未测试        |
| CQHTTP_IP                 |                  cq-http的ip地址                   |                      |
| CQHTTP_PORT               |                  cq-http的HTTP端口号               |       默认5700       |
| CQHTTP_MESSAGE_TYPE       |    cq-http的消息发送方式，`private`为私聊，`group`为群聊 |  private/group |
| CQHTTP_SEND_ID            |               接收消息的qq号码/群号码              |                      |
| CQHTTP_TOKEN              |                 cqhttp的CQHTTP_TOKEN               |    未设置不需要填写  |
| RESIN_ALERT_NUM           |               树脂达到多少时进行提示               |         150          |
| RECEIVE_RESIN_DATA        |                是否接收树脂溢出提示                |        ON/OFF        |
| RECEIVE_BOSS_COUNT        |          是否接收本周boss树脂减半剩余次数          |        ON/OFF        |
| RECEIVE_TASK_NUM          |                是否接收每日委托信息                |        ON/OFF        |
| REVEIVE_EXPEDITION_NUM    |                是否接收探索派遣信息                |        ON/OFF        |
| INCOMPLETE_ALERT          |      在这个时间，如果每日委托未完成，进行提示      | "213030"(即21:30:30) |
| EXPEDITION_COMPLETE_ALERT |              当探索派遣完成时发送提醒              |        ON/OFF        |
| SELLP_TIME                | 程序每轮执行的休眠时间，为避免被封ip，建议稍微长点（单位：秒） |   900    |
| ALERT_SUCCESS_SLEEP_TIME  |    提示成功后的休眠时间，为避免扰民可以设置长点（单位：秒）    |   1800   |
| SLEEP_START_TIME          |       休眠开始时间，避免深夜扰民，与`SLEEP_END_TIME`配合使用   | "230000"(即23:00:00) |
| SLEEP_END_TIME            |        休眠结束时间，与`SLEEP_START_TIME`配合使用    | "080000"(即08:00:00) |


## 自定义提示信息：
#### 根据需要修改getinfo中dataanalystic.py与notifiers中的几个文件即可(近几天有空会优化一下，现在有点丑)

## 更新日志

### v1.2.4（2021-11-24）

- BUG FIX：修复 cookie 出错时的异常退出问题

### v1.2.3（2021-11-23）

- CQHTTP 推送IP字段支持协议头，以支持 HTTPS

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

- 增加cqhttp推送
- 更新文档

### v1.1.1 (2021-10-28)

- 增加探索派遣完成提醒
- 优化提醒标题

### v1.1.0 (2021-10-28)

- 修复休眠时间不正确的问题
- 优化提醒逻辑
- 增加账号信息显示

## 致谢

- [Lycreal](https://github.com/Lycreal) 好看的米游社api调用

- [y1ndan](https://www.yindan.me/tutorial/genshin-impact-helper.html) notifiers 多渠道发送消息

- [lulu666lulu](https://github.com/lulu666lulu) ds的算法

- [Mrs4s](https://github.com/Mrs4s) cqhttp客户端

- [nonebot](https://github.com/nonebot/nonebot2) nonebot机器人框架

## License

[MIT](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE)