class NegociacaoController {

    constructor () {
        //let $ = document.querySelector;
        let $ = document.querySelector.bind(document);

        this._data = $('#data');
        this._quantidade = $('#quantidade');
        this._valor = $('#valor');
        this._list = new NegociacoesList();
        this._view = new NegociacoesView($('#negociacoesView'));

        this._view.update(this._list);
    }

    add(event) {

        event.preventDefault();

        this._list.add(this._createNegociacao());
        this._clearForm();
        this._view.update(this._list);
    }

    _createNegociacao() {

        return new Negociacao(
            DateHelper.textToDate(this._data.value),
            this._quantidade.value,
            this._valor.value
        );
    }

    _clearForm() {

        this._data.value = '';
        this._quantidade.value = 1;
        this._valor.value = 0.0;

        this._data.focus();
    }
}