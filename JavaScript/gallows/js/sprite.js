const createSprite = selector => {

    const $el = $(selector);

    const frames = [
		'frame1', 'frame2', 'frame3', 'frame4', 'frame5',
		'frame6', 'frame7', 'frame8', 'frame9'
	];

	let current = 0;
	let last = frames.length - 1;


	$el.addClass(frames[current]);

    const moveFrame = (from, to) => {

		$el.removeClass(from)
			.addClass(to);
	};

    const hasNext = () => {

		return current + 1 <= last;
	};

    const nextFrame = () => {

		if (hasNext())
			moveFrame(frames[current], frames[++current]);
	};

    const reset = () => {

		moveFrame(frames[current], frames[0]);

		current = 0;
	};

    const isFinished = () => {

		return !hasNext();
	};

	return {
		nextFrame,
		reset,
		isFinished
	};
};