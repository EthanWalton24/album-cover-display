import os,time,sys,urllib.request
from PIL import Image




def displayCover(matrix,coverURL=None):

    #display album cover if given an image
    if coverURL is not None:

        #get image from url
        urllib.request.urlretrieve(
            coverURL,
            'cover.jpg'
        )

        #open and format image from url
        image = Image.open('cover.jpg')
        image = image.rotate(90)
        image = image.resize((64,64))
        image.thumbnail((matrix.width,matrix.height),Image.ANTIALIAS)

        matrix.SetImage(image.convert('RGB'))


    #display default image if not given an image
    if coverURL is None:
        
        #open and format image from url
        image = Image.open('cover.jpg')
        image = image.rotate(90)
        image = image.resize((64,64))
        image.thumbnail((matrix.width,matrix.height),Image.ANTIALIAS)

        matrix.SetImage(image.convert('RGB'))
