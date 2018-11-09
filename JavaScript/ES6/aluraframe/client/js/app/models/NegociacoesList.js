class NegociacoesList {

    constructor() {

        this._negociacoes = [];
    }

    add(negociacao) {

        this._negociacoes.push(negociacao);
    }

    get negociacoes() {

        return [].concat(this._negociacoes);
    }

    empty() {

        this._negociacoes = [];
    }

    get volume() {
        return this._negociacoes.reduce((total, n) => total + n.volume, 0.0);
    }
}