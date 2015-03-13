# **wwqgtxx-goagent** #

## 一个为goagent/新版wallproxy提供免费公共服务端的项目，在此先感谢goagent和wallproxy作者为我们无私的奉献，向他们敬礼 ##

项目地址：https://code.google.com/p/wwqgtxx-goagent/


---

### 项目宗旨 ###

> 本项目的宗旨是为goagent/新版wallproxy提供公共开放的的服务端，同时做出一些优化，并且提供免配置的firefox，以便于大家的使用。

---


  * <font color='red'>发现<del>360系列软件</del>会严重干扰本程序运行，请各位用户使用本项目产品时务必停止使用<del>360产品</del>(因为360会监视你的一举一动，并发送给网警部门，小心被请喝茶)，请务必把<del>360杀毒</del>彻底卸载用<a href='http://www.ijinshan.com/'>金山毒霸</a>或其他杀毒软件代替，<del>360安全卫士</del>用<a href='http://guanjia.qq.com/'>腾讯电脑管家</a>代替，<del>360浏览器</del>务必用<a href='firefox.md'>Firefox 火狐浏览器 (著名的国外开源浏览器，强烈推荐使用)</a>代替，保证上网不被跟踪.</font>
  * (注：如果你的安全要求很高，金山毒霸、腾讯电脑管家也不要用，全部用国外的杀毒和防火墙，如：用小红伞代替360杀毒、金山毒霸，用`ZoneAlarm`、`Comodo`代替国内防火墙！)

---


  * ### <font color='green'>请从 <a href='https://code.google.com/p/wwqgtxx-goagent/downloads/list'>downloads</a> 中选择合适版本wwqgtxx-goagent/wwqgtxx-wallproxy下载，downloads中永远是最新版，请根据下文说明选择wwqgtxx-goagent/wwqgtxx-wallproxy版本，配合下载中的<a href='firefox.md'>firefox</a>使用</font> ###


---

### 公告 ###

  * chrome 出现证书错误警告的话， 可以通过添加 --ignore-certificate-errors 启动参数忽略(wwqgtxx-wallproxy暂时无此问题)证书错误，也可以使用[firefox](firefox.md)代替。
  * 强烈推荐大家使用开源的firefox浏览器，拥抱自由的互联网，[下载页面](firefox.md)。
  * 请各位电影族使用wwqgtxx-wallproxy，内置专用电影id，可以看**任何电影**，(有180个appid专用的偶)
  * ### wwqgtxx-goagent以加入自动判断appid是否可用的功能，请使用最新版本。 ###
  * 说明：新版wallproxy是基于旧版wallproxy、兼容goagent而编写的新一代fq工具


---

### [If you are English ,Please Here](Summary.md) ###

---


## 最新说明： ##

<font color='#CD853F'>

<ul><li>服务端:更新到goagent2.1.11兼容goagent2.0.14和wallproxy2.1.13，增加130个服务端，提高服务端性能，目前有290个服务端，修改一次密码，让更多的人更新。<br>
</li><li>goagent:更新到goagent2.1.11-97，速度大幅度提升， <b>加入自动判断appid是否可用的功能</b> ，增加上述的130个服务端服务端。<br>
</li><li>wallproxy:更新到wallproxy2.1.13.2修复大量bug，可以看所有电影了(不支持gae的网站除外，比如部分日本网站)<br>
</li><li>firefox:增加firefox esr17.0.2以及firefox18.0，为firefox安装大量插件。<br>
</li><li>项目主页:增加对firefox的说明</li></ul>

</font>

---


## 版本区别: ##

<font color='#00CED1'>
<ul><li>wwqgtxx-goagent2.1--使用goagent2.1系列版本构建，抗封锁能力较强，速度较慢（适合用于看网页，上facebook，twitter，google+等）<br>
</li><li>wwqgtxx-goagent2.0--使用goagent2.0系列构建，抗封锁能力较弱，速度较快（适合用于看网页，上facebook，twitter，google+等）<br>
</li><li>wwqgtxx-wallproxy2.1--使用wallproxy2.1系列构建，抗封锁能力一般，速度一般，但看<b>电影速度很快</b>（特别适合<code>YouTube</code>）用于看只要gae可以访问的电影的电影，使用无限制电影appid，保证你畅快的电影享受<br>
</li><li>wwqgtxx-firefox（免配置的firefox，已导入证书，自带autoproxy插件，需要另行下载上面的客户端请根据需要选择）:<a href='firefox.md'>https://code.google.com/p/wwqgtxx-goagent/wiki/firefox</a>
<ul><li>firefoxportable16.0.1:<br>
<blockquote><a href='firefox.md'>firefox</a>经典版本，纯净版，除了autoproxy无其他插件，下载地址：<a href='https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortable.7z'>https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortable.7z</a>
</blockquote></li><li>firefoxportable esr 17.0.2:<br>
<blockquote><a href='firefox.md'>firefox</a>的长期支持版本，最稳定的版本，插件同firefoxportable18.0，下载地址：<a href='https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortableESR17.0.2.7z'>https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortableESR17.0.2.7z</a>
</blockquote></li><li>firefoxportable18.0:<br>
<blockquote><a href='firefox.md'>firefox</a>速度最快的版本，内置大量的插件，也是本人使用的版本，非常好用，分享给大家，希望大家都能使用的舒心，下载地址：<a href='https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortable18.0.7z'>https://wwqgtxx-goagent.googlecode.com/files/FirefoxPortable18.0.7z</a></blockquote></li></ul></li></ul>

</font>

---

## 使用帮助---wwqgtxx-goagent ##
  * ## 图文教程：[https://code.google.com/p/wwqgtxx-goagent/wiki/goagent](goagent.md) ##

<font color='purple'>

<ul><li>简便方法：下载<a href='https://code.google.com/p/wwqgtxx-goagent/downloads/list'>downloads</a>中的<a href='firefox.md'>firefox</a>和wwqgtxx-goagent，分别解压，打开goagent.exe和firefoxportable.exe即可使用</li></ul>

</font>

## 使用说明---wwqgtxx-wallproxy ##
  * ## 图文教程：[https://code.google.com/p/wwqgtxx-goagent/wiki/wallproxy](wallproxy.md) ##

<font color='purple'>

<ul><li>简便方法：下载<a href='https://code.google.com/p/wwqgtxx-goagent/downloads/list'>downloads</a>中的<a href='firefox.md'>firefox</a>和wwqgtxx-wallproxy，分别解压，打开wallproxy.exe(或python.exe或Run.bat)和firefoxportable.exe即可使用。</li></ul>

</font>

---

<font color='#F08080'>

<h2>公共服务端说明</h2>

<ul><li>请各位多多堆广本项目，大家使用的好才是项目发展的动力</li></ul>

<ul><li>本项目提供的供wwqgtxx-goagent使用的290个服务端（出于节约流量和项目长远安全考虑）在电影网站方面只支持<b>看youtube视频</b>服务，不支持其他视频网站，同时也不提供访问<b>国内网站</b>的服务，另外权衡了一下安全也为了支持一下我们的服务提供商google，屏蔽了其他搜索，搜索时请使用google ssl版以保证不被监听，如需使用已屏蔽的服务，请使用下面电影服务端。<br>
</li><li>本项目提供的180个电影服务端无上述限制，可以自由访问系列gae可以访问的网站，只部署在wwqgtxx-wallproxy上(流量有限，好好使用)。</li></ul>

<ul><li>如果出现Over Quota应使用<b>最新版本</b>，以加入自动判断appid是否可用的功能。，出现server is update 说明您的客户端程序须要更新了，请各位到download页面下载<br>
<blockquote>注：刷新非google页面才有作用</blockquote></li></ul>

<ul><li>当遇到反复循环刷新Appid时，请确定是循环刷新(就是同一个Appid在程序输出中输出了一遍又一遍，不是同一个Appid就不是循环刷新)，一般的刷新是正常的，循环刷新表示当天流量已经用尽，需要等待北京时间下午4点重置流量之后使用(请关闭程序后再打开)</li></ul>

<ul><li>欢迎大家到Issues中提出意见</li></ul>


<ul><li>出现一下情况是<b>正常</b>的：<br>
<ol><li>刚开启是无法连接，因为刚开启时wwqgtxx-goagent/wwqgtxx-wallproxy会逐一寻找可用的服务端<br>
</li><li>出现Hosts Deny，表示该网站不应该通过本项目访问，应通过自行架设服务端解决或直接访问</li></ol></li></ul>

</font>


---

### 基础知识 FAQ ###
[FAQ https://code.google.com/p/wwqgtxx-goagent/wiki