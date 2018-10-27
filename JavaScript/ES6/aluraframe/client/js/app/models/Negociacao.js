class Negociacao {

    constructor (date, quantity, value) {

        // Detaches reference to date
        this._date = new Date(date.getTime());
        this._quantity = quantity;
        this._value = value;

        // shallow
        //Object.freeze(this);
    }

    get volume () {
        return this._quantity * this._value;
    }

    get date () {
        return new Date(this._date.getTime());
    }

    get quantity () {
        return this._quantity;
    }

    get value () {
        return this._value;
    }

    // set volume () ...
    // set date () ...
    // set quantity () ...
    // set value () ...
}