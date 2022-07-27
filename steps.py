import random

from tango import Step
from tango.format import JsonFormat


@Step.register("generate-name")
class GenerateNameStep(Step):

    VERSION = "001"
    CACHEABLE = True

    def run(self, seed: int = 1) -> str:  # type: ignore[override]
        return random.Random(seed).choice(["Billy", "Bob", "Larry", "Randy"])


@Step.register("hello")
class HelloStep(Step):

    VERSION = "007"
    CACHEABLE = True
    FORMAT = JsonFormat()

    def run(self, name: str) -> str:  # type: ignore[override]
        greeting = f"Hello, {name}!"
        self.logger.info(greeting)
        return greeting
