# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def computeMandelbrot( xwidth, yheight, max_interactions ):
    # c = (a, b) = c[0], c[1]
    nPixels = xwidth*yheight
    k,l = 0, 0
    percent = 0
    Im = [ [ 0 for j in range(xwidth) ] for i in range(yheight) ]
    a, b, c, d = -2, 1.5, -2.0, 2.0
    
    # Factor to Scale and scaling  ---
    alfa = float(xwidth)/float(yheight)
    if alfa < 1: # xwidth < yheight (image sizes)
        c, d = alfa*c, alfa*d
    # xwidth > yheight
    else: 
        a, b = alfa*a, alfa*b
    # ----
    #a, b, c, d = alfa*a, alfa*b, alfa*c, alfa*d
    
    x, y = 0, 0
    
    
    delta_x = (b - a)/xwidth
    delta_y = (d - c)/yheight
    
    x_j = 0
    y_i = 0
    xtemp = 0
    count = 0
    
    import math
    color = lambda n: n*math.sin(n) + n*math.cos(n) + n**2
    
    #  Values color out interval [0, 255]
    def centralizedn(n):
        # n in range value [0, 255]
        if n < 0:
            return 0
        elif n > 255:
            return 255
        return n
    
    for i in range(yheight):
        k = k + 1
        y_i = i*delta_y + c
        
        for j in range(xwidth):
            l = l + 1
            x_j = j*delta_x + a
            print('Percent calculated...', 100.0*( (k+l)/nPixels), ' %')
            
            
            x, y = 0, 0
            count = 0
            
            while count < max_interactions:
                if x*x + y*y >= 4:
                    #print('escape')
                    Im[i][j] = 255 # White color to point out Mandelbrot set. Pixeis brancos indincam pontos fora do conjunto Mandelbrot.
                    #Im[i][j] = centralizedn( int(  color(count) ) )
                    break
                
                xtemp = x
                x = x*x - y*y + x_j
                y = 2*xtemp*y + y_i
                count = count + 1
            
    return Im

W = 800
H = 600

M = computeMandelbrot(W, H, 200)


with open("/home/user/image.ppm", 'w') as fl:
    fl.write(f'P2\n{W} {H}\n255\n')
    for i in range(H):
        for j in range(W):
            fl.write(str( M[i][j] )+'\n' ) 
print(M)
            
        