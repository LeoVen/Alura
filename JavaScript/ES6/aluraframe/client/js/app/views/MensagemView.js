class MensagemView extends View {

    constructor(element) {
        super(element);
    }

    _template(model) {

        return model.texto ? `<p class="alert alert-info">${model.texto}</p>` : `<p></p>`;
    }

}