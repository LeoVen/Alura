// jQuery

// Score related functions
// Responsible for adding a register to the scoreboard
function scoreAdd() {

	var table = $("#scoreboard").find("table").find("tbody");

	var words = $("#words_counter").text();
	var letters = $("#letter_counter").text();

	var user = prompt("What is your name?");

	var row = scoreBuilder(user, words, letters);

	// Adding event
	row.find(".remove_score").on("click", scoreRemove);

	table.prepend(row);

	$("#scoreboard").slideDown(500);

	scoreScroll();
}

// Function that animates scoreboard scroll, called when timer is finished
function scoreScroll() {
	var pos = $("#scoreboard").offset().top;

    $("body").animate(
    {
        scrollTop: pos + "px"
    }, 1000);
}

// Building score html with jQuery
function scoreBuilder(user, words, letters) {

	var row = $("<tr>");

	var colu = $("<td>").text(user);
	var colw = $("<td>").text(words);
	var coll = $("<td>").text(letters);

	var colr = $("<td>");
	var link = $("<a>").addClass("remove_score").attr("href", "#");
	var icon = $("<i>").addClass("small").addClass("material-icons").text("delete");

	link.append(icon);
	colr.append(link);

	row.append(colu);
	row.append(colw);
	row.append(coll);
	row.append(colr);

	return row;
}

// Remove score event wrapper
function scoreRemove() {

	event.preventDefault();

	var row = $(this).parent().parent();

	row.fadeOut(500);
	
	setTimeout(function () {
		row.remove();
	}, 600);

}

// Shows scoreboard
function scoreShow() {
	// Stop is used to stop all current animations
	$("#scoreboard").stop().slideToggle(600);
}