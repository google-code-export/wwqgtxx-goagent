# -*- coding: utf-8 -*-
# 是否使用ini作为配置文件，0不使用
ini_config = 1359277138
# 监听ip
listen_ip = '127.0.0.1'
# 监听端口
listen_port = 8086
# 是否使用通配符证书
cert_wildcard = 1
# 更新PAC时也许还没联网，等待tasks_delay秒后才开始更新
tasks_delay = 0
# WEB界面是否对本机也要求认证
web_authlocal = 0
# 登录WEB界面的用户名
web_username = 'admin'
# 登录WEB界面的密码
web_password = 'admin'
# 全局代理
global_proxy = None
# URLFetch参数
fetch_keepalive = 1
check_update = 0

def config():
    Forward, set_dns, set_resolve, set_hosts, check_auth, redirect_https = import_from('util')
    FORWARD = Forward()
    set_dns('8.8.8.8')
    set_resolve('talk.google.com talkx.l.google.com .youtube.com')
    google_sites = ('.appspot.com', '.google.com', '.google.com.hk', '.googlecode.com', '.googleusercontent.com', '.googlegroups.com', '.google-analytics.com', '.gstatic.com', '.googleapis.com', '.blogger.com', '.ggpht.com')
    google_hosts = 'www.google.com www.google.com.hk mail.google.com www.google-analytics.com 74.125.128.59 74.125.128.54 74.125.128.102 74.125.128.101 74.125.128.83 74.125.128.17 74.125.128.51 74.125.128.35 74.125.128.45 74.125.128.106 74.125.128.50 74.125.128.65 74.125.128.104 74.125.128.138 74.125.128.96'
    set_hosts(google_sites, google_hosts)
    set_hosts('www.youtube.com upload.youtube.com', google_hosts)

    from plugins import paas; paas = install('paas', paas)
    GAE = paas.GAE(appids=['freegoagent001', 'freegoagent002', 'freegoagent003', 'freegoagent004', 'freegoagent005', 'freegoagent006', 'freegoagent007', 'freegoagent008', 'freegoagent009', 'freegoagent010', 'freegoagent011', 'freegoagent012', 'freegoagent013', 'freegoagent014', 'freegoagent015', 'freegoagent016', 'freegoagent017', 'freegoagent018', 'freegoagent019', 'freegoagent020', 'freegoagent021', 'freegoagent022', 'freegoagent023', 'freegoagent024', 'freegoagent025', 'freegoagent026', 'freegoagent027', 'freegoagent028', 'freegoagent029', 'freegoagent030', 'freegoagent031', 'freegoagent032', 'freegoagent033', 'freegoagent034', 'freegoagent035', 'freegoagent036', 'freegoagent037', 'freegoagent038', 'freegoagent039', 'freegoagent040', 'freegoagent041', 'freegoagent042', 'freegoagent043', 'freegoagent044', 'freegoagent045', 'freegoagent046', 'freegoagent047', 'freegoagent048', 'freegoagent049', 'freegoagent050', 'freegoagent051', 'freegoagent052', 'freegoagent053', 'freegoagent054', 'freegoagent055', 'freegoagent056', 'freegoagent057', 'freegoagent058', 'freegoagent059', 'freegoagent060', 'freegoagent061', 'freegoagent062', 'freegoagent063', 'freegoagent064', 'freegoagent065', 'freegoagent066', 'freegoagent067', 'freegoagent068', 'freegoagent069', 'freegoagent070', 'freegoagent071', 'freegoagent072', 'freegoagent073', 'freegoagent074', 'freegoagent075', 'freegoagent076', 'freegoagent077', 'freegoagent078', 'freegoagent079', 'freegoagent080', 'freegoagent081', 'freegoagent082', 'freegoagent083', 'freegoagent084', 'freegoagent085', 'freegoagent086', 'freegoagent087', 'freegoagent088', 'freegoagent089', 'freegoagent090', 'freegoagent091', 'freegoagent092', 'freegoagent093', 'freegoagent094', 'freegoagent095', 'freegoagent096', 'freegoagent097', 'freegoagent098', 'freegoagent099', 'freegoagent100', 'freegoagent101', 'freegoagent102', 'freegoagent103', 'freegoagent104', 'freegoagent105', 'freegoagent106', 'freegoagent107', 'freegoagent108', 'freegoagent109', 'freegoagent110', 'freegoagent121', 'freegoagent122', 'freegoagent124', 'freegoagent125', 'freegoagent126', 'freegoagent127', 'freegoagent128', 'freegoagent129', 'freegoagent130', 'freegoagent131', 'freegoagent132', 'freegoagent133', 'freegoagent134', 'freegoagent135', 'freegoagent136', 'freegoagent137', 'freegoagent138', 'freegoagent139', 'freegoagent140', 'freegoagent141', 'freegoagent142', 'freegoagent143', 'freegoagent144', 'freegoagent145', 'freegoagent146', 'freegoagent147', 'freegoagent148', 'freegoagent149', 'freegoagent150', 'freegoagent151', 'freegoagent152', 'freegoagent153', 'freegoagent154', 'freegoagent155', 'freegoagent156', 'freegoagent157', 'freegoagent158', 'freegoagent159', 'freegoagent160', 'freegoagent161', 'freegoagent162', 'freegoagent163', 'freegoagent164', 'freegoagent165', 'freegoagent166', 'freegoagent167', 'freegoagent168', 'freegoagent169', 'freegoagent170', 'fgabootstrap001', 'fgabootstrap002', 'fgabootstrap003', 'fgabootstrap004', 'fgabootstrap005', 'fgabootstrap006', 'fgabootstrap007', 'fgabootstrap008', 'fgabootstrap009', 'fgabootstrap010', 'fgaupdate001', 'fgaupdate002', 'fgaupdate003', 'fgaupdate004', 'fgaupdate005', 'fgaupdate006', 'fgaupdate007', 'fgaupdate008', 'fgaupdate009', 'fgaupdate010', 'gonggongid01', 'gonggongid02', 'gonggongid03', 'gonggongid04', 'gonggongid05', 'gonggongid06', 'gonggongid07', 'gonggongid08', 'gonggongid09', 'gonggongid10', 'gonggongid11', 'gonggongid12', 'gonggongid13', 'gonggongid14', 'gonggongid15', 'gonggongid16', 'gonggongid17', 'gonggongid18', 'gonggongid19', 'gonggongid20'], listen='8087', password='wwqgtxx-wallproxy2.1-0.10', path='/fetch.py', scheme='https', hosts=google_hosts, maxsize=500000, waitsize=100000, max_threads=3, fetch_mode=1)

    PacFile, RuleList, HostList = import_from('pac')
    forcehttps_sites = RuleList('http://*.appspot.com/ \n http://*.google.com/ \n http://*.google.com.hk/ \n http://*.googlecode.com/ \n http://*.googleusercontent.com/ \n http://*.blogger.com/ \n @@http://books.google.com/ \n @@http://translate.google.com/ \n @@http://scholar.google.com/ \n @@http://feedproxy.google.com/ \n @@http://*.pack.google.com/ \n @@http://www.google.com*/imgres? \n @@http://www.google.com*/translate_t? \n @@http://www.google.com/analytics/ \n @@http://wiki.*.googlecode.com/ \n @@http:/// \n @@http://website.*.googlecode.com/ \n @@http://www.google.com*/custom? \n @@http://www.google.com/dl/')
    autorange_rules = RuleList('||c.youtube.com \n ||c.docs.google.com \n ||googlevideo.com \n http*://av.vimeo.com/ \n http*://smile-*.nicovideo.jp/ \n http*://video.*.fbcdn.net/ \n http*://s*.last.fm/ \n http*://x*.last.fm/ \n /^https?:\\/\\/[^\\/]+\\/[^?]+\\.(?:f4v|flv|hlv|m4v|mp4|mp3|ogg|avi|exe)(?:$|\\?)/ \n http*://*.googleusercontent.com/videoplayback?')
    _GAE = GAE; GAE = lambda req: _GAE(req, autorange_rules.match(req.url, req.proxy_host[0]))
    import re; useragent_match = re.compile('(?i)mobile').search
    useragent_rules = RuleList('||twitter.com')
    withgae_sites = RuleList('||c.docs.google.com \n ||translate.google.com \n ||play.google.com \n http*://books.google.com/books?id= \n http*://*.googleusercontent.com/videoplayback?')
    notruehttps_sites = HostList('.docs.google.com translate.google.com play.google.com books.google.com')
    truehttps_sites = HostList('.appspot.com .google.com .google.com.hk .googlecode.com .googleusercontent.com .googlegroups.com .google-analytics.com .gstatic.com .googleapis.com .blogger.com .ggpht.com')
    crlf_rules = RuleList('/^https?:\\/\\/[^\\/]+\\.c\\.youtube\\.com\\/liveplay\\?/ \n /^https?:\\/\\/upload\\.youtube\\.com\\// \n /^https?:\\/\\/www\\.youtube\\.com\\/upload\\//')
    hosts_rules = RuleList(' \n ||appspot.com \n ||google.com \n ||google.com.hk \n ||googlecode.com \n ||googleusercontent.com \n ||googlegroups.com \n ||google-analytics.com \n ||gstatic.com \n ||googleapis.com \n ||blogger.com \n ||ggpht.com')
    FORWARD.http_failed_handler = GAE

    rulelist = (
        (RuleList(['https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt', 'userlist.ini']), GAE),
    )
    httpslist = (
        (rulelist[0][0], None),
    )
    unparse_netloc = import_from(install('utils', lambda:globals().update(vars(utils))))

    def find_gae_handler(req):
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
            if withgae_sites.match(url, host):
                return GAE
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
            if crlf_rules.match(url, host):
                req.crlf = 1
                return FORWARD
            if not needhttps and hosts_rules.match(url, host):
                return FORWARD
            return GAE
        if notruehttps_sites.match(host): return
        if truehttps_sites.match(host): return FORWARD
    paas.data['GAE_server'].find_handler = find_gae_handler

    def find_proxy_handler(req):
        proxy_type = req.proxy_type
        host, port = req.proxy_host
        if proxy_type.endswith('http'):
            url = req.url
            if useragent_match(req.headers.get('User-Agent','')) and useragent_rules.match(url, host):
                req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
            if withgae_sites.match(url, host):
                return GAE
            needhttps = req.scheme == 'http' and forcehttps_sites.match(url, host) and req.content_length == 0
            if needhttps and getattr(req, '_r', '') != url:
                req._r = url
                return redirect_https
            if crlf_rules.match(url, host):
                req.crlf = 1
                return FORWARD
            if not needhttps and hosts_rules.match(url, host):
                return FORWARD
            for rule,target in rulelist:
                if rule.match(url, host):
                    return target
            return FORWARD
        if notruehttps_sites.match(host): return
        if truehttps_sites.match(host): return FORWARD
        elif proxy_type.endswith('https'):
            url = 'https://%s/' % unparse_netloc((host, port), 443)
            for rule,target in httpslist:
                if rule.match(url, host):
                    return target
            return FORWARD
    return find_proxy_handler
