{
  steps: {
    name: { type: "generate-name", seed: 2 },
    hello: { type: "hello", name: { type: "ref", ref: "name" } },
    hello_you: { type: "hello", name: "you" },
    hello_me: { type: "hello", name: "me" },
  }
}
