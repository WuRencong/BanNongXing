// 新闻栏动态样式切换器
$(".news_box").mouseover(function(){
	$(this).addClass("news_box_action");
});
$(".news_box").mouseout(function(){
	if($(this).val() == "")
	$(this).removeClass("news_box_action");
});
//新闻栏鼠标事件着重
$('.on_list').mousemove(function(){
	$(this).children('.on_ico').css("color", "rgba(255,0,4,1.00)");
});
$('.on_list').mouseout(function(){
	$(this).children('.on_ico').css("color", "rgba(255,0,4,0.00)");
});
//轮播图样式定义
$(window).resize(function() {//浏览器窗口大小变化时
	var W_img = $('.banner').width();
	$('.banner_img').css('width',W_img);
	var W_button = $('.b_list ul li').width();
	var button_x = (W_img * 0.5 - (8.1 * W_button));
	$('.b_list ul').css('left', button_x);
});
var W_img = $('.banner').width();
$('.banner_img').css('width',W_img);
var button_x = (W_img * 0.5);
$('.b_list ul').css('left', button_x);
var H_box = $('.text-center').height();
$('.banner').css('height', H_box);	//将轮播图高度与侧边栏齐平
var H_img = $('.banner').height();
$('.banner_img').css('height', H_img);
var H_button = $('.b_list ul li').height();
var W_button = $('.b_list ul li').width();
var button_y = H_img - (2.5 * H_button);
$('.b_list ul').css('top', button_y);
var button_x = (W_img * 0.5 - (8.1 * W_button));
$('.b_list ul').css('left', button_x);

//轮播图的代码
var $li = $(".b_list ul li");//获取.b_list里面的所有li，放到$li这个变量里面
var len = $li.length-1;
var _index = 0;//li的索引
var $img = $(".b_main .b_m_pic li");//同上
var $btn = $(".b_btn div");

var timer = null;

//  alert(typeof timer); timer是一个对象

$li.hover(function(){
	$(this).addClass("l_hover");//指向li添加样式
},function(){
	$(this).removeClass("l_hover");//指向li删除样式
});

//点击事件
$li.click(function(){
	_index = $(this).index();
	//获取li的下标，改变样式
	//$li.eq(_index).addClass("l_click").siblings().removeClass("l_click");
	//获取图片的下标，实现淡入淡出
	//$img.eq(_index).fadeIn().siblings().fadeOut();
	play();
});

//封装函数
function play(){
	//获取li的下标，改变样式
	$li.eq(_index).addClass("l_click").siblings().removeClass("l_click");
	//获取图片的下标，实现淡入淡出
	$img.eq(_index).fadeIn().siblings().fadeOut();
}
//定时轮播
function auto(){
	//把定时器放进timer这个对象里面
	timer = setInterval(function(){
		_index++;
		if(_index > len){
			_index = 0;
		}
		play();
	},2000);
}
auto();

//当鼠标移上d_main的时候停止轮播
$(".b_main").hover(function(){
	clearInterval(timer);
},function(){
	//移开重新调用播放
	auto();
});