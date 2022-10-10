// 表单框背景水纹涟漪效果控制代码(太卡了)
// $("body").ripples({
// 	resolution: 400,
// 	dropRadius: 20,
// 	perturbance: 0.005,
// });

// form_text动态样式控制
$(".my_form_text input").on("focus",function(){
	$(this).addClass("form_text_action");
});
$(".my_form_text input").on("blur",function(){
	if($(this).val() == "")
		$(this).removeClass("form_text_action");
});

// $(".my_form_text input").mouseover(function(){
// 	$(this).addClass("form_text_mouse_action");
// 	$(this).siblings().addClass("form_text_mouse_action");	//选择所有兄弟元素
// });
// $(".my_form_text input").mouseout(function(){
// 	if($(this).val() == "")
// 		$(this).removeClass("form_text_mouse_action");
// 		$(this).siblings().removeClass("form_text_mouse_action");
// });

// form_reset控制样式
$("#form_reset").click(function(){
	$(".my_form_text input").removeClass("form_text_action");
});

$('#form_submit').click(function () {
	alert('表单提交成功')
});