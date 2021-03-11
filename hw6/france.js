class France {
    constructor(govType, head, population, year) {
        this._govType = govType
        this._head = head
        this._population = population
        this._year = year
    }

    newYear() {
        this._year= this._year+1
        this._population = (this._population*1.14)
    }

    get govType() {
        return this._govType
    }
    get head() {
        return this._head
    }
    get population() {
        return this._population
    }
    get year() {
        return this._year
    }

    set govType(value) {
        this._govType=value
    }
    set head(value) {
        this._head=value
    }
}

module.exports = { 'France' : France }