$(function() {
 $('.humberger-btn').click(function() {
	 $(this).toggleClass('active');

	 if($(this).hasClass('active')) {
		 $('#menu').addClass('active');
	 }else {
		 $('#menu').removeClass('active');
	 }
 });
});
$(function() {
	$('#menu li').hover(
		function() {
			$(this).children('ul').show(200);
		},
		function() {
			$(this).children('ul').hide(200);
		}
	);
})