import os
images = list(os.listdir('images/'))

for image in images:
    a = str(image)
    print('<a href="images/' + a + '"><img src="thumbnails/' + a.replace('.jpg', '.webp') + '"></a>')