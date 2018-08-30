// jQuery

// You can also user:
//
// $(function () {
// 
// });
//
// Works the same as below

$(document).ready(function () {

	updateScores();
	startClock();
	restartGame();
	borderInit();

});

// Word and letter counters update function wrapper
function updateScores() {

	// Textarea user input event to update word and letter counters
	// .on("input") event
	$("#words_input").on("input", function () {

		// .text() returns text inside the tag
		// .match(" ") matches regex expression
		// .length length of array returned by match()
		if ($("#words_input").val().match(/\S+/g) === null) {
			var count = 0;
		}
		else {
			var count = $("#words_input").val().match(/\S+/g).length;
		}

		$("#words_counter").text(count);
		$("#letter_counter").text($("#words_input").val().length);

	});
}

// User on focus event function wrapper
function startClock() {

	// Textarea user focus event to start clock
	// .one("focus") event executes only once
	$("#words_input").one("focus", function () {

		// Seconds interval
		var interval_id = setInterval(function () {

			var seconds = $("#seconds_goal").text();

			$("#seconds_goal").text(seconds -= 1);

			// Lock textarea and stop interval
			if (seconds < 1) {

				$("#words_input").attr("disabled", true);

				$("#words_input").toggleClass("gray_bg");

				clearInterval(interval_id);
			}

		}, 1000);

	});
}

// Restart game function wrapper
function restartGame() {

	// Restart game button event
	$("#restart_game").on("click", function () {

		var seconds = $("#seconds_goal").text();

		if (seconds === "0") {

			var field = $("#words_input");

			// Reset textarea
			field.attr("disabled", false);
			field.val("");

			// Reset timer
			$("#seconds_goal").text("20");

			// Reset word/letter counters
			$("#words_counter").text("0");
			$("#letter_counter").text("0");

			field.toggleClass("gray_bg");

			field.removeClass("border_red");
			field.removeClass("border_green");

			startClock();
		}

	});

}

// Function wrapper that checks if text written equals to target text and
// changes textarea border
function borderInit() {

	$("#words_input").on("input", function () {

		var field = $("#words_input");

		var target_text = $("#phrase").text();
		var written_text = $("#words_input").val();

		var comparable = target_text.substr(0, written_text.length);

		if (written_text === comparable) {

			field.addClass("border_green");
			field.removeClass("border_red");

		} else {

			field.addClass("border_red");
			field.removeClass("border_green");

		}

	});
}
