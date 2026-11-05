# When to Mock

## Mock at system boundaries only

- External APIs (payment, email).
- Databases, sometimes; prefer a test database.
- Time and randomness.
- File system, sometimes.
- Never your own classes, modules, or internal collaborators.

## Design for mockability

- **Inject dependencies** instead of creating them inside:

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

- **Prefer SDK-style interfaces over generic fetchers:** one function per external operation, so each mock returns one shape, setup has no conditionals, and types stay per endpoint.

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
