# Good and Bad Tests

Illustrations in TypeScript. The project's own language, runner and conventions win.

## Good tests

Test through real interfaces, not mocks of internal parts.

```typescript
// GOOD: observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

- Tests behavior callers care about.
- Uses the public API only.
- Survives internal refactors.
- Describes what, not how.
- One logical assertion per test.

## Bad tests

**Implementation-detail tests** are coupled to internal structure.

```typescript
// BAD: asserts how checkout works inside
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags:

- Mocking internal collaborators.
- Testing private methods.
- Asserting call counts or order.
- The test breaks on a refactor that keeps behavior.
- The test name describes how, not what.
- Verifying through external means instead of the interface.

```typescript
// BAD: bypasses the interface to verify
test("createUser saves to database", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GOOD: verifies through the interface
test("createUser makes user retrievable", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

**Tautological tests** restate the implementation, so they pass by construction.

```typescript
// BAD: expected value is recomputed the way the code computes it
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// GOOD: expected value is an independent, known literal
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```
