from tango import Step


@Step.register("hello")
class HelloStep(Step):
    VERSION = "001"
    CACHEABLE = False

    def run(self, name: str) -> str:  # type: ignore
        if name == "Sitka":
            raise ValueError("oh no!")
        return name
