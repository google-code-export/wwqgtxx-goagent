var Z7c=Ze;function Z8c(){Z7c=Zc}function Z9c(a){if(a!=Zd){for(var b=a.nextSibling;b&&"LI"!=b.tagName&&"UL"!=b.tagName;)b=b.nextSibling;if(!b||"LI"==b.tagName)for(b=a.firstChild;b&&"UL"!=b.tagName;)b=b.nextSibling;return b}}function Z$c(a){a.stopPropagation();if(!Z7c){a=a.target;var b=Z9c(a);b&&("treeopen"==a.className?(a.className="",b.className=""):(a.className="treeopen",b.className="treeleafcontainer"))}}var Zad=Zb;
function Zbd(a){if(a)for(a=a.firstChild;a;){if("LI"==a.tagName){for(var b=a.firstChild;b&&"A"!=b.tagName;)b=b.nextSibling;if(b&&"A"==b.tagName&&(ZE(b,"click",Z8c),document.location.href.split("?")[0]==b.href||document.location.href.split("#")[0]==b.href))Zad=b;(b=Z9c(a))?(ZE(a,"click",Z$c),Zbd(b)):a.className="treeleaf"}a=a.nextSibling}}Zbd(Z9c(Zx("sidebarcontainer")));
if(Zad){Zad.className="currentpagelink";for(var Zcd=Zad.parentNode.parentNode;Zcd&&"UL"==Zcd.tagName;){Zcd.className="treeleafcontainer";for(var Z6=Zcd.previousSibling;Z6&&"LI"!=Z6.tagName;)Z6=Z6.previousSibling;Z6&&"LI"==Z6.tagName&&(Z6.className="treeopen");Zcd=Zcd.parentNode}var Zdd=Zad.parentNode;if(!Zdd.className){var Zed=Z9c(Zdd);Zed&&(Zdd.className="treeopen",Zed.className="treeleafcontainer")}}
_DW_toggleSidebar=function(a){a=Zjc(a);CS_env.token&&ZT(CS_env.projectHomeUrl+"/w/setSidebarPref.do",Zca,{expanded:a?1:0})};function Zfd(a){a=ZO(a);var b=Zx("wikimaincol");b.innerHTML=a.preview_html;prettyPrint();gapi.plusone.go(b)}_DW_syncPreview=function(a){ZT(CS_env.projectHomeUrl+"/w/syncWikiPreviewJSON",Zfd,{content:a})};
