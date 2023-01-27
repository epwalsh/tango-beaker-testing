from beaker import Beaker

if __name__ == "__main__":
    beaker = Beaker.from_env(default_workspace="ai2/petew-testing")
    for experiment in beaker.workspace.experiments():
        print(f"Deleting experiment {beaker.experiment.url(experiment)}")
        beaker.experiment.delete(experiment)
    for dataset in beaker.workspace.datasets():
        print(f"Deleting dataset {beaker.dataset.url(dataset)}")
        beaker.dataset.delete(dataset)
