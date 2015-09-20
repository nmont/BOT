/*
 * loadTemplate returns a lodash template function
 * from the given file.
 */

(function ($) {
	'use strict';

	function loadTemplate(file) {
		var temp = {};
		$.ajax({
			url: file,
			method: 'GET',
			async: false,
			dataType: 'html',
			success: function(res) {
				temp = res;
			}
		});
		return _.template(temp);
	}
	_.mixin({ 'loadTemplate': loadTemplate });

})(jQuery);
