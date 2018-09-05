// Returns a random number between [min, max] both included
function RandInt(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Gets a random phrase from server
function phraseRandom() {

	var time = $("#seconds_goal").text();

	if (time !== "0") {

		$.get("http://localhost:3000/frases", function (data, code, request) {

			var r = RandInt(0, data.length);

			$("#phrase").text(data[r].texto);
			$("#seconds_goal").text(data[r].tempo);

			updatePhraseLength();

		});
	}


}