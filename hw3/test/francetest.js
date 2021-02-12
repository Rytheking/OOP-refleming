const assert = require('assert');
const chai = require('chai');
const { France }  = require('../france');

const expect = chai.expect;
const assertEq = assert.deepStrictEqual

describe('France', function() {
  describe('#constructor', function() {
    it('can be made', function(){
		const govType= 3
        const head = "blue"
        const population = 28000000
        const year = 1776
        const France = new France(govType, head, population, year)
        assertEq(govType, France.govType)
        assertEq(France.head,head)
        assertEq(France.population,population)
        assertEq(France.year,year)
        France.newYear()
        assertEq(France.population,population*1.14)
        assertEq(France.year,year+1)

    });
  });
});