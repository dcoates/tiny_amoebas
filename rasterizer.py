# Rasterize a single line segment into pixel buffer "buf"

# Direct implementation of "Differential digital analyzer" algorithm from Wikipedia:
# https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
def dda1(buf, start, end, max_step=None,do_print=False,do_flip=False):
    x0,y0=start
    x1,y1=end
    if do_flip: # Untested
        x0=buf.shape[0]-x0
        y0=buf.shape[1]-y0
        x1=buf.shape[0]-x1
        y1=buf.shape[1]-y1
    dx=x1-x0
    dy=y1-y0
    if abs(dx)>=abs(dy):
        step=abs(dx)
    else:
        step=abs(dy)
    if step!=0: # Usually:
        dx /= step
        dy /= step
    i=0
    x,y=x0,y0

    if do_print:
        print(dx,dy,step)
        print()

    prx=x0
    pry=y0

    if max_step is None:
        max_step=step
    while (i<max_step):
        # Current point
        iy=round(y)
        ix=round(x)

        if iy>=buf.shape[0]:
            iy=-(iy-buf.shape[0]+1) # Reflect (using negative idxs)
        if ix>=buf.shape[1]:
            ix=-(iy-buf.shape[1]) # Reflect
        buf[iy,ix]=1  # Turn on pixel

        # Next point
        y += dy
        x += dx
        i = i+1
