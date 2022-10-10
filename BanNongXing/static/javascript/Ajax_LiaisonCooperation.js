// 联系信息报文前台传值
function AjaxTogglePages() {
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"name" : "川建国",
			"address" : "美利坚合众国北卡罗莱纳州华盛顿特区白宫",
			"phone" : "33252525",
			"classification" : "这是个字符串",
			"describe" : "这也是个字符串"
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}