class NegociacaoController {

    constructor () {
        //let $ = document.querySelector;
        let $ = document.querySelector.bind(document);

        this._data = $('#data');
        this._quantidade = $('#quantidade');
        this._valor = $('#valor');

        // model == this._list
        /*this._list = new NegociacoesList(model => {
            this._view.update(model);
        });*/

        // Using proxy
        /*this._list = new Proxy(new NegociacoesList(), {
            get: (target, prop, receiver) => {
                return Reflect.get(target, prop, receiver);
            }

            set: (target, prop, value, receiver) => {

                console.log(`${target[prop]} new value: ${value}`);
                return Reflect.set(target, prop, value, receiver);
            }
        });*/

        let self = this;
        this._list = new Proxy(new NegociacoesList(), {

            get(target, prop, receiver) {

                if (['add', 'empty'].includes(prop) && typeof(target[prop]) === typeof(Function)) {

                    return function () {

                        Reflect.apply(target[prop], target, arguments);

                        self._view.update(target);
                    }

                }

                return Reflect.get(target, prop, receiver);
            }
        });

        this._view = new NegociacoesView($('#negociacoesView'));
        this._view.update(this._list);

        this._mensagem = new Mensagem();
        this._mView = new MensagemView($('#mensagemView'));
        this._mView.update(this._mensagem);
    }

    add(event) {

        event.preventDefault();

        this._list.add(this._createNegociacao());
        this._clearForm();

        this._mensagem.texto = 'Negociação adicionada com sucesso';
        this._mView.update(this._mensagem);
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

    emptyList() {

        this._list.empty();

        this._mensagem.text = "Negociacoes apagadas com sucesso";
        this._mView.update(this._mensagem);
    }
}