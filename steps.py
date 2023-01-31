import random

from tango import step

VERSION = "011"


@step(version=VERSION)
def generate_name(seed: int = 1) -> str:
    if seed == -1:
        raise ValueError("seed must be non-negative")
    random.seed(seed)
    return random.choice(["Billy", "Bob", "Larry", "Randy"])


@step(bind=True, version=VERSION)
def hello(self, name: str) -> str:
    greeting = f"Hello, {name}!"
    self.logger.info(greeting)
    return greeting
