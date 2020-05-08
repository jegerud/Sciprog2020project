import numpy as np
import matplotlib.pyplot as plt
import imageio
import Source.Eksplisitt as eks
import Source.ImageView as imv

def seamless(fra, til):
    """
    Kloner to bilder sømløst 

    Parameters
    ---------
    fra : image
        Bildet det skal hentes fra
    
    til : image
        Bildet det skal klones inn i

    Returns
        image:
        Det ferdig bildet bestående av 'til' med en partisjon fra 'fra'.
    -------
    """

    im_from=imageio.imread(fra)         # Leser inn bilde som det skal hentes fra
    im_to=imageio.imread(til)           # Leser inn bildet som det klones inn i

    im_from=im_from.astype(float)/255   # np.array verdier fra 0 til 1
    im_to=im_to.astype(float)/255
    xy0=(700,50)                        # hvor det skal klones inn 
    xy1=(350,500)                       # området hvor det hentes fra
    xlen=200                            # størrelsen på klonen
    ylen=500                            # 

    im_ed=np.zeros((xlen, ylen))
    im_ed=im_from[xy1[0]:xy1[0]+xlen, xy1[1]:xy1[1]+ylen] #henter ut delen av bildet
                                                          #som skal klones
    alpha=.25
    laplace1 = (im_ed[0:-2, 1:-1] +     # Laplace for likning 1
               im_ed[2:, 1:-1] +
               im_ed[1:-1, 0:-2] +
               im_ed[1:-1, 2:] -
               4 * im_ed[1:-1, 1:-1])

    for i in range(1000):               # Itererer diffusjonslikningen
        laplace2 = (im_ed[0:-2, 1:-1] + # Laplace for likning 2
                   im_ed[2:, 1:-1] +    
                   im_ed[1:-1, 0:-2] +
                   im_ed[1:-1, 2:] -
                   4 * im_ed[1:-1, 1:-1])
        im_ed[1:-1, 1:-1]+=alpha*(laplace2-laplace1)        # Løser diffusjonslikningen
    
        im_ed[ :,  0] = im_to[xy0[0]:xy0[0]+xlen, xy0[1]]   # dirichlet randbetingelser
        im_ed[ :, -1] = im_to[xy0[0]:xy0[0]+xlen, xy0[1]+ylen]
        im_ed[ 0,  :] = im_to[xy0[0],      xy0[1]:xy0[1]+ylen]
        im_ed[-1,  :] = im_to[xy0[0]+xlen, xy0[1]:xy0[1]+ylen]

    im_ed[im_ed<0]=0                    #klipper til lovlige verdier
    im_ed[im_ed>1]=1
    im_to[xy0[0]:xy0[0]+xlen, xy0[1]:xy0[1]+ylen] = im_ed
    
    return im_to