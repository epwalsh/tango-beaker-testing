{
  steps: {
    name: { type: "generate-name", seed: 2 },
    hello: { type: "hello", name: { type: "ref", ref: "name" } },
  }
}
