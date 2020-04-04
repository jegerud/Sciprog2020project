import matplotlib.pyplot as plt

def viewBW(original, ny1, BW, ny2, text):
    """
    Viser bildene ved siden av hverandre.
    
    Original, svart-hvit og glattet

    Paramters
    ---------
    original : Bildefil
               Pathen til filen der original bildet befinner seg uten andvending
    BW       : Bildefil
               Pathen til filen der svart-hvit bildet befinner seg
    ny       : Bildefil
               Bildet som har blit anvendt
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
