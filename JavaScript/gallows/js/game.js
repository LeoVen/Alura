const createGame = sprite => {

    let secretWord = '';
    let letters = [];
    let phase = 1;

    const winner = () => {

        return letters.length
            ? !letters.some(letter => letter === '')
            : false;
    };

    const looser = () => sprite.isFinished();

    const winOrLost = () => winner() || looser();

    const restart = () => {

        phase = 1;
        letters = [];
        secretWord = '';
        sprite.reset();
    };

    const process = word => {

        if (!word.trim())
            throw Error('Chute invalido');

        const exp = new RegExp(word, 'gi');
        let result,
            hit = false;

        while (result = exp.exec(secretWord)) {

            letters[result.index] = word;

            hit = true;
        }

        if (!hit) {
            sprite.nextFrame();
        }
    };

    const createLetters = () => {

        for (let i = 0; i < secretWord.length; i++)
            letters.push('');
    };

    const nextPhase = () => {

        phase = 2;
    };

    const setSecretWord = word => {

        if (!word.trim())
            throw Error('Palavra invalida');

        secretWord = word;
        createLetters();
        nextPhase();
    };

    const getLetters = () => letters;

    const getPhase = () => phase;

    return {
        setSecretWord,
        getLetters,
        getPhase,
        process,
        winner,
        looser,
        winOrLost,
        restart
    };
}