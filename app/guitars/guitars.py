from fastai.vision import defaults, torch, Path, open_image, load_learner

defaults.device = torch.device("cpu")
path = Path("app/guitars")
img = open_image(path/"myguitar.jpg")
learn = load_learner(path)


async def handle():
    pred_class, pred_idx, outputs = learn.predict(img)
    return pred_class
