import numpy as np

from rllab.misc.instrument import VariantGenerator
from sac.misc.utils import flatten, get_git_rev, deep_update

M = 256
REPARAMETERIZE = True

LSP_POLICY_PARAMS_BASE = {
    'type': 'lsp',
    'coupling_layers': 2,
    's_t_layers': 1,
    'action_prior': 'uniform',
    # 'preprocessing_hidden_sizes': None,
    'preprocessing_output_nonlinearity': 'relu',
    'reparameterize': REPARAMETERIZE,
    'squash': True
}

LSP_POLICY_PARAMS = {
   
    'humanoid-rllab': { # 21 DoF
        'preprocessing_hidden_sizes': (M, M, 42),
        's_t_units': 21,
    },
    'cassie' :{
    'preprocessing_hidden_sizes': (M, M, 42),
    's_t_units': 21
    }
}

GMM_POLICY_PARAMS_BASE = {
    'type': 'gmm',
    'K': 1,
    'reg': 1e-3,
    'action_prior': 'uniform',
    'reparameterize': REPARAMETERIZE
}

GMM_POLICY_PARAMS = {
   
    'humanoid-rllab': { # 21 DoF
    },
    'humanoid-standup-gym': { # 17 DoF
    },
    'cassie' : {}
}

GAUSSIAN_POLICY_PARAMS_BASE = {
    'type': 'gaussian',
    'reg': 1e-3,
    'action_prior': 'uniform',
    'reparameterize': REPARAMETERIZE
}

GAUSSIAN_POLICY_PARAMS = {
    
    'humanoid-rllab': { # 21 DoF
    },
    'humanoid-standup-gym': { # 17 DoF
    },
    'cassie': {}
}

POLICY_PARAMS = {
    'lsp': {
        k: dict(LSP_POLICY_PARAMS_BASE, **v)
        for k, v in LSP_POLICY_PARAMS.items()
    },
    'gmm': {
        k: dict(GMM_POLICY_PARAMS_BASE, **v)
        for k, v in GMM_POLICY_PARAMS.items()
    },
    'gaussian': {
        k: dict(GAUSSIAN_POLICY_PARAMS_BASE, **v)
        for k, v in GAUSSIAN_POLICY_PARAMS.items()
    },
}

VALUE_FUNCTION_PARAMS = {
    'layer_size': M,
}

ENV_DOMAIN_PARAMS = {
   
    'humanoid-rllab': { # 21 DoF
    },
    'humanoid-standup-gym': { # 17 DoF
    },
    'cassie': {}
}

ENV_PARAMS = {
    'swimmer-rllab': { # 2 DoF
    },
    'hopper': { # 3 DoF
    },
    'half-cheetah': { # 6 DoF
    },
    'walker': { # 6 DoF
    },
    'ant': { # 8 DoF
        'resume-training': {
            'low_level_policy_path': [
                # 'ant-low-level-policy-00-00/itr_4000.pkl',
            ]
        },
        'cross-maze': {
            'terminate_at_goal': True,
            'goal_reward_weight': [1000],
            'goal_radius': 2,
            'velocity_reward_weight': 0,
            'ctrl_cost_coeff': 0, # 1e-2,
            'contact_cost_coeff': 0, # 1e-3,
            'survive_reward': 0, # 5e-2,
            'goal_distance': 12,
            'goal_angle_range': (0, 2*np.pi),

            'env_fixed_goal_position': [[6, -6], [6, 6], [12, 0]],

            'pre_trained_policy_path': []
        },
    },
    'humanoid-gym': { # 17 DoF
        'resume-training': {
            'low_level_policy_path': [
                # 'humanoid-low-level-policy-00-00/itr_4000.pkl',
            ]
        }
    },
    'humanoid-rllab': { # 21 DOF
    },
    'humanoid-standup-gym': { # 17 DoF
    },
    'cassie': {
        'task': ['running', 'fix-vel'],
    }
}

ALGORITHM_PARAMS_BASE = {
    'lr': [3e-4, 0.2],
    'discount': 0.99,
    'target_update_interval': 1,
    'tau': 0.005,
    'reparameterize': REPARAMETERIZE,

    'base_kwargs': {
        'epoch_length': 1000,
        'n_train_repeat': 1,
        'n_initial_exploration_steps': 1000,
        'eval_render': False,
        'eval_n_episodes': 1,
        'eval_deterministic': True,
    }
}

ALGORITHM_PARAMS = {
    'swimmer-rllab': { # 2 DoF
        'scale_reward': 25,
        'base_kwargs': {
            'n_epochs': 1e3,
        }
    },
    'hopper': { # 3 DoF
        'scale_reward': 5,
        'base_kwargs': {
            'n_epochs': 1e3,
        }
    },
    'half-cheetah': { # 6 DoF
        'scale_reward': 5,
        'base_kwargs': {
            'n_epochs': 3e3,
            'n_initial_exploration_steps': 10000,
        }
    },
    'walker': { # 6 DoF
        'scale_reward': 5,
        'base_kwargs': {
            'n_epochs': 1e3,
        }
    },
    'ant': { # 8 DoF
        'scale_reward': 5,
        'base_kwargs': {
            'n_epochs': 3e3,
            'n_initial_exploration_steps': 10000,
        }
    },
    'humanoid-gym': { # 17 DoF
        'scale_reward': 20,
        'base_kwargs': {
            'n_epochs': 1e4,
        }
    },
    'humanoid-rllab': { # 21 DoF
        'scale_reward': 10,
        'base_kwargs': {
            'n_epochs': 1e4,
        }
    },
    'humanoid-standup-gym': { # 17 DoF
        'scale_reward': 100,
        'base_kwargs': {
            'n_epochs': 1e4,
        }
    },
    'cassie': {
    'scale_reward': 10,
    'base_kwargs': {
    'n_epochs': 1e4
    }
    }
}

REPLAY_BUFFER_PARAMS = {
    'max_replay_buffer_size': 1e6,
}

SAMPLER_PARAMS = {
    'max_path_length': 1000,
    'min_pool_size': 1000,
    'batch_size': [256, 512],
}

RUN_PARAMS_BASE = {
    'seed': [1,2],
    'snapshot_mode': 'gap',
    'snapshot_gap': 1000,
    'sync_pkl': True,
}

RUN_PARAMS = {
    
    'cassie': {
    'snapshot_gap': 2000
    }
}


DOMAINS = [
    'swimmer-rllab', # 2 DoF
    'hopper', # 3 DoF
    'half-cheetah', # 6 DoF
    'walker', # 6 DoF
    'ant', # 8 DoF
    'humanoid-gym', # 17 DoF # gym_humanoid
    'humanoid-rllab', # 21 DoF
    'humanoid-standup-gym', # 17 DoF # gym_humanoid
    'cassie'
]

TASKS = {
    'swimmer-rllab': [
        'default',
        'multi-direction',
    ],
    'hopper': [
        'default',
    ],
    'half-cheetah': [
        'default',
    ],
    'walker': [
        'default',
    ],
    'ant': [
        'default',
        'multi-direction',
        'cross-maze'

    ],
    'humanoid-gym': [
        'default',
    ],
    'humanoid-rllab': [
        'default',
        'multi-direction'
    ],
    'humanoid-standup-gym': [
        'default',
    ],
    'cassie': [
    'default'
    ]
}

def parse_domain_and_task(env_name):
    domain = next(domain for domain in DOMAINS if domain in env_name)
    domain_tasks = TASKS[domain]
    task = next((task for task in domain_tasks if task in env_name), 'default')
    return domain, task

def get_variants(domain, task, policy):
    params = {
        'prefix': '{}/{}'.format(domain, task),
        'domain': domain,
        'task': task,
        'git_sha': get_git_rev(),

        'env_params': ENV_PARAMS[domain].get(task, {}),
        'policy_params': POLICY_PARAMS[policy][domain],
        'value_fn_params': VALUE_FUNCTION_PARAMS,
        'algorithm_params': deep_update(
            ALGORITHM_PARAMS_BASE,
            ALGORITHM_PARAMS[domain]
        ),
        'replay_buffer_params': REPLAY_BUFFER_PARAMS,
        'sampler_params': SAMPLER_PARAMS,
        'run_params': deep_update(RUN_PARAMS_BASE, RUN_PARAMS[domain]),
    }

    # TODO: Remove flatten. Our variant generator should support nested params
    params = flatten(params, separator='.')

    vg = VariantGenerator()
    for key, val in params.items():
        if isinstance(val, list) or callable(val):
            vg.add(key, val)
        else:
            vg.add(key, [val])

    return vg
