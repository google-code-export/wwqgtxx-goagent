# **wwqgtxx-goagent** #

## 一个为goagent/新版wallproxy提供免费公共服务端的项目，在此先感谢goagent和wallproxy作者为我们无私的奉献，向他们敬礼 ##

项目地址：https://code.google.com/p/wwqgtxx-goagent/


---

### 项目宗旨 ###

本项目的宗旨是为goagent/新版wallproxy提供公共开放的的服务端，同时做出一些优化，以便于大家的使用。

---


  * ### <font color='red'>发现360系列软件会严重干扰本程序运行，请各位用户使用本项目产品时务必停止使用360产品(已禁止在有360的电脑上运行)，最好360杀毒用<a href='http://www.ijinshan.com/'>金山毒霸</a>代替，360安全卫士用<a href='http://guanjia.qq.com/'>腾讯电脑管家</a>代替，360浏览器用<a href='http://firefox.com.cn/download/'>firefox</a>代替，保证上网不被跟踪.</font>(编注：如果你的安全要求很高高，金山毒霸、腾讯电脑管家也不要用，全部用国外的杀毒和防火墙，如：用小红伞代替360杀毒、金山毒霸，用ZoneAlarm、Comodo代替国内防火墙！) ###

  * ### <font color='green'>请从 <a href='https://code.google.com/p/wwqgtxx-goagent/downloads/list'>downloads</a> 中选择合适版本wwqgtxx-goagent/wwqgtxx-wallproxy下载，downloads中永远是最新版，请根据下文说明选择wwqgtxx-goagent/wwqgtxx-wallproxy版本，配合下载中的firefox使用</font> ###


---

### 公告 ###

  * chrome 出现证书错误警告的话， 可以通过添加 --ignore-certificate-errors 启动参数忽略(wallproxy暂时无此问题)
  * 请各位电影族节约使用，尽量使用自己appid，造福大家
  * 说明：新版wallproxy是基于旧版wallproxy、兼容goagent而编写的新一代工具


---

### [If you are English ,Please Here](https://code.google.com/p/wwqgtxx-goagent/wiki/Summary) ###

---


## 最新说明： ##

<font color='#CD853F'>

<ul><li>服务端:更新到goagent2.1.9兼容goagent2.0.14和wallproxy2.1.11，提高服务端性能，统一更换一次密码<br>
</li><li>goagent:再次增加可用ip(应该有700多个)，提高稳定性<br>
</li><li>wallproxy:更新到wallproxy2.1.11修复大量bug</li></ul>

</font>

---


## 版本区别: ##

<font color='#00CED1'>
<ul><li>wwqgtxx-goagent2.1--使用goagent2.1系列版本构建，抗封锁能力较强，速度较慢（用于看网页，上facebook，twitter，google+等）<br>
</li><li>wwqgtxx-goagent2.0--使用goagent2.0系列构建，抗封锁能力较弱，速度较快（用于看网页，上facebook，twitter，google+等）<br>
</li><li>wwqgtxx-wallproxy2.1--使用wallproxy2.1系列构建，抗封锁能力一般，速度一般，但看电影速度很快（特别适合用于看youtube的电影），可以支持智能代理，自动选择是否走代理(需要自行设置8086为代理端口，于autoproxy功能类似，由于firefox的autoproxy插件功能更为强大，所以默认未8086端口):，稳定性强于goagent<br>
</li><li>wwqgtxx-firefox（免配置的firefox，自带autoproxy插件，需要另行下载上面的客户端请根据需要选择）:</li></ul>

</font>

---

## 使用帮助---wwqgtxx-goagent ##

<font color='purple'>

<ul><li>简便方法：下载解压后，打开goagent.exe，下载downloads中的firefox打开即可使用</li></ul>

<ul><li>下载中的wwqgtxx-goagent已配置好60个公共服务端，请先启动goagent.exe（如需设置为开机启动，请双击打开addto-startup.vbs），请设置浏览器的代理地址为127.0.0.1，端口为8087使用<br>
</li><li>强烈建议使用<a href='http://firefox.com.cn/download/'>firefox</a>+<a href='https://addons.mozilla.org/zh-CN/firefox/addon/autoproxy/'>autoproxy</a>（可以下载配置好的firefox在下载中）<br>
</li><li>或使用PAC模式，pac文件地址为<a href='http://127.0.0.1:8086/proxy.pac'>http://127.0.0.1:8086/proxy.pac</a>
</li><li>chrome请安装SwitchySharp插件，然后导入这个设置<a href='https://goagent.googlecode.com/files/SwitchyOptions.bak'>https://goagent.googlecode.com/files/SwitchyOptions.bak</a>
</li><li>firefox请安装FoxyProxy，Firefox需要导入证书，方法请见FAQ<br>
(Firefox怎么不能登陆twitter/facebook等网站, Firefox如何导入证书?<br>
<blockquote>打开FireFox->选项->高级->加密->查看证书->证书机构->导入证书, 选择local\ca.crt, 勾选所有项，导入。<br>
）</blockquote></li></ul>

</font>

## 使用说明---wwqgtxx-wallproxy ##

<font color='purple'>

<ul><li>简便方法：下载解压后，打开wallproxy.exe(或python.exe或Run.bat)再下载downloads中的firefox，打开即可使用</li></ul>

<ul><li>标准方法:<br>
</li></ul><ol><li>打开wallproxy.exe(或python.exe)，代理地址127.0.0.1:8087；如需使用PAC，设 置<a href='http://127.0.0.1:8087/proxy.pac；如需使用'>http://127.0.0.1:8087/proxy.pac；如需使用</a> switchysharp/autoproxy等浏览器扩展（SwitchySharp用户可导入配置local\misc\SwitchyOptions.bak），与 goagent设置方法相同；如需使用智能代理（使无 法使用PAC或扩展的程序也做到该走代理走代 理，不该走就不走），设置127.0.0.1:8086为代理 即可。<br>
</li><li>导入<a href='http://127.0.0.1:8086/CA.crt'>http://127.0.0.1:8086/CA.crt</a> 为浏览器根证书 （cmd窗口提示时间与导入后查看到的时间相同 基本就是导入成功了，升级版本时请保留cert目 录，以免需要再次导入）<br>
</li><li>可通过 <a href='http://127.0.0.1:8086或http://wallproxy访问'>http://127.0.0.1:8086或http://wallproxy访问</a></li></ol>

</font>

---

<font color='#F08080'>

<h3>请各位多多堆广本项目，大家使用的好才是项目发展的动力</h3>

<ul><li>本项目提供的60个服务端（出于节约流量和项目长远安全考虑）不支持<b>看电影(youtube除外)</b>服务，同时也不提供访问<b>国内网站</b>的服务，另外权衡了一下安全也为了支持一下我们的服务提供商google，屏蔽了其他搜索，搜索时请使用google ssl版以保证不被监听，如需使用已屏蔽的服务，请自行搭建服务端，详见<a href='https://code.google.com/p/goagent/'>goagent</a>和<a href='https://code.google.com/p/wallproxy'>wallproxy</a>项目</li></ul>

<ul><li><h2>特别说明：如果出现Over Quota应多多刷新（刷新一次更换一次服务器，最多刷60次吧，请大家理解），wwqgtxx-wallproxy无此现象，出现server is update 说明您的客户端程序须要更新了，请各位到download页面下载</h2></li></ul>

<ul><li><h3>注：刷新非google页面才有作用</h3></li></ul>

<ul><li>60个服务端每天有60GB流量，如果出现503: Service Unavailable 请反复刷新，是正在更换服务端，若刷新30次以上仍出现503，一般是流量用完了，请等待下午4点之后，再使用（正在向goagent作者提出添加自动判断服务器是否可用的功能，希望作者能尽快添加，wwqgtxx-wallproxy无此问题）</li></ul>

<ul><li>欢迎大家到Issues中提出意见</li></ul>


<h2>出现一下情况是<b>正常</b>的：</h2>

<ol><li>刚开启是无法连接，因为刚开启时wwqgtxx-goagent/wwqgtxx-wallproxy会逐一寻找可用的服务端<br>
</li><li>出现Hosts Deny，表示该网站不应该通过本项目访问，应通过自行架设服务端解决或直接访问<br>
</li><li>出现503错误，参见上文</li></ol>

</font>


---

### 基础知识 FAQ ###

<font color='gray'>

<ul><li>wwqgtxx-goagent/wwqgtxx-wallproxy是什么？<br>
<blockquote>wwqgtxx-goagent/wwqgtxx-wallproxy是使用Goagent和新版Wallproxy编写的网络软件，为其提供公共服务端，可以运行在Windows/Mac/Linux上。<br>
</blockquote></li><li>遇到FAQ没有解决问题怎么办?<br>
<blockquote>首先请更新客户端和服务端到最新版(见首页)，如果还有问题的话请到<a href='https://code.google.com/p/wwqgtxx-goagent/issues/list'>https://code.google.com/p/wwqgtxx-goagent/issues/list</a> 提出issue。提issue前建议先搜索下看是否是重复的问题，请尽量描述问题产生的原因，配置情况，网络情况等，这样有助于重现问题并解决。虽然我们可能顾不上回答，但是我们保证每个issue都会看的并尝试解决的。<br>
</blockquote></li><li>google reader提示404错误？<br>
<blockquote>使用<a href='https://www.google.com/reader'>https://www.google.com/reader</a> 访问.<br>
</blockquote></li><li>在 Linux/Mac 下如何安装 gevent?<br>
<blockquote>在shell命令执行如下语句(注意需要安装 gcc 或 xcode): curl -k -L <a href='http://git.io/I9B7RQ|sh'>http://git.io/I9B7RQ|sh</a>
</blockquote></li><li>提示Error code 502错误怎么办？<br>
<blockquote>503: Service Unavailable 一般是流量用完了，请等待下午4点之后<br>
</blockquote></li><li>我是Mac/Linux用户怎么办？<br>
<ol><li>wwqgtxx-goagent：在终端直接运行python proxy.py即可。需要Python版本2.6以上。Mac用户可以尝试 GoAgent Mac GUI 或者GoAgentX<br>
</li><li>wwqgtxx-wallproxy：非Windows用户运行startup.py<br>
</li></ol></li><li>如何设为系统服务（开机自启动）？<br>
<ol><li>wwqgtxx-goagent：双击addto-startup.vbs即可。<br>
</li><li>wwqgtxx-wallproxy：加入开始菜单的启动文件夹开机运行就行了啊，或者用GUI设置开机启动。建议方法：proxy.exe右键菜单选择“发送到桌面快捷方式”，生成的桌面快捷方式上右键选择“属性”，在目标后面加上 --hide --single，如果觉得图标太难看可以顺便“更改图标”，例如换成GUI的，“确定”，复制该快捷方式到“开始”菜单的“启动”文件夹。<br>
</li></ol></li><li>wwqgtxx-goagent/wwqgtxx-wallproxy支持IPv6网络吗？<br>
<blockquote>支持的。proxy.ini中profile=google_ipv6即可。<br>
</blockquote></li><li>为什么wwqgtxx-goagent/wwqgtxx-wallproxy第一次运行需要管理员权限？<br>
<blockquote>因为wwqgtxx-goagent/wwqgtxx-wallproxy会尝试调用certmgr.exe向系统导入IE/Chrome的证书，这需要管理员权限。</blockquote></li></ul>

</font>


## by wwqgtxx ##