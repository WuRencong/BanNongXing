//超过一定高度给导航栏添加类样式
var nav=$("header"); //得到导航对象
var win=$(window); //得到窗口对象
var sc=$(document);//得到document文档对象。
win.scroll(function(){
    if(sc.scrollTop()>=0){
        nav.addClass("on");
    }
    else{
        nav.removeClass("on");
    }
});
//移动端展开nav
$('#navToggle').on('click',function(){
    $('.m_nav').addClass('open');
});
//移动端关闭nav
$('.m_nav .top .closed').on('click',function(){
    $('.m_nav').removeClass('open');
});
//二级导航  移动端
$(".m_nav .ul li").click(function() {
    $(this).children("div.dropdown_menu").slideToggle('slow')
    $(this).siblings('li').children('.dropdown_menu').slideUp('slow');
});
//快速收藏网站网址
function AddFavorite(title,url){
    try{
        window.external.addFavorite(url,title);
    }
    catch(e){
        try{
            window.sidebar.addPanel(title,url,"");
        }
        catch(e){
            alert("抱歉，您所使用的浏览器无法完成此操作。\n\n请使用快捷键Ctrl+D进行添加！");
        }
    }
}
//将当前网页设为首页 <a οnclick="setHome(this,window.location)">设为首页</a>
function setHome(obj, vrl){
    try{
        obj.style.behavior='url(#default#homepage)';
        obj.setHomePage(vrl);
    }
    catch(e){
        if(window.netscape) {
            try {
                netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
            }
            catch (e) {
                alert("此操作被浏览器拒绝！\n请在浏览器地址栏输入“about:config”并回车\n然后将 [signed.applets.codebase_principal_support]的值设置为'true',双击即可。");
            }
            var prefs = Components.classes['@mozilla.org/preferences-service;1'].getService(Components.interfaces.nsIPrefBranch);
            prefs.setCharPref('browser.startup.homepage',vrl);
        }
    }
}