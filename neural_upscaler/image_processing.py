import matplotlib.pyplot as plt

def read_image(img_path):
    return plt.imread(img_path)

def show(img):
    fig = plt.imshow(img)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.draw()
    plt.waitforbuttonpress(0)