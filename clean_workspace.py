from beaker import Beaker

beaker = Beaker.from_env(default_workspace="ai2/beaker-tango-testing")
for dataset in beaker.workspace.datasets():
    beaker.dataset.delete(dataset)
for experiment in beaker.workspace.experiments():
    beaker.experiment.delete(dataset)
