import { describe, it, expect } from 'vitest';
import { greet } from '../src/index.js';

describe('b', () => {
  it('greets', () => { expect(greet('x')).toBe('hello x'); });
});
