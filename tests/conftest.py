import os

import pytest


@pytest.fixture
def data_dir():
    top_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(top_dir, 'test_data')
