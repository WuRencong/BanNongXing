/* 获取浏览器对象 */
var userAgent = navigator.userAgent.toLowerCase(), s, o = {};

/* 获得浏览器的名称及版本信息 */
var browser = {
    version:(userAgent.match(/(?:firefox|opera|safari|chrome|msie)[\/: ]([\d.]+)/))[1],
    safari:/version.+safari/.test(userAgent),
    chrome:/chrome/.test(userAgent),
    firefox:/firefox/.test(userAgent),
    ie:/msie/.test(userAgent),
    opera: /opera/.test(userAgent )
};

/* 判断是否为 Safari 浏览器 */
if (browser.safari) {
    // alert("您使用的是 Safari 浏览器")
}

 /* 判断是否为 Firefox 浏览器 */
if (browser.firefox) {
    // alert("您使用的是 Firefox 浏览器")
}

/* 判断是否为 Chrome 浏览器 */
if (browser.chrome) {
    // alert("您使用的是 Chrome 浏览器或 Edge 浏览器")
}

/* 判断是否为 Opera 浏览器 */
if (browser.opera) {
    // alert("您使用的是 Opera 浏览器")
}

/* 判断是否为老到掉牙的 IE 浏览器 */
if (browser.ie) {
    alert("您使用的是 IE 浏览器");
    if (browser.version < 12){
        alert("您使用的是 IE 12 以下版本的 IE 浏览器，本网站并不对 IE 12 以下版本支持正常访问服务，" +
            "\n请使用现代浏览器访问网站")
    }
}