from tango import Step


@Step.register("hello")
class HelloStep(Step):

    VERSION = "002"

    def run(self) -> None:  # type: ignore[override]
        self.logger.info("Hello!")
