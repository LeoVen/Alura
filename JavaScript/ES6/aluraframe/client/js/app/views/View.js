class View {

    constructor(element) {

        this._element = element;
    }

    _template() {
        throw new Error("_template() must be implemented");
    }

    update(model) {

        this._element.innerHTML = this._template(model);
    }

}