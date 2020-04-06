import matplotlib.pyplot as plt

def view(original, ny1, BW, ny2, text):
    """
    Viser bildene ved siden av hverandre.
    
    Original, svart-hvit og glattet

    Parameters
    ---------
    original : Bildefil
               Pathen til filen der original bildet befinner seg uten andvending
    ny1       : Bildefil
                Bildet som har blitt anvendt
    BW       : Bildefil
               Pathen til filen der svart-hvit bildet befinner seg
    ny       : Bildefil
               Bildet som har blitt anvendt i svart-hvitt
    text     : text
               Tittelen på bildet som er anvendt
    """
    plt.figure(figsize=(16, 8))
    plt.subplot(131)    
    plt.imshow(original, plt.cm.gray)
    plt.title('Originalbilde')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(ny1, plt.cm.gray)
    plt.title(text)
    plt.axis('off')
    
    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)
    
    plt.figure(figsize=(16, 8))
    plt.subplot(131)    
    plt.imshow(BW, plt.cm.gray)
    plt.title('Gråskala')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(ny2, plt.cm.gray)
    plt.title(text)
    plt.axis('off')

    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)

def viewInpaint(original, mask, ny, text, rgb):
    """
    Viser bildene ved siden av hverandre.
    
    Original, masken og inpainted

    Parameters
    ---------
    original : Bildefil
               Pathen til filen der original bildet befinner seg uten andvending
    mask       : Bildefil
               Masken til bildet
    ny       : Bildefil
               Bildet som har blitt anvendt
    text     : text
               Tittelen på bildet som er anvendt
    rgb      : bool
               Fargebilde/gråtone
    
    """
    plt.figure(figsize = (20, 10))
    plt.subplot(131)
    if rgb:
        plt.imshow(original)
    else:
        plt.imshow(original, plt.cm.gray)
    plt.title('Originalbilde')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(mask)
    plt.imshow(mask, plt.cm.gray)
    plt.title('Mask')
    plt.axis('off')
    
    plt.subplot(133)
    if rgb:
        plt.imshow(ny)
    else:
        plt.imshow(ny, plt.cm.gray)
    plt.title(text)
    plt.axis('off')

    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)

def singleView(image, title):
    plt.figure(figsize = (20,10))
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')