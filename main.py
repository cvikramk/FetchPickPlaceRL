import gym
import time
from gym.envs.registration import register
from model import *



initial_qpos = {
            "robot0:slide0": 0.405,
            "robot0:slide1": 0.48,
            "robot0:slide2": 0.0,
            "object0:joint": [5.0, 5.0, 5.0, 1.0, 0.0, 0.0, 0.0],
        }
register(id="FetchPickAndPlace-v2", entry_point="env:FetchPickAndPlaceEnv", max_episode_steps=50)
env = gym.make('FetchPickAndPlace-v2')
# print(env.model.gravity)
env.initial_qpos = initial_qpos
state_size = env.observation_space.shape
action_size = env.action_space.shape
print(env.observation_space,action_size)
# exit(0)
state = env.reset()
env.render()
# time.sleep(10)
done = False
def policy(state):
	return env.action_space.sample()
# print(env.action_space.n)
# exit(0)
while True:
	action = policy(state)

	next_state,reward,done,info = env.step(action)
	state = next_state
	env.render()
	if done:
		break
env.close()

# actor = Actor(state_size, action_size).to(device)
# critic = Critic(state_size, action_size).to(device)
# trainIters(actor, critic, n_iters=100)