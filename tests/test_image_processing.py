import numpy as np
from neural_upscaler import image_processing

def test_read_image_return_value(prague_photo_path):
    img = image_processing.read_image(prague_photo_path)
    assert isinstance(img, np.ndarray)
