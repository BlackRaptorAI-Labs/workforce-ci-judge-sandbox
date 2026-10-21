import { describe, it, expect } from 'vitest';
import { double } from '../src/index.js';

describe('a', () => {
  it('doubles', () => { expect(double(2)).toBe(4); });
});
