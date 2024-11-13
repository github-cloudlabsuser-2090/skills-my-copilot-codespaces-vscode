const assert = require('assert');
const Calculator = require('./test').Calculator;

describe('Calculator', function() {
    let calc;

    beforeEach(function() {
        calc = new Calculator();
    });

    describe('#add()', function() {
        it('should return 8 when adding 5 and 3', function() {
            assert.strictEqual(calc.add(5, 3), 8);
        });

        it('should return -2 when adding -5 and 3', function() {
            assert.strictEqual(calc.add(-5, 3), -2);
        });
    });

    describe('#subtract()', function() {
        it('should return 2 when subtracting 3 from 5', function() {
            assert.strictEqual(calc.subtract(5, 3), 2);
        });

        it('should return -8 when subtracting 3 from -5', function() {
            assert.strictEqual(calc.subtract(-5, 3), -8);
        });
    });

    describe('#multiply()', function() {
        it('should return 15 when multiplying 5 and 3', function() {
            assert.strictEqual(calc.multiply(5, 3), 15);
        });

        it('should return -15 when multiplying -5 and 3', function() {
            assert.strictEqual(calc.multiply(-5, 3), -15);
        });
    });

    describe('#divide()', function() {
        it('should return 1.6666666666666667 when dividing 5 by 3', function() {
            assert.strictEqual(calc.divide(5, 3), 1.6666666666666667);
        });

        it('should throw an error when dividing by 0', function() {
            assert.throws(() => calc.divide(5, 0), Error, "Division by zero is not allowed.");
        });
    });
});