from beaker import Beaker

if __name__ == "__main__":
    beaker = Beaker.from_env(default_workspace="ai2/petew-testing")
    print(beaker.workspace.clear(images=False, secrets=False))
