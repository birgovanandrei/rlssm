from rlssm import RLARDModel_2A
from tests.model_creation.common_methods import check_pkl_file_existence


def test_model_RLARDM(hier_levels=1, print_results=True):
    model_name = "RLARDM"

    rlardm_model = RLARDModel_2A(hierarchical_levels=hier_levels)

    check_pkl_file_existence(model_name=model_name, hier_levels=hier_levels)