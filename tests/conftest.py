from pathlib import Path
import pytest

@pytest.fixture
def test_data_folder():
    return Path(__file__).parent /"test_data"

@pytest.fixture
def prague_photo_path(test_data_folder):
    return test_data_folder / "prague.jpg"

@pytest.fixture
def mongolia_photo_path(test_data_folder):
    return test_data_folder / "mongolia.jpg"