import numpy as np

# https://cglab.ca/~sander/misc/ConvexGeneration/convex.html
def make1vec(coord_min,coord_max,ngon):
    coords=np.random.randint( coord_min,coord_max, ngon )
    c_s = np.sort( coords )

    vecs=[]
    last0=c_s[0]
    last1=c_s[0]
    # Build 2 random chains of vectors, one goes "up", the other "down"
    for n in range(1,ngon-1):
        if np.random.randint(2):
            vecs += [c_s[n] - last0]
            last0 = c_s[n]
        else:
            vecs += [last1 - c_s[n]]
            last1 = c_s[n]

    vecs += [c_s[-1]-last0]
    vecs += [last1 - c_s[-1]]

    vecs = np.random.permutation(vecs)
    return vecs,c_s[0]

def gen_poly(ngon,maxx=32,maxy=32):
    xvals,x0=make1vec(0,maxx,ngon)
    yvals,y0=make1vec(0,maxy,ngon)
    coords=list( zip( xvals, yvals) )
    angles=[np.arctan2(coo[1],coo[0]) for coo in coords]

    np.argsort( angles )
    seglist=[[0,0]]
    for idx in np.argsort(angles):
            dx,dy=coords[idx]
            seglist = seglist + [[seglist[-1][0]+dx,seglist[-1][1]+dy]]

    seglist = np.array( seglist)
    seglist += np.array( np.array([x0,y0])-seglist.min(axis=0))
    return seglist
