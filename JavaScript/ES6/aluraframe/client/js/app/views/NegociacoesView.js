class NegociacoesView {

    constructor(element) {

        this._element = element;
    }

    update(model) {

        this._element.innerHTML = this._template(model);
    }

    _template(model) {

        return `
            <table class="table table-hover table-bordered">
                <thead>
                    <tr>
                        <th>DATA</th>
                        <th>QUANTIDADE</th>
                        <th>VALOR</th>
                        <th>VOLUME</th>
                    </tr>
                </thead>
                <tbody>
                    ${model.negociacoes.map(el => `
                        <tr>
                            <td>${DateHelper.dateToText(el.date)}</td>
                            <td>${el.quantity}</td>
                            <td>${el.value}</td>
                            <td>${el.volume}</td>
                        </tr>
                    `).join('')}
                </tbody>
                <tfoot>
                    <td colspan="3"></td>
                    <td>
                        ${model.negociacoes.reduce((total, n) => total + n.volume, 0.0)}
                    </td>
                </tfoot>
            </table>
        `;
    }
}

// Immediately-invoked function expression
/*
${
    (() => {
        let total = 0;
        model.negociacoes.forEach(n => total += n.volume);
        return total;
    })()
}*/
