from unitytrainers.trainer_controller import TrainerController
import os
import numpy as np
import time
tc = TrainerController('python/Balance', None, None, None, None, None, True,
                      0, 0, 0, 0, '', os.path.abspath(os.path.join(os.path.dirname(__file__), "trainer_config.yaml")))

class Net():
    def forward(self):
        return np.random.randint(0,180)

pop = 10
bots = []
env = tc.env
[bots.append(Net()) for i in range(pop)]
default_brain = env.external_brain_names[0]
brain = env.brains[default_brain]
rewards = [0] * pop
fittest = {}
max_gens = 1000
max_frames = 10000
state = env.reset(train_mode=True)[default_brain]
print()

for generation in range(max_gens):
    print("         GENERATION "+str(generation))
    print("----------------------------")
    print()
    for count, bot in enumerate(bots):
        frame = 0
        terminal = False
        while state.vector_observations[0] < -1 or state.vector_observations[0] > 1:
            state = env.step(0)[default_brain]
        print("Bot "+str(count))
        while frame < max_frames and not terminal:
            frame += 1
            print(" ------ "+str(state.vector_observations[0]))
            if state.vector_observations[0] > 90 or state.vector_observations[0] < -90:
                terminal = True
            state = env.step(bot.forward())[default_brain]
        rewards[count] = frame
        print(" --- "+str(frame))
        print()
        print("----------------------------")
        print()

    tmp = 0
    tmpindex = 0
    for count, i in enumerate(rewards):
        if i > tmp:
            tmp = i
            tmpindex = count

    fittest.update({tmp:tmpindex})

    print(fittest)
