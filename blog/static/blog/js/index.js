$(document).ready(function () {
	toggleForm('replyToggle', 'replyForm');
	toggleForm('editToggle', 'editForm');
	$('.addLorem').click(function (e) {
		e.preventDefault();
		$('textarea').data('lorem', '1p');
		$('textarea').lorem();
	})
})

function toggleForm (anchorClass, formClass) {
	$('.'+anchorClass).click(function (e) {
		e.preventDefault();
		var form = $(this).siblings('.'+formClass)[0]
		$(form).slideToggle();
	})
}