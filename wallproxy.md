# 本项目因为[一些原因](https://code.google.com/p/greatagent/wiki/WhyMove)，我们决定迁移到https://code.google.com/p/greatagent/ #

wwqgtxx

<a href='Hidden comment: 
=因为本项目被GFW盯上，我们决定迁移到[https://code.google.com/p/greatagent/]，下面内容请大家无视=


------
<wiki:toc max_depth="2"/>
----
==第一步：下载wwqgtxx-wallproxy==
# 首先从[https://code.google.com/p/wwqgtxx-goagent/wiki/downloads?tm=2]下载wwqgtxx-wallproxy，并解压，运行wwqgtxx-wallproxy.bat。
# 代理地址127.0.0.1:8087；如需使用PAC，设置[http://127.0.0.1:8087/proxy.pac]；如需使用SwitchySharp/AutoProxy等浏览器扩展（SwitchySharp用户可导入配置local\misc\SwitchyOptions.bak），见图文教程（GUI应该选择“禁用切换”）；如需使用智能代理（使无法使用PAC或扩展的程序也做到该走代理走代理，不该走就不走），设置127.0.0.1:8086为代理即可。
# 导入[http://127.0.0.1:8086/CA.crt]为浏览器根证书可消除浏览器证书警告（cmd窗口提示时间与导入后查看到的时间相同基本就是导入成功了，升级版本时请保留cert目录，以免需要再次导入）
# 可通过[http://127.0.0.1:8086]或[http://wallproxy]访问Web配置界面

==第二步：运行客户端==
# 运行local文件夹下wwqgtxx-wallproxy.bat，完成自动更新后可显示下图
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image011.png]
双击托盘图标，可出现控制台窗口
# 托盘左键菜单用于配置代理，右键菜单配置程序。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image013.png]
# 直接连接：强制浏览器不使用代理；
# GAE代理：强制浏览器使用127.0.0.1:8087作为代理（除部分google网站外，大部分网站都走GAE）；
# 智能代理：强制浏览器使用127.0.0.1:8086作为代理，由wallproxy智能判断是否需要走GAE，如果直连失败，可自动改走GAE；
# 自动代理：由浏览器通过PAC判断是否需要走GAE，与智能代理相比性能损失小，但无法做到在直连失败时改走GAE；
# 禁用切换：强制IE不使用代理；以上4个选择在每次运行WallProxy.exe时都会去修改IE代理为所选择项，而选择“禁用切换”后下次运行不会对IE代理做任何修改。*使用SwitchySharp/AutoProxy等浏览器扩展管理代理的用户，请选择此项* 。
# 如果需要自定义这些菜单，可以选择“设置代理”菜单项：
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image014.png]
勾选“退出时恢复无代理”可在退出WallProxy.exe时将IE代理修改为无代理，以免影响正常使用；勾选“禁用代理切换”效果类似于“禁用切换”菜单。
如果使用如图所示的拨号上网方式，将连接名称填入上图“连接名称”，例如下图“连接 宽带连接”，将“宽带连接”填入即可。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image015.jpg]
# 打开浏览器输入：[http://www.facebook.com]，并成功访问。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image016.jpg]
# 自定义代理规则，访问[http://wallproxy/]或者[http://127.0.0.1:8086/]，再点击“自定义规则”，输入要走GAE的规则后保存即可：
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image017.jpg]
==附录==
===附录一：浏览器简便设置方法===
# 直接下载[https://code.google.com/p/wwqgtxx-goagent/wiki/downloads?tm=2 	wwqgtxx-wallproxy-Release-withFirefox版本]，打开不用配置，可以直接使用

===附录二：`Firefox + WallProxy`===
# 使用系统代理
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image019.jpg]
# 导入根证书
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image020.jpg]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image021.png]
# 检查导入是否正确（可选），时间相同，说明没有导错：
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image022.jpg]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image023.jpg]

===附录三：配合`Chrome + SwitchySharp`使用方法===
[]*GUI左键菜单选择“禁用切换”* ，按下图导入配置，之后“直接连接”、“GAE代理”、“智能代理”、“自动代理”作用与WallProxy.exe相同。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image024.jpg]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image025.png]

===附录四：配合`Firefox + FoxyProxy`使用方法===
[]*GUI左键菜单选择“禁用切换”* ，如图所示依次添加“GAE代理”127.0.0.1:8087，“智能代理”127.0.0.1:8086，“自动代理”[http://127.0.0.1:8087/proxy.pac]。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image026.jpg]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image027.jpg]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image028.jpg]

===附录五：配合`Firefox + AutoProxy`使用方法===
[]*GUI左键菜单选择“禁用切换”* ，相比之下AutoProxy是比个强大的代理扩展，如果找不到以下对话框从哪些菜单找出来，还是改用配置好的[https://code.google.com/p/wwqgtxx-goagent/wiki/firefox firefox]吧。
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image029.png]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image030.png]
[https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image031.png]

------
===by wwqgtxx===
'></a>