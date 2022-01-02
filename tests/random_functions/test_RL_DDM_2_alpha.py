import os
import pandas as pd

from rlssm.random.random_RL_DDM import simulate_rlddm_2A
from rlssm.random.random_common import generate_task_design_fontanesi


# Reinforcement learning data
def test_RL_DDM_2_alpha(print_results=True):
    print("Test - RL + DDM 2 alpha; simulate_rlddm_2A")

    dm = generate_task_design_fontanesi(n_trials_block=80,
                                        n_blocks=3,
                                        n_participants=1,
                                        trial_types=['1-2', '1-3', '2-4', '3-4'],
                                        mean_options=[34, 38, 50, 54],
                                        sd_options=[5, 5, 5, 5])

    data = simulate_rlddm_2A(task_design=dm,
                             gen_alpha=[.1, .01],
                             gen_drift_scaling=.1,
                             gen_threshold=1,
                             gen_ndt=.23,
                             initial_value_learning=0)

    # Test data produced against reference data
    reference_path = os.path.join(os.path.dirname(__file__), 'reference_data', 'RL_DDM_2_alpha.csv')
    # data.to_csv(reference_path)
    reference_data = pd.read_csv(reference_path, index_col=0)
    # assert data.equals(reference_data)

    if print_results:
        print(data)
