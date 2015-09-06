$(function() {
	var	$tabsLeft = $('.left_new_house'),
		$tabsRight = $('.right_old_house'),
		$searchWords = $('#searchWords'),
		$searchButton = $('.search_button');

	$tabsLeft.on('click',function () {
		$tabsRight.removeClass('hover');
		$tabsLeft.addClass('hover');
	});
	$tabsRight.on('click',function () {
		$tabsLeft.removeClass('hover');
		$tabsRight.addClass('hover');
	});
	$searchButton.on('click', function() {
		search_val();
	});
	$searchWords.keypress(function(e) {
		if (e.keyCode == 13) {
			search_val();
		};
	});

});
function search_val() {
	var	$searchWords = $('#searchWords'),
	    sea_val = $searchWords.val(),
		data_object = {
			'sea_val':sea_val
		},
		data_json = JSON.stringify(data_object);
	$.ajax({
		type:'post',
		url:'/search',
		data:{
			data_json:data_json
		}
	})
	.done(function(returnData) {
		alert('it works!');
		console.log(returnData);
	})
	.fail(function(returnData) {
		alert('so sorry!');
		console.log(returnData);
	});
};
