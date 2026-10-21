import { it, expect } from 'vitest';
import { shout } from '../src/index.js';

it('shouts', () => { expect(shout('x')).toBe('HELLO X'); });
