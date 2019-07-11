#import turtle

#tina=turtle.Turtle()
#tina.shape('turtle')
#tina.penup()


def check_longestgap(N):

    binx = str(bin(N)[2:])
    print(bin(N))
    print(binx)
    #print(binx.isdecimal())

    binx = binx.split('1')

    binx = binx.remove(binx[-1])
    print(binx)

    maxA = len(binx[0])
    maxA = 0
    lenlist = len(binx)
    count = 0

    for a in binx:
        if count > lenlist:
            if len(a) < maxA - 2:
                maxA = len(a)

    return maxA


yourinput=int(input("enter your int :"))

print(check_longestgap(yourinput))

