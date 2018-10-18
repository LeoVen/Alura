var createSprite = function(selector) {

	var $el = $(selector);

	var frames = [
		'frame1', 'frame2', 'frame3', 'frame4', 'frame5',
		'frame6', 'frame7', 'frame8', 'frame9'
	];

	var current = 0;
	var last = frames.length - 1;


	$el.addClass(frames[current]);

	var moveFrame = function(from, to) {

		$el.removeClass(from)
			.addClass(to);
	};

	var hasNext = function() {

		return current + 1 <= last;
	};

	var nextFrame = function() {

		if (hasNext()) moveFrame(frames[current], frames[++current]);

	};

	var reset = function() {

		moveFrame(frames[current], frames[0]);

		current = 0;
	};

	var isFinished = function() {

		return !hasNext();
	};

	return {
		nextFrame: nextFrame,
		reset: reset,
		isFinished: isFinished
	};
};