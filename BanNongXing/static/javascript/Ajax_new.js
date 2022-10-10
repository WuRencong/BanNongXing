// 切换页面报文前台传值
function AjaxTogglePages() {
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"page" : "2",    // 注意，这里是字符串格式数据，如果里面是next表示下一页，prev表示上一页，fast表示首页，last表示尾页
			"pageSize" : 2
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}

// 提交新闻ID报文前台传值
function AjaxSubmit(){
	$.ajax({
		type: "post", // 以post方式发起请求
		url: "/yourUrl", // 你的请求链接
		data: { // 提交数据
			"newsnum" : 2
		},
		success: function(data) {
			// data为返回值
			// 成功后的回调方法
		}
	})
}