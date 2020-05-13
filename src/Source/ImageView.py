import matplotlib.pyplot as plt

def subplotAdjust():
    """
    Setter rammene på bildene nærmere hverandre
    """
    return plt.subplots_adjust(wspace=0.02, hspace=0.02,
                                 top=0.9,   bottom=0,
                                 left=0,     right=1)
def twoImageSetup(im1, im2, title1="", title2=""):
    """
    Setter opp et standard bildeoppsett for 2 bilder for å displaye bildene i subplots
    
    Parameters
    ----------
    im1 :   Bildefil
             Bilde 1 som skal displayes
    im2 :   Bildefil
             Bilde 2 som skal displayes
    title1: Text
             En eventuell tittel over bilde 1
    title2: Text
             En eventuell tittel over bilde 2
    Returns
    -------
    plt.imshow -> Displayer 2 bilder ved siden av hverandre
    med en eventuell tittel
    """
    return (
        plt.figure(figsize=(20,10)),
        plt.subplot(131),
        plt.imshow(im1, plt.cm.gray),
        plt.title(title1),
        plt.axis('off'),
        
        plt.subplot(132),
        plt.imshow(im2, plt.cm.gray),
        plt.title(title2),
        plt.axis('off'),
        subplotAdjust(),
        plt.show(block=True)
        )
def threeImageSetup(im1, im2, im3, title1="", title2="", title3=""):
    """
    Setter opp et standard bildeoppsett for 2 bilder for å displaye bildene i subplots
    
    Parameters
    ----------
    im1 :   Bildefil
             Bilde 1 som skal displayes
    im2 :   Bildefil
             Bilde 2 som skal displayes
    im3 :   Bildefil
             Bilde 3 som skal displayes
    title1: Text
             En eventuell tittel over bilde 1
    title2: Text
             En eventuell tittel over bilde 2
    title3: Text
             En eventuell tittel over bilde 3
    Returns
    -------
    plt.imshow -> Displayer 3 bilder ved siden av hverandre
    med en eventuell tittel
    """
    return (
        plt.figure(figsize=(20,10)),
        plt.subplot(131),
        plt.imshow(im1, plt.cm.gray),
        plt.title(title1),
        plt.axis('off'),
        
        plt.subplot(132),
        plt.imshow(im2, plt.cm.gray),
        plt.title(title2),
        plt.axis('off'),
        subplotAdjust(),
      
        plt.subplot(133),
        plt.imshow(im3, plt.cm.gray),
        plt.title(title3),
        plt.axis('off'),
        plt.show(block=True),
        )

def view(original, ny1, BW, ny2, text):
    """
    Viser bildene ved siden av hverandre.
    
    Farget og glattet + gråtone og glattet

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
    twoImageSetup(original, ny1,"Originalbilde", text)
    twoImageSetup(BW, ny2, "Gråskala", text)
   
 
def singleView(image, gray=False):
    """
    Viser bildet

    Parameters
    ---------
    image : Bildefil
               Pathen til filen der original bildet befinner seg
    """
    plt.figure(figsize = (20,10))           # Setter størrelse på bilde
    if(gray):                               # Hvis gråtonebilde
        plt.imshow(image, plt.cm.gray)      # Viser gråtonebilde
    else:                                   # Fargebilde
        plt.imshow(image)                   # Viser fargebilde
    plt.axis('off')                         # Fjerner aksene
