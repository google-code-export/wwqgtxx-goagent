

---

## Step 1: Download wwqgtxx-wallproxy ##
  1. https://code.google.com/p/wwqgtxx-goagent/wiki/download_en Download wwqgtxx-wallproxy, and extract the run wwqgtxx-wallproxy.bat
  1. Proxy address 127.0.0.1:8087; For PAC, set http://127.0.0.1:8087/proxy.pac; For use browser extensions in `SwitchySharp / AutoProxy` the (`SwitchySharp users can import configuration local \ misc \ SwitchyOptions.bak `), see graphic tutorial (GUI should select" Disable switch "); For the use of intelligent agents (so can not use the PAC or expand the program to do the walking agent to take the agent should not go not go), the set 127.0.0.1:8086 agent can.
  1. Import http://127.0.0.1:8086/CA.crt browser root certificate to eliminate browser certificate warning (cmd window view to the prompt time and import the same basic is the import was successful, the upgrade version Please keep the cert directory, in order to avoid the need to import again)
  1. By http://127.0.0.1:8086 or http://wallproxy to access the Web configuration interface

## Step 2: Run the client ##
  1. Run a local file folder under `wwqgtxx-wallproxy.bat`, The following diagram can be displayed after you complete the automatic update
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image011.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image011.png)
> > Double-click the tray icon, the console window
  1. Tray left-menu is used to configure the proxy, the right-click menu configuration program.
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/mage013.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/mage013.png)
    1. Direct connection: force the browser does not use a proxy;
    1. GAE Proxy: force the browser to use 127.0.0.1:8087 as a proxy (except some of the google site, most of the sites are gone GAE);
    1. Intelligent Agents: force the browser to use 127.0.0.1:8086 as a proxy to determine whether you need to go GAE wallproxy smart, direct connection fails, GAE can automatically change to go;
    1. Auto Agent: PAC determine whether you need to go through by the browser GAE, small performance loss compared with intelligent agents, but can not do the change to go directly connected fails GAE;
    1. Disable the switch: to force IE does not use a proxy; choose to modify the IE proxy in each run `WallProxy.exe` will for the selected item 4 above, and select "Disable switch" after the next run will not do the IE proxy any modification. **Use `SwitchySharp / AutoProxy` browser extensions Management Agent user, select this**.
  1. If you need custom menu, you can choose to set up a proxy menu item:
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image014.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image014.png)
> > Check the "exit recovery agentless" exit `WallProxy.exe` IE proxy is amended as agentless, so as not to affect the normal use; checked "Disable Proxy Switcher effect similar to" disable switch "menu.
> > If you use a dial-up mode as shown in the figure, the connection name filled in on the map "connection name", for example, the following figure "Connection broadband connection, broadband connection can fill.
> > > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image015.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image015.jpg)
  1. Open the browser input: http://www.facebook.com and successful visit.

> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/mage016.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/mage016.jpg)
  1. Custom proxy rules, visit http://wallproxy/ or http://127.0.0.1:8086/, and then click the "Custom Rules, the input saved can go GAE rules:
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image017.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image017.jpg)

## Appendix A: the browser easy setup method ##
  1. Direct download [wwqgtxx-wallproxy-Release-withFirefox version](https://code.google.com/p/wwqgtxx-goagent/wiki/download_en) open without configuration, can be used directly

## Appendix II: `Firefox + WallProxy` ##
  1. System Agent
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image019.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image019.jpg)
  1. RootCerts
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image020.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image020.jpg)
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image021.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image021.png)
  1. Check whether the correct import (optional), the same amount of time, not guide the wrong:
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image022.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image022.jpg)
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image023.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image023.jpg)

## Appendix III: to match `the Chrome + SwitchySharp` use ##

> [.md](.md) **GUI Left menu, select "Disable switch", press the map import configuration, after "direct connection", GAE agent "," intelligent agent "," Automatic Proxy "same effect` WallProxy.exe `.
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image024.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image024.jpg)
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image025.png](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image025.png)**

## Appendix IV: with the `Firefox + FoxyProxy` use ##

> [.md](.md) **GUI left-menu select "Disable switch**, as shown sequentially adding" GAE proxy 127.0.0.1:8087 "intelligent agent" 127.0.0.1:8086, "Automatic Proxy" [.0.1:8087 / proxy.pac](http://127.0).
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image026.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image026.jpg)
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image027.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image027.jpg)
> > ![https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image028.jpg](https://wwqgtxx-goagent.googlecode.com/git/wiki/wallproxy.files/image028.jpg)

## Appendix V: to match the `Firefox + AutoProxy` use ##

> [.md](.md) 