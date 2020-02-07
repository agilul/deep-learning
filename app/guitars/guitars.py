from fastai.vision import defaults, torch, Path, open_image, load_learner

defaults.device = torch.device("cpu")
path = Path("app/guitars")
learn = load_learner(path)


def handle(image):
    img = open_image(image)
    _, _, output = learn.predict(img)
    return zip(learn.data.classes, output.tolist())
