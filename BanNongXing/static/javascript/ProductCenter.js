//九宫格动态样式切换
$('.LN-container').mouseover(function(){
//	$(this).parent().addClass('LN_mouse_on')
	$(this).addClass('LN_mouse_on')
});
$('.LN-container').mouseout(function(){
//	$(this).parent().removeClass('LN_mouse_on')
	$(this).removeClass('LN_mouse_on')
});