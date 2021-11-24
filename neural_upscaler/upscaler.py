from neural_upscaler import image_processing

def run(img_path, output_path, show_comparison=False):
    img = image_processing.read_image(img_path)
    
    img = crop_to_correct_dim(img)
    img = fill_to_target_resolution(img)
    img = upscale(img)
    
    if show_comparison:
        image_processing.show(img)

    if output_path:
        save(img, output_path)