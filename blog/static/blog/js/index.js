$(document).ready(function () {
	toggleForm('replyToggle', 'replyForm');
	toggleForm('editToggle', 'editForm');
})

function toggleForm (anchorClass, formClass) {
	$('.'+anchorClass).click(function (e) {
		e.preventDefault();
		var form = $(this).siblings('.'+formClass)[0]
		$(form).slideToggle();
	})
}