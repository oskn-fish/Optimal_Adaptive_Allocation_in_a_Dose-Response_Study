# from gym.envs.registration import register
from gymnasium.envs.registration import register

register(
    id='MCPMod-v0',
    entry_point='MCPMod.envs:MCPModEnv'
)
