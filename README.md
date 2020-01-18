# RESPOSITORY MOVED

This repository has been moved to the main ncss-summer-school repository.
Further changes and bugs should be directed there.

The contents of the repository before the move are archived here.

# ncss-embedded
Booklet (lectures, lab notes, samples and demos) for NCSS Embedded stream

## Authoring

### Equations
Use [Math URL](http://mathurl.com/) to generate a PNG, and then embed using Markdown:

```
![Taylor Series](http://mathurl.com/yaay9fvf.png)
```

You can edit the equation (and generate a new URL) by removing the `.png` from the URL.

### Code snippets
Use regular markdown code blocks, with the `python` language set. e.g.

````
```python
from microbit import *
display.show(Image.HEART)
```
````

### Emoji
If you put emoji into the main text, you need to tell TeX about it, since emoji by default cannot be embedded in PDFs (there is no support for image-based fonts in the pdf spec).
Therefore, add a string like:
```tex
\newunicodechar{😛}{{\emoji{1f600}}}
```
to the `notes.tex` file, and include a PNG version of the image in the emoji folder.

## Printing
To print GitHub markdown, see [this page](https://jimmo.id.au/print.html).

