import numpy as np
from spaceship import Spaceship

def sexytimes(papa_bear, mama_bear):
    baby_weights = []
    for papa_weight, mama_weight in zip(papa_bear.agent.model.model.get_weights(), mama_bear.agent.model.model.get_weights()):
        gene_mask = np.random.normal(*papa_weight.shape) > 0.5
        baby_weights.append(np.where(gene_mask, papa_weight, mama_weight))
    brother_bear, sister_bear = Spaceship(papa_bear.screen, papa_bear.telemetry.world), Spaceship(papa_bear.screen, papa_bear.telemetry.world)
    brother_bear.agent.model.model.set_weights(baby_weights)
    sister_bear.agent.model.model.set_weights(baby_weights)
    brother_bear.agent.model.mutate()
    sister_bear.agent.model.mutate()
    return brother_bear, sister_bear