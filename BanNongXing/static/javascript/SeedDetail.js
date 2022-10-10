let ele = document.querySelector('.scope_img')
let gray = document.querySelector('.gray')
let elephp = document.querySelector('.scope_img_wrap>img')
let scope = document.querySelectorAll('.scope')
let close = document.querySelector('.close')

for (let i = 0; i < scope.length; i++) {
  scope[i].addEventListener('click', function (e) {
    let src = e.target.attributes.src.value
    elephp.src = src
    $(ele).slideDown();
    $(gray).slideDown();
  })
}

gray.addEventListener('click', function () {
  $(ele).slideUp();
  $(this).slideUp();
})

close.addEventListener('click', function () {
  $(ele).slideUp();
  $(gray).slideUp();
})