const assert = require('assert');
const chai = require('chai');
const { France } = require('../france');

const expect = chai.expect;
const assertEq = assert.deepStrictEqual

describe('France', function () {
    describe('#constructor', function () {
        it('can be made', function () {
            const govType = 3
            const head = "blue"
            const population = 28000
            const year = 1776
            const france = new France(govType, head, population, year)
            assertEq(govType, france.govType)
            assertEq(france.head, head)
            assertEq(france.population, population)
            assertEq(france.year, year)
        });
    });
    describe('#newYear()', function () {
        it('can be interacted with', function () {
            const govType = 3
            const head = "blue"
            const population = 2800
            const year = 1776
            const france = new France(govType, head, population, year)
            france.newYear()
            assertEq(france.population, population * 1.14)
            assertEq(france.year, year + 1)
        });
    });
});