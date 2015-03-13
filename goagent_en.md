## Client ##
  1. The the download wwqgtxx-goagent Select https://code.google.com/p/wwqgtxx-goagent/wiki/download_en, and extract
  1. Run folder in wwqgtxx-goagent.bat
    * Set the browser or other agent program proxy address 127.0.0.1:8087
    * Note: The use of the process has been running wwqgtxx-goagent.bat
    * Reminder: just start page shows the 503 error, please use the latest version added automatically determine the appid whether available.
    * Proxy address 127.0.0.1:8087; For more information about using the PAC, set pac address http://127.0.0.1:8086/proxy.pac; For with SwitchySharp / AutoProxy browser extensions (SwitchySharp from the local file folder in SwitchyOptions.bak file import configuration)
  1. Import the certificate
    * Use the Run as administrator goagent.exe automatically imported to the system IE / Chrome certificate, you can also double-click the the local folder CA.crt install the certificate; Firefox require a separate import certificate and open FireFox? -> Options -> Advanced -> Encryption -> View Certificate -> Certificate Authority -> Import Certificate, select local \ ca.crt check all import.

﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎
## Attached: browser settings ##
  1. ### IE browser settings ###
> > There are two ways to IE goagent agents and pac were all automatic proxy
> > Click the Settings tool "Internet Options" connection, click LAN Settings LAN users, broadband users choose a broadband connection
    1. Set the proxy 127.0.0.1:8087, all use goagent agent
> > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/001.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/001.png)
      * To IE recovery when not in use agentless
    1. Automatic proxy using PAC
> > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/002.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/002.png)
  1. ### Google chrome with the Proxy SwitchySharp extension ###
    1. Install extensions
      * Open the Extension Manager page chrome :/ / chrome / extensions / drag the local folder SwitchySharp-0.9-beta-[r48](https://code.google.com/p/wwqgtxx-goagent/source/detail?r=48).crx to the page, and then click OK to install the extensions can also be obtained from the chrome app store [https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm](.md)
    1. Import Settings
      * Click the Proxy SwitchySharp icon "option" pour / export "![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/003.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/003.png)
      * Browse to SwitchyOptions.bak, click OK to import settings
      * Update automatically switch rules (first to run goagent update rules)
        * In extended settings page click "switching rules", click on the "Update List", and finally click "Save". ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/004.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/004.png)
      * Click on the right side of the address bar the Proxy SwitchySharp icon to mode selection
> > > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/005.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/005.png) ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/006.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/006.png)
> > > > The # GoAgent the mode except match proxy.ini sites all through GAE
        1. GoAgent PAAS mode without ignoring
        1. GoAgent Socks5 mode no need to ignore
        1. Automatic switching mode is automatically selected according to the switching rule whether the agent automatically select what agent
        * Encounter rules can be used to expand the "New Rule" button to add their own
  1. ### The Firefox with FoxyProxy extension ###
    1. Installed extensions [https://addons.mozilla.org/zh-cn/firefox/addon/foxyproxy-standard/](https://addons.mozilla.org/zh-cn/firefox/addon/foxyproxy-standard/)-
    1. Set

> > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/007.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/007.png)
      * Right click foxyporxy icon to select proxy mode
> > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/008.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/008.png)
  1. ### Firefox with AutoProxy extension ###
    1. Installed extensions [https://addons.mozilla.org/zh-cn/firefox/addon/autoproxy/](https://addons.mozilla.org/zh-cn/firefox/addon/autoproxy/)-
    1. Set
      1. Add the proxy server
> > > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/009.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/009.png) ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/010.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/010.png) ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/011.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/011.png)
      1. Add rules Subscribe
> > > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/012.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/012.png)] ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/013.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/013.png)
      1. Choose their mode
> > > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/014.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/goagent.files/014.png)]
> > > > The # automatic mode according to the rules to choose whether or not to use a proxy
        1. Global mode all use a proxy
        1. Disable all without using a proxy agent
    1. Or directly using the portable version of Firefox installed autoproxy: [Download](https://code.google.com/p/wwqgtxx-goagent/wiki/firefox)

## Applicable environmental goagent ##
  * Applies: browser, download software
  * NA: game client program needs a stable network, QQ, to tor (verification certificate). To be added. . .
﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎ ﹎
﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊ ﹊
# **Not to this page submission software use problems** #
  * Bug feedback, please go to [issues](https://code.google.com/p/wwqgtxx-goagent/issues/list) page submitted

> Please do not submit irrelevant content 