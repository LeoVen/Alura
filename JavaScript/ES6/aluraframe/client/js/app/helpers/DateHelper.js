class DateHelper {

    constructor() {
        throw new Error('DateHelper can not be instantiated');
    }

    static textToDate(text) {

        let exp = /\d{4}-\d{2}-\d{2}/;

        if (!exp.test(text))
            throw new Error('Must be in the format yyyy-mm-dd');

        return new Date(
            ...text
                .split('-')
                .map((item, index) => (index === 1) ? item - 1 : item)
        );
    }

    static dateToText(date) {

        return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
    }

}