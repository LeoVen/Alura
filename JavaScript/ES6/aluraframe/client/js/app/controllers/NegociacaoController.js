class NegociacaoController {

    constructor () {
        //let $ = document.querySelector;
        let $ = document.querySelector.bind(document);

        this._data = $('#data');
        this._quantidade = $('#quantidade');
        this._valor = $('#valor');

        this._list = new Bind(
            new NegociacoesList(),
            new NegociacoesView($('#negociacoesView')),
            'add', 'empty'
        );

        this._mensagem = new Bind(
            new Mensagem(),
            new MensagemView($('#mensagemView')),
            'texto'
        );
    }

    add(event) {

        event.preventDefault();

        this._list.add(this._createNegociacao());

        this._mensagem.texto = 'Negociação adicionada com sucesso';

        this._clearForm();
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

        this._mensagem.texto = "Negociacoes apagadas com sucesso";
    }

    import() {

        let xhr = new XMLHttpRequest();

        xhr.open('GET', 'negociacoes/semana');

        // 0: requisição ainda não iniciada
        //
        // 1: conexão com o servidor estabelecida
        //
        // 2: requisição recebida
        //
        // 3: processando requisição
        //
        // 4: requisição está concluída e a resposta está pronta
        xhr.onreadystatechange = () => {

            if (xhr.readyState === 4) {

                if (xhr.status === 200) {
                    console.log("Getting server information");
                    JSON.parse(xhr.responseText)
                        .map(obj => new Negociacao(new Date(obj.data), obj.quantidade, obj.valor))
                        .forEach(neg => this._list.add(neg));

                    this._mensagem.texto = "Negociações importadas com sucesso"
                }
                else {
                    console.log(xhr.responseText);
                    this._mensagem.texto = "Não foi possível importar as negociações";
                }
            }
        }

        xhr.send();
    }
}