# python-glrlm

This is library of Gray Level Run Length Matrix, feature extraction method of image processing

![GitHub](https://img.shields.io/github/license/eiproject/python-glrlm)
![GitHub top language](https://img.shields.io/github/languages/top/eiproject/python-glrlm)
![GitHub all releases](https://img.shields.io/github/downloads/eiproject/python-glrlm/total)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eiproject/python-glrlm)

## Installation

```console
pip install glrlm
```

## Usage Example

```python
from glrlm import GLRLM
import cv2

IMG_PATH = 'path_to_your/image'
img = cv2.imread(IMG_PATH)

app = GLRLM()
glrlm = app.get_features(img, 8)
```

## Features extracted

Feature extraction result from GLRLM library

- SRE = Short Run Emphasis
- LRE = Long Run Emphasis
- GLU = Grey Level Uniformity
- RLU = Run Length Uniformity
- RPC = Run Percentage

## Support

Reach me out on [Email](mailto:razifrizqullah@gmail.com "razifrizqullah@gmail.com")

## Contribution

If you find out this library as useful please give it a star to let everyone know. If you have idea on how to improve this library, I am always open for every contributors. Thank you!
