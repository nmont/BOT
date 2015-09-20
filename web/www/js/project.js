// project
(function ($) {
	// ui-form-adv.html
	$('.datepicker-adv-doc-1').datepicker();

	$('.datepicker-adv-doc-2').datepicker({
		format: "dd-mmm-yyyy",
		selectMonths: true,
		selectYears: 30
	});

	// ui-modal.html
	$('#toast-1').on('click', function () {
		$('body').toast({
			content: 'Simple toast with some text'
		});
	});

	$('#toast-2').on('click', function () {
		$('body').toast({
			content: '<a data-dismiss="toast">Dismiss</a><div class="toast-text">Simple toast with some text and a simple <a href="javascript:void(0)">link</a>.</div>'
		});
	});

	// ui-progress.html
	$('.finish-loading').on('click', function(e) {
		e.stopPropagation();
		$($(this).attr('data-target')).addClass('el-loading-done');
	});

	$('#el-loading-tile-wrap .tile-active-show').each(function (index) {
		var $this = $(this);
		var timer;

		$this.on('hide.bs.tile', function(e) {
			clearTimeout(timer);
		});

		$this.on('show.bs.tile', function(e) {
			if (!$('.el-loading', $this).hasClass('el-loading-done')) {
				timer = setTimeout(function() {
					$('.el-loading', $this).addClass('el-loading-done');
					$this.prepend('<div class="tile-sub"><p>Additional information<br><small>Aliquam in pharetra leo. In congue, massa sed elementum dictum, justo quam efficitur risus, in posuere mi orci ultrices diam.</small></p></div>');
				}, 6000);
			}
		});
	});

	// B.O.T. Cards
	function updateCards() {
		$.getJSON('/data', function(data) {
			var cardElements = cardAPI.jsonToCards(data);
			_.forEach(cardElements, function (value, index) {
				console.log(index,value);
				$('#cards').delay(500 * index).append(value);
			});
		});
	}
	window.updateCards = updateCards;

	function clearCards() {
		var cards = $('#cards').children();
		cards.each(function (index) {
			$(this).delay(100 * index).animate({left: window.innerWidth + 20, opacity: 0}, 'slow', function () {
				$(this).remove();
			});
		});
	}
	window.clearCards = clearCards;

	$('#update-cards').on('click', function () {
		updateCards();
		$('body').toast({
			content: 'Cards updated from the saved file'
		});
	});

	$('#clear-cards').on('click', function () {
		clearCards();
		$('body').toast({
			content: 'Cards cleared'
		});
	});

})(jQuery);
