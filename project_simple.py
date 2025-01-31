from p5 import *

def setup():
    size(800, 800)
    background(255)
    no_loop()

def draw():
    # Geometrische Formen
    fill(0)
    rect(100, 200, 400, 50)
    circle((400, 400), 150)

    # Typografie
    fill(0)
    text_size(32)
    text("ARMIN", (120, 250))
    text("HOFMANN", (130, 300))

    # Linien
    stroke(0)
    line((100, 100), (700, 700))
    line((700, 100), (100, 700))

if __name__ == "__main__":
    run()
