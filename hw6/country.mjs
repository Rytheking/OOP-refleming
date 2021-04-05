export class CountryModel {
    constructor(GDP, continent) {
        this._GDP = GDP;
        this._continent = continent;
    }
    get GDP() {
        return this._GDP;
    }

    get continent() {
        return this._continent;
    }
}

// module.exports = { 'SatelliteModel' : SatelliteModel };