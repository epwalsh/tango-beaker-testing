from beaker import Beaker, DatasetNotFound

if __name__ == "__main__":
    beaker = Beaker.from_env(default_workspace="ai2/beaker-tango-testing")
    for dataset in beaker.workspace.datasets():
        print(f"Deleting dataset {beaker.dataset.url(dataset)}")
        beaker.dataset.delete(dataset)
    for experiment in beaker.workspace.experiments():
        print(f"Deleting experiment {beaker.experiment.url(experiment)}")
        try:
            beaker.experiment.delete(experiment)
        except DatasetNotFound:
            pass
