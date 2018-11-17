import turtle

import math


####one
wn=turtle.Screen()
turtle.delay(1)


####two
sun=turtle.Turtle()
sun.color("yellow")

sun.shape("circle")

mercury=turtle.Turtle()
mercury.shape("circle")
mercury.color("blue")

venus=turtle.Turtle()
venus.shape("circle")
venus.color("green")

mars=turtle.Turtle()
mars.shape("circle")
mars.color("red")

jupiter=turtle.Turtle()
jupiter.shape("circle")
jupiter.color("black")

saturn=turtle.Turtle()
saturn.shape("circle")
saturn.color("orange")

earth=turtle.Turtle()
earth.shape("circle")
earth.color("sea green")



####three
mercury_a=23
mercury_b=20

venus_a=59
venus_b=51

mars_a=117
mars_b=106

jupiter_a=259
jupiter_b=254

saturn_a=377
saturn_b=360

earth_a=80
earth_b=77


####four
earth.up()
earth.fd(earth_a)
earth.pd()

saturn.up()
saturn.fd(saturn_a)
saturn.pd()

jupiter.up()
jupiter.fd(jupiter_a)
jupiter.pd()

mars.up()
mars.fd(mars_a)
mars.pd()

venus.up()
venus.fd(venus_a)
venus.pd()

mercury.up()
mercury.fd(mercury_a)
mercury.pd()



####five
mercury.speed(0)
venus.speed(10)
earth.speed(6)
mars.speed(3)
jupiter.speed(1)



####six
for c in range (10000):
    mercury.goto(mercury_a*(math.cos(math.radians(c))),mercury_b*(math.sin(math.radians(c))))
    venus.goto(venus_a*(math.cos(math.radians(c/2))),venus_b*(math.sin(math.radians(c/2))))
    mars.goto(mars_a*(math.cos(math.radians(c/5))),mars_b*(math.sin(math.radians(c/5))))
    jupiter.goto(jupiter_a*(math.cos(math.radians(c/10))),jupiter_b*(math.sin(math.radians(c/10))))
    saturn.goto(saturn_a*(math.cos(math.radians(c/12))),saturn_b*(math.sin(math.radians(c/12))))
    earth.goto(earth_a*(math.cos(math.radians(c/4))),earth_b*(math.sin(math.radians(c/4))))
