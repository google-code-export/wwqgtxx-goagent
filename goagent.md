# 本项目因为[一些原因](https://code.google.com/p/greatagent/wiki/WhyMove)，我们决定迁移到https://code.google.com/p/greatagent/ #

wwqgtxx

<a href='Hidden comment: 

=因为本项目被GFW盯上，我们决定迁移到[https://code.google.com/p/greatagent/]，下面内容请大家无视=


------
==使用客户端==
# 下载wwqgtxx-goagent，[https://code.google.com/p/wwqgtxx-goagent/wiki/downloads?tm=2]，并解压
# 运行文件夹中的wwqgtxx-goagent.bat
* 设置浏览器或其他需要代理的程序代理地址为127.0.0.1:8087
* 注意：使用过程中要一直运行wwqgtxx-goagent.bat
* 提醒：刚启动时出现网页无法显示属于正常情况，程序需要完成自动更新以及寻找配置服务端的任务，请耐心等待。
* 代理地址127.0.0.1:8087；如需使用PAC，设置pac地址为http://127.0.0.1:8086/proxy.pac；如需配合SwitchySharp/AutoProxy等浏览器扩展（SwitchySharp用户可从local文件夹中的SwitchyOptions.bak文件导入配置）
# 导入证书
* 使用管理员身份运行goagent.exe会自动向系统导入IE/Chrome的证书，你也可以双击local文件夹中的CA.crt安装证书；Firefox需要单独导入证书，打开FireFox?->选项->高级->加密->查看证书->证书机构->导入证书, 选择local\ca.crt, 勾选所有项，导入。
------
==附：浏览器详细设置方法==
# ===IE浏览器设置===
* IE有两种方式，分别为全部使用goagent代理和是pac自动代理
* 工具->Internet选项->连接，局域网用户单击局域网设置，宽带用户选择宽带连接之后单击设置
# 设置代理为127.0.0.1:8087，全部使用goagent代理
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/001.png]
* 不使用时要将IE恢复无代理状态
# 使用PAC自动代理
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/002.png]
# ===谷歌chrome配合Proxy  SwitchySharp扩展==
# 安装扩展
* 打开扩展管理页chrome://chrome/extensions/ ，将local文件夹中的SwitchySharp-0.9-beta-r48.crx拖拽到该页面之后点击确定即可安装，扩展也可以从chrome应用商店获得[https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm]
# 导入设置
* 点击 Proxy  SwitchySharp图标->选项->倒入/导出->[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/003.png]
* 浏览到SwitchyOptions.bak，点击确定导入设置
* 更新自动切换规则（先运行goagent再更新规则）
* 在扩展设置页点击“切换规则”，点击“立即更新列表”，最后点击“保存”。[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/004.png]
* 单击地址栏右侧Proxy  SwitchySharp图标即可进行模式选择
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/005.png][https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/006.png]
# GoAgent模式  除匹配proxy.ini中sites的外，全部通过GAE
# GoAgent PAAS模式   无需理睬
# GoAgent Socks5模式   无需理睬
# 自动切换模式 根据切换规则自动选择是否进行代理，自动选择使用何种代理
* 遇到规则中没有的，可以使用扩展的“新建规则”按钮自行添加
# ===Firefox配合FoxyProxy扩展===
# 安装扩展[https://addons.mozilla.org/zh-cn/firefox/addon/foxyproxy-standard/ https://addons.mozilla.org/zh-cn/firefox/addon/foxyproxy-standard/]
# 设置
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/007.png]
* 右击foxyporxy图标即可选择代理模式
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/008.png]
# ===Firefox配合AutoProxy扩展===
# 安装扩展[https://addons.mozilla.org/zh-cn/firefox/addon/autoproxy/ https://addons.mozilla.org/zh-cn/firefox/addon/autoproxy/]
# 设置
# 添加代理服务器
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/009.png][https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/010.png][https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/011.png]
# 添加规则订阅
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/012.png][https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/013.png]
# 选择自己需要的模式
[https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/014.png]
# 自动模式   根据规则自行选择是否使用代理
# 全局模式   全部使用代理
# 禁用代理   全部不使用代理
# 或者直接使用使用已安装好autoproxy的Firefox便携版本：[https://code.google.com/p/wwqgtxx-goagent/wiki/firefox 下载]

==wwqgtxx-goagent适用环境==
* 适用：浏览器，下载软件等
* 不适用：游戏客户端等需要稳定网络的程序，QQ，tor（验证证书）。
------
=﹡﹡﹡请勿到本页提交软件使用问题﹡﹡﹡=
* bug反馈等请到[https://code.google.com/p/wwqgtxx-goagent/issues/list issues]页提交
* 可以在本页提出有关本wiki的建议等，请勿提交无关内容
------
===by wwqgtxx===
'></a>