// 通过post提交方式将form表单中的数据序列化后传递到后台
// 调查信息报文前台传值
// 前台传值方法
function AjaxForm() {
       $.ajax({
           type: "post", // 以post方式发起请求
           url: "/yourUrl", // 你的请求链接
           data: $("#myForm").serialize(), // 对id为myForm的表单数据进行序列化并传递到后台
           success: function(data){
               // data为返回值
               // 成功后的回调方法
           }
       })
   }