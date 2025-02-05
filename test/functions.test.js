const { add } = require('../src/functions');
const assert = require('assert');

describe('add', () => {
  it('should return the sum of two numbers', () => {
    assert.strictEqual(add(1, 2), 3);
    assert.strictEqual(add(-1, -1), -2);
  });

  it('should return 0 when both arguments are 0', () => {
    assert.strictEqual(add(0, 0), 0);
  });
});
