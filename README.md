# UniversalMessagePushFramework
A python(flask)-based simple universal message push framework or system. This framework enable message requested by on a local server, works like a USB hub. It's more secure if tokens are not distributed on any projects. It's also flexible to add additional feature on your own, like encrypt or tls, or just delete it. For example, Dingtalk can be useless for non-Chinese users.


Current support platform:

 - E-Mail
 - DingTalk

We are also interested to build a simple web panel to indicate server status.

# 统一消息推送框架

简单的自部署统一推送服务平台。这个项目像集线器一样，把涉及token之类的核心信息保留在单一服务而非任意应用程式。推送可达钉钉、邮件等，可根据需要进行二次开发，如加密或添加新的通知服务。例如钉钉对海外用户无用，是完全可以删掉的模块。

目前支援的一些平台或推送方式：

- 邮件
- 钉钉

我们也同样对简单的网页可视化面板感兴趣，这可以使得服务器状态被轻松列印。
