xData = [81, 83, 83, 83, 83, 82, 79, 77, 80, 83, 
  84, 85, 84, 90, 94, 94, 89, 85, 83, 75, 
  71, 63, 59, 60, 44, 37, 33, 21, 15, 12, 
  14, 19, 22, 27, 32, 35, 40, 41, 38, 37, 
  36, 36, 37, 43, 50, 59, 67, 71]

yData = [10, 17, 22, 27, 33, 41, 49, 53, 67, 76, 
  93, 103, 110, 112, 114, 118, 119, 118, 121, 121, 
  118, 119, 119, 122, 122, 118, 113, 108, 100, 92, 
  88, 90, 95, 99, 101, 80, 62, 56, 43, 32, 
  24, 19, 13, 16, 23, 22, 24, 20]

myFont = None
mag = 5.0

def setup():
  size(800, 800)

  global myFont
  myFont = loadFont("CenturySchoolbook-60.vlw") 
  textFont(myFont)
  noLoop()


def draw():
  background(253) 

  global mag, xData, yData
  nPoints = len(xData)

  pushMatrix() 
  scale(mag) 
  translate(23, 1) 
  fill(229) 
  stroke(0) 
  stroke(0) 
  strokeJoin(MITER) 
  strokeWeight(8.0/mag)

  perimeter = 0 
  beginShape()
  for i in range(nPoints):
    px = xData[i]
    py = yData[i]
    qx = xData[(i+1)%nPoints]
    qy = yData[(i+1)%nPoints]
    delta = dist(px, py, qx, qy) 
    perimeter += delta
    vertex(px, py)
  
  endShape(CLOSE)
  popMatrix() 


  fill(0) 
  textAlign(CENTER) 
  text("Perimeter = " + str(int(round(perimeter))) + " pixels", width/2, 730)
