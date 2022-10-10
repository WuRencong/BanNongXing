// 登陆报文前台传值
function AjaxLand() {
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"username" : "和蔼的撒旦",
			"password" : "baba2020"
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}

// 注册报文前台传值
function AjaxRegister() {
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"username" : "和蔼的撒旦",
			"password" : "baba2020",
			"emailip" : "2665478433@qq.com"
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}

// 找回账号报文前台传值
function AjaxFind() {
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"emailip" : "2665478433@qq.com"
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}