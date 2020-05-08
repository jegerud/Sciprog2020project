import matplotlib.pyplot as plt

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
    plt.figure(figsize=(16, 8))         # Setter størrelse på bildene
    plt.subplot(131)                    # Legger til subplot for bilde
    plt.imshow(original, plt.cm.gray)   # Viser bildet
    plt.title('Originalbilde')          # Legger til tittel
    plt.axis('off')                     # Fjerner aksene i figuren
    
    plt.subplot(132)                    # Legger til subplot for bilde
    plt.imshow(ny1, plt.cm.gray)        # Viser glattet bilde        
    plt.title(text)                     # Legger til tittel
    plt.axis('off')                     # Fjerner aksene i figuren
                                        # Gjør margene mindre
    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)
    
    plt.figure(figsize=(16, 8))         # Setter størrelse på bildene
    plt.subplot(131)                    # Legger til subplot for bilde
    plt.imshow(BW, plt.cm.gray)         # Viser gråtonebildet
    plt.title('Gråskala')               # Legger til tittel
    plt.axis('off')                     # Fjerner aksene i figuren

    plt.subplot(132)                    # Legger til subplot for bilde
    plt.imshow(ny2, plt.cm.gray)        # Viser bildet
    plt.title(text)                     # Legger til tittel
    plt.axis('off')                     # Fjerner aksene i figuren
                                        # Gjør margene mindre
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
    plt.figure(figsize = (20, 10))          # Setter størrelse på figur
    plt.subplot(131)                        # Legger til subplot
    if rgb:                                 # Hvis farger
        plt.imshow(original)                # Vis fargebilde
    else:                                   # Gråtonebilde
        plt.imshow(original, plt.cm.gray)   # Vis gråtonebilde
    plt.title('Originalbilde')              # Legger til tittel
    plt.axis('off')                         # Fjerner aksene
    
    plt.subplot(132)                        # Legger til subplot for bilde
    if rgb:                                 # Hvis farger
        plt.imshow(mask)                    # Vis bilde med maske
    else:                                   # Gråtonebilde 
        plt.imshow(mask, plt.cm.gray)       # Vis gråtonebilde med maske
    plt.title('Mask')                       # Setter tittel
    plt.axis('off')                         # Fjerner aksene
    
    plt.subplot(133)                        # Legger til subplot for bilde
    if rgb:                                 # Hvis farger
        plt.imshow(ny)                      # Viser inpaintet bilde
    else:                                   # Gråtonebilde
        plt.imshow(ny, plt.cm.gray)         # Viser inpaintet gråtonebilde
    plt.title(text)                         # Setter tittel
    plt.axis('off')                         # Fjerner aksene
                                            # Gjør margene mindre
    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)

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

def viewDemosaic(original, mosaic, ny, text):
    """
    Viser bildene ved siden av hverandre.
    
    Original, masken og inpainted

    Parameters
    ---------
    original : Bildefil
               Pathen til filen der original bildet befinner seg uten andvending
    mosaic   : Bildefil
               Mosaicen til bildet
    ny       : Bildefil
               Bildet som har blitt demosaicet
    text     : text
               Tittelen på bildet som er anvendt

    """
    plt.figure(figsize = (20, 10))          # Setter størrelse på figur
    plt.subplot(131)                        # Legger til subplot for bilde
    plt.imshow(original)                    # Viser originalbilde
    plt.title('Originalbilde')              # Tittel
    plt.axis('off')                         # Fjerner aksene
    
    plt.subplot(132)                        # Legger til subplot for bilde
    plt.imshow(mosaic, plt.cm.gray)         # Viser gråtonemosaic
    plt.title('Mosaic')                     # Tittel
    plt.axis('off')                         # Fjerner aksene
    
    plt.subplot(133)                        # Legger til subplot for bilde
    plt.imshow(ny)                          # Viser demosaiced bilde
    plt.title(text)                         # Tilhørende tittel
    plt.axis('off')                         # Fjerner aksene
                                            # Gjør margene mindre
    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,right=1)