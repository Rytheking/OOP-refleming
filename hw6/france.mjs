import { CountryModel } from './country.mjs'

export class FranceModel extends CountryModel {
    constructor(config) {
        super(config.distance, config.orbits);
        this._population = config.population;
        this._govType = config.govType;
        this._head = config.head;
        this._year = config.year
    }

    get head() {
        return this._head
    }

    set head(value) {
        this._head=value
    }

    get govType() {
        return this._govType
    }

    set govType(value) {
        this._govType=value
    }

    get population() {
        return this._population
    }
    set population(value) {
        this._population=value
    }
}

export class FranceController {
    constructor(model) {
        this._model = model;
    }
    get model() {
        return this._model;
    }

    year() {
        this._model.year = this._model.year+1
    }

    isNewFrance() {
        return this._model.year == 481
    }
}

export class FranceView {
    createImage() {
        const canvas = document.createElement("img");
        canvas.setAttribute("id", this._id + "-img");
        img.width = 200;
        img.height = 200;
        img.setAttribute("src", "/france.jpg");
        img.setAttribute("alt", "france");
        img.setAttribute("style", "border: 1px solid black");
        return img;
    }

    constructor(model, controller, div, id, config) {
        this._model = model;
        this._controller = controller;
        this._div = div;
        this._id = id;
        this._div.innerHTML = "France(id=" + this._id + ", govType=" + this._govType + ")";
        this._img = this.createImage();
        this._div.appendChild(this._img);
        const me = this;
        setInterval(() => { me.year(); }, 1000);
    }

    onFranceModelChange() {
        this.redraw();
    }

    redraw() {
    }

}


export function FranceInstantiate() {
    const divs = document.getElementsByClassName("France");
    for (let i = 0; i < divs.length; ++i) {
        const div = divs[i];
        const id = "France-" + i;
        const config = JSON.parse(div.getAttribute("data-config"));
        const France = new France(div, id, config)
    }
}
