from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CROPS = {
    "JASON_AND_THE_MLC_020.JPG": (0.70, 0.04, 0.96),
    "JASON_AND_THE_MLC_036.JPG": (0.52, 0.02, 0.98),
    "tosco_2022_christmas_pic.JPG": (0.65, 0.0, 1.0),
}

for name, (wf, y0, y1) in CROPS.items():
    path = ROOT / name
    im = Image.open(path)
    w, h = im.size
    im.crop((0, int(h*y0), int(w*wf), int(h*y1))).save(path, quality=90)
    print("cropped", name)
