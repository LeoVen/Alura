const createController = game => {

    const $input = $('.entrada');
    const $letters = $('.lacunas');

    const displayLetters = () => {

        $letters.empty();
        game.getLetters().forEach(function (letter) {
            $('<li>')
                .addClass('lacuna')
                .text(letter)
                .appendTo($letters);
        });
    };

    const changePlaceHolder = text => $input.attr('placeholder', text);

    const storeSecretWord = () => {

        try {
            game.setSecretWord($input.val().trim());

            $input.val('');
            changePlaceHolder('Chute');
            displayLetters();
        } catch (err) {
            alert (err.message);
        }

    };

    const restartController = () => {

        game.restart();
        $letters.empty();
        changePlaceHolder('palavra secreta');
    };

    const readInput = () => {

        try {
            game.process($input.val().trim().substr(0, 1));
            $input.val('');
            displayLetters();

            if (game.winOrLost()) {

                setTimeout(function () {

                    if (game.winner()) {
                        alert("Congratulations! You won!");
                    } else {
                        alert("Oh no! You lost!");
                    }
                    restartController();
                }, 200);
            }
        } catch (err) {
            alert(err.message);
        }
    };

    const start = () => {

        $input.keypress(function (event) {
            if (event.which === 13) {
                switch (game.getPhase()) {
                    case 1:
                        storeSecretWord();
                        break;
                    case 2:
                        readInput();
                        break;
                }
            }
        });
    };

    // retorna um objeto com a propriedade start, que deve ser chamada assim que o controller for criado.
    return {start: start};
};