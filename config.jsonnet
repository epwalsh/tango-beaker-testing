{
  steps: {
    name: { type: "generate-name", seed: 1 },
    hello: { type: "hello", name: { type: "ref", ref: "name" } },
  }
}
