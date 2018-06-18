jQuery(function($) {
	$('.vine').jscroll({
		loadingHtml: '<img src="' + settings.STATIC + 'images/loading.gif" alt="Loading" />',
		padding: 100,
		pagingSelector: '.pagination',
		nextSelector: 'a.next_page:last',
		contentSelector: '.item,.pagination'
});
});