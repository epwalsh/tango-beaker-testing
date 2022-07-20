from tango import Step


@Step.register("generate-name")
class GenerateNameStep(Step):

    VERSION = "001"
    CACHEABLE = True

    def run(self, seed: int = 1) -> str:  # type: ignore[override]
        if seed == -1:
            raise ValueError("seed must be non-negative")

        import random

        random.seed(seed)

        return random.choice(["Billy", "Bob", "Larry", "Randy"])


@Step.register("hello")
class HelloStep(Step):

    VERSION = "007"
    CACHEABLE = True

    def run(self, name: str) -> str:  # type: ignore[override]
        greeting = f"Hello, {name}!"
        self.logger.info(greeting)
        return greeting
