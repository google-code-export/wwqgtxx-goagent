# 本项目因为[一些原因](https://code.google.com/p/greatagent/wiki/WhyMove)，我们决定迁移到https://code.google.com/p/greatagent/ #

wwqgtxx

<a href='Hidden comment: 


------
===基础知识 FAQ===

<font color="gray">

* wwqgtxx-goagent/wwqgtxx-wallproxy是什么？
wwqgtxx-goagent/wwqgtxx-wallproxy是使用Goagent和新版Wallproxy编写的网络软件，为其提供公共服务端，可以运行在Windows(支持自动更新)和Mac/Linux(不支持自动更新)上。
* 遇到FAQ没有解决问题怎么办?
首先请自动更新客户端到最新版(见首页)，如果还有问题的话请到https://code.google.com/p/wwqgtxx-goagent/issues/list 提出issue。提issue前建议先搜索下看是否是重复的问题，请尽量描述问题产生的原因，配置情况，网络情况等，这样有助于重现问题并解决。虽然我们可能顾不上回答，但是我们保证每个issue都会看的并尝试解决的。
* google reader提示404错误？
使用https://www.google.com/reader 访问.
* 在 Linux/Mac 下如何安装 gevent?
在shell命令执行如下语句(注意需要安装 gcc 或 xcode): curl -k -L http://git.io/I9B7RQ|sh
* 我是Mac/Linux用户怎么办？
#  wwqgtxx-goagent：在终端直接运行python proxy.py即可。需要Python版本2.6以上。
#  wwqgtxx-wallproxy：非Windows用户运行startup.py
* 如何设为系统服务（开机自启动）？
#  wwqgtxx-goagent：双击addto-startup.vbs即可。
#  wwqgtxx-wallproxy：加入开始菜单的启动文件夹开机运行就行了啊，或者用GUI设置开机启动。建议方法：proxy.exe右键菜单选择“发送到桌面快捷方式”，生成的桌面快捷方式上右键选择“属性”，在目标后面加上 --hide --single，如果觉得图标太难看可以顺便“更改图标”，例如换成GUI的，“确定”，复制该快捷方式到“开始”菜单的“启动”文件夹。
* wwqgtxx-goagent/wwqgtxx-wallproxy支持IPv6网络或者公司内部需要使用代理的网络吗？
目前不支持。
* 为什么wwqgtxx-goagent/wwqgtxx-wallproxy第一次运行需要管理员权限？
因为wwqgtxx-goagent/wwqgtxx-wallproxy会尝试调用certmgr.exe向系统导入IE/Chrome的证书，这需要管理员权限。



Unknown end tag for &lt;/font&gt;


'></a>