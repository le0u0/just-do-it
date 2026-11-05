# When to Mock

Mock at **system boundaries** only:

- External APIs (payment, email).
- Databases, sometimes; prefer a test database.
- Time and randomness.
- File system, sometimes.

Never mock your own classes, modules, internal collaborators, or anything you control.

## Designing for mockability

At a system boundary, design interfaces that are easy to mock.

**Use dependency injection.** Pass external dependencies in instead of creating them inside:

```typescript
// Easy to mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Hard to mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**Prefer SDK-style interfaces over generic fetchers.** One specific function per external operation, not one function with conditional logic:

```typescript
// GOOD: each function is independently mockable
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch("/orders", { method: "POST", body: data }),
};

// BAD: mocking needs conditional logic inside the mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

Each mock then returns one specific shape, test setup has no conditional logic, it is clear which endpoints a test exercises, and types stay per endpoint.
