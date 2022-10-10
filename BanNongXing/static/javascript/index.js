//banner 响应JS的的的代码（实现图片大小变换，自动切换，淡入淡出等效果）
$('.index_banner').slick({
    autoplay: true, 
    arrows: false,
    dots:false,
    infinite: true,
    speed: 500,
    autoplaySpeed: 5000,
    pauseOnHover: false,
    fade: true,
    responsive: [
      {
        breakpoint: 992,
        settings: {
          dots: true
        }
      }
    ]
});

// 这段代码是控制轮播图文本动画，按钮动画与响应变换的JQ
////注：slick-current属性是slick框架的一个内含样式
$('.index_banner').init(function(slick){
    $('.index_banner .item.slick-current').addClass('active').siblings().removeClass('active')
})
//// 这段是响应由翻页按钮造成的页面变化样式
$('.index_banner').on('afterChange',function(slick,currentSlide){
    $('.index_banner .item.slick-current').addClass('active').siblings().removeClass('active');
    var _index = $('.index_banner').slick('slickCurrentSlide')
    $('.section1 .number span').eq(_index).addClass('active').siblings().removeClass('active')
})
//// 这段是控制页面按钮样式变换的
$('.section1 .number span').click(function(){
    var _index = $(this).index();
    $('.index_banner').slick('slickGoTo',_index);
    $(this).addClass("active").siblings().removeClass("active")
});
//// 下面这两段是控制前后翻页按钮进行翻页的
$('.section1 .prev').click(function(){
  $('.index_banner').slick('slickPrev')
})
$('.section1 .next').click(function(){
  $('.index_banner').slick('slickNext');
});


//全屏滚动 （是实现按块滚动的效果的代码）
$('#index_main').fullpage({
	'navigation': true,
	slidesNavigation: true,
	controlArrows: false,
	continuousHorizontal:true,
	scrollingSpeed:1000,
	showActiveTooltip :true, 
	anchors: ['hero', 'one', 'two', 'three'],
	loopHorizontal: true,
	afterLoad: function(anchorLink, index){
		if(index == 1){
			$('header').removeClass('on');
		}
		if(index == 2){
			$('header').addClass('on');
			$('.section2 h3').addClass('animated fadeInUp').css('animation-delay', '.1s');
		}
		if(index == 3){
			$('header').addClass('on');
			$('.section3 h3').addClass('animated fadeInUp').css('animation-delay', '.1s');
		}
		if(index == 4){
			$('header').addClass('on');
			$('.section4 h3').addClass('animated fadeInUp').css('animation-delay', '.1s');
		}
	},
	onLeave: function(index, direction){
	}
})