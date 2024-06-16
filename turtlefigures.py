
import math
import random
class TerminateFunc:
    def __init__(self, isRunning=False):
        self.isRunning = isRunning
     

def drawShape(pen, shapeIndex, n, l,t):
     
     # binary tree
     def tree(n, l):
          if n==0 or l<2 or not t.isRunning :
               return
          #endif
          pen.forward(l)
          pen.left(45)
          tree(n-1, l/2)
          pen.right(90)
          tree(n-1, l/2)
          pen.left(45)
          pen.backward(l)

     #end
     
# quadratic tree

     def dandelion(n,l):
          
          #termination
          if n==0 or l<2 or not t.isRunning:
               return
          pen.forward(l)
          pen.left(90)
          dandelion(n-1,l/2)
          pen.right(60)
          dandelion(n-1,l/2)
          pen.right(60)
          dandelion(n-1,l/2)
          pen.right(60)
          dandelion(n-1,l/2)
          pen.left(90)
          pen.backward(l)

#Fern 
     def fern(n,l):
          
          #termination
          if n==0 or l<2 or not t.isRunning :
               return
          pen.forward(0.3*l)
          pen.right(45)
          fern(n-1,l/2)
          pen.left(45)
          pen.forward(0.7*l)
          pen.left(30)
          fern(n-1,l/2)
          pen.right(30)
          pen.forward(l)
          pen.right(10)
          fern(n-1,0.8*l)
          pen.left(10)
          pen.backward(2*l)
          
     
     def koch(n,l):
            #termination
          if n==0 or l<2 or not t.isRunning :
               pen.forward(l)
               return
          koch(n-1,l/3)
          pen.left(60)
          koch(n-1,l/3)
          pen.right(120)
          koch(n-1,l/3)
          pen.left(60)
          koch(n-1,l/3)

     def antiFlake(n,l):
          for i in range(3):
               koch(n,l)
               pen.left(120)

     def flake(n,l):
          for i in range(3):
               koch(n,l)
               pen.right(120)


     def triangleGasket(n,l):
          if n==0 or l<2 or not t.isRunning:
               for i in range(3):
                    pen.forward(l)
                    pen.left(120)
               return
          for i in range(3):
               triangleGasket(n-1,l/2)
               pen.forward(l)
               pen.left(120)
          
          
     def squareGasket(n,l):
          if(n==0 or l <2 or not t.isRunning):
               for i in  range(4):
                    pen.forward(l)
                    pen.left(90)
               return
          for j in range(4):
               squareGasket(n-1,l/3)
               pen.forward(l)
               pen.left(90)
     def nineSquares(n,l):
          if(n==0 or l<2 or not t.isRunning):
               for i in  range(4):
                    pen.forward(l)
                    pen.left(90)
               return
          for i in  range(4):
               nineSquares(n-1,l/3); pen.forward(l/3);
               nineSquares(n-1,l/3); pen.forward(l/3);
               pen.forward(l/3); pen.left(90);
               
     
               
               
     def hexagons(n,l):
          if(n==0 or l<2 or not t.isRunning):
               for i in range(6):
                    pen.forward(l)
                    pen.left(60)
               
               return
          for j in range(6):
               hexagons(n-1,l/3)
               pen.forward(l)
               pen.left(60)
     def twoCircles(n,r):
          if(n==0 or r<2 or not t.isRunning):
               pen.circle(r)
               return
          twoCircles(n-1,r)
          twoCircles(n-1,r/2)
          pen.up()
          pen.left(90)
          pen.forward(2*r)
          pen.left(90)
          
          pen.down()
          twoCircles(n-1,r/2)
          pen.up()
          pen.left(90)
          pen.forward(2*r)
          pen.left(90)
          pen.down()
          
       
   
          

     def threeCircles(n,r):
           if(n==0 or r<2 or not t.isRunning):
               pen.circle(r)
               return
           threeCircles(n-1,r)
           threeCircles(n-1,(3*r/(2*math.sqrt(3)+3)))
           pen.up()
           pen.left(90)
           pen.forward((3*r/(2*math.sqrt(3)+3))+((3*math.sqrt(3)*r)/(2*math.sqrt(3)+3)))
           pen.down()
           threeCircles(n-1,(3*r/(2*math.sqrt(3)+3)))
           pen.right(180)
           threeCircles(n-1,(3*r/(2*math.sqrt(3)+3)))
           pen.up()
           pen.forward((3*r/(2*math.sqrt(3)+3))+((3*math.sqrt(3)*r)/(2*math.sqrt(3)+3)))
           pen.left(90)
           pen.down()
     
     def fourCircles(n,r):
          if(n==0 or r<2 or not t.isRunning):
               pen.circle(r)
               return
          fourCircles(n-1,r)
          fourCircles(n-1,r/(math.sqrt(2)+1))
          pen.left(90)
          pen.up()
          pen.forward(2*r)
          pen.left(90)
          pen.down()
          fourCircles(n-1,r/(math.sqrt(2)+1))
          pen.left(90)
          pen.up()
          pen.forward(r)
          pen.right(90)
          pen.forward(r)
          pen.left(90)
          pen.down()
          fourCircles(n-1,r/(math.sqrt(2)+1))
          pen.left(90)
          pen.up()
          pen.forward(2*r)
          pen.down()
          pen.left(90)
          fourCircles(n-1,r/(math.sqrt(2)+1))
          pen.up()
          pen.left(90)
          pen.forward(r)
          pen.left(90)
          pen.forward(r)
          pen.left(90)
          pen.down()

   
     def custom1(n,r):
         if(n==0 or r<2 or not t.isRunning):
             pen.circle(r)
             return
         custom1(n-1,r)
         custom1(n-1,r/3)
         for i in range(2):
             
             pen.up()
             pen.left(90)
             pen.forward(2*r/3)
             pen.right(90)
             pen.down()
             custom1(n-1,r/3)
         for i in range(6):   
             pen.right(90)
             pen.up()
             pen.forward(r/3)
             pen.left(120)
             pen.forward(r/3)
             pen.right(90)
             pen.down()
             custom1(n-1,r/3)
         pen.up()
         pen.right(90)
         pen.forward(r/3)
         pen.left(90)
        
         for i in range(6): 
             pen.forward((r/3)+(2*r/3))
             pen.left(90)
             pen.down()
             custom1(n-1,r/9)
             pen.up()
             pen.right(90)
             pen.backward((r/3)+(2*r/3))
             pen.left(60)
             
         for i in range(6): 
             pen.forward((r/3))
             pen.right(90)
             pen.down()
             custom1(n-1,r/18)
             pen.up()
             pen.left(90)
             pen.backward((r/3))
             pen.right(60)
         pen.up()
         pen.right(90)
         pen.forward(r)
         pen.left(90)
         pen.down()
         

         

     def custom2(n,r):
         if(n==0 or r<2 or not t.isRunning):
             for i in range(6):
                     pen.forward(r)
                     pen.left(60)
             pen.left(60)
             pen.forward(r)
             pen.right(60)
             pen.forward(r)
             pen.backward(r)
             pen.left(120)
             pen.forward(r)
             pen.up()
             pen.left(120)
             pen.forward(r)
             pen.left(60)
             pen.forward(r)
             pen.left(60)
             pen.down()
             return
         custom2(n-1,r)
         pen.right(180)
         for j in range(6):
             custom2(n-1,r/2)
             pen.backward(r)
             pen.left(60)
             
         pen.left(180)

          
     def custom3(n,r):
          if(n==0 or r<2 or not t.isRunning):
               threeCircles(1,r)
               return
          for i in range(6):
               custom3(n-1,r/2)
               pen.color(random.random(),random.random(),random.random())
               pen.up()
               pen.left(90)
               pen.forward(r)
               pen.left(90)
               pen.down()
               custom3(n-1,r/2)
               pen.left(90)
               pen.up()
               pen.forward(r)
               pen.left(90)
               pen.left(60)
               pen.down()
               

     def custom4(n,r):
         
          if(n==0 or r<2 or not t.isRunning):
               pen.left(90)
               pen.forward(r)
               
               fern(10,r/4)
              
               pen.left(180)
               
               fern(10,r/4)
               pen.left(90)
               fern(10,r/4)
               pen.left(180)

               fern(10,r/4)
               return
          for i in range(6):
               custom4(n-1,r/2)
               pen.up()
               pen.forward(r)
               pen.left(60)
               pen.forward(r/2)
               pen.down()        

         
          

     match shapeIndex:
          case 0:
               tree(n,l);
          case 1:
               dandelion(n,l);
          case 2:
               fern(n,l)
          case 3:
               koch(n,l)
          case 4:
               antiFlake(n,l)
          case 5:
               flake(n,l)
          case 6:
               triangleGasket(n,l)
          case 7:
               squareGasket(n,l)
          case 8:
               nineSquares(n,l)
          case 9:
               hexagons(n,l)
          case 10:
               twoCircles(n,l)
          case 11:
               threeCircles(n,l)
          case 12:
               fourCircles(n,l)
          case 13:
               custom1(n,l)
          case 14:
               custom2(n,l)
          case 15:
               custom3(n,l)
          case 16:
               custom4(n,l)
              
          
          case _:
               return
     
class FractalFigure:
    def __init__(self, name, description):
        self.name = name
        self.description = description

fractal_list=[FractalFigure("Binary Tree","A binary tree is a tree-type fractal which is created by recursively travelling forward and turning left by 45 degrees"),
              FractalFigure("Dandelion","This is a fractal in the shape of a dandelion"),
              FractalFigure("Fern","This is a fractal in the shape of a fern"),
              FractalFigure("Koch","This is a Koch curve which can be used to draw a snow flake"),
              FractalFigure("Anti Flake","This is a fractal figure which uses Koch curve to form a anti flake"),
              FractalFigure("Flake","This is a fractal figure which uses Koch curve to form a snow flake"),
              FractalFigure("Triangle Gasket","The Triangle Gasket, also known as the Sierpinski Triangle, is formed by recursively subdividing an equilateral triangle into smaller triangles, with each iteration creating more intricate and detailed patterns."),
              FractalFigure("Square Gasket","This fractal consists of a larger square which encloses 4 smaller squares that are quarter the size of the larger square "),
              FractalFigure("Nine Squares","This also known as the Menger Sponge, is a three-dimensional fractal. It's constructed by repeatedly removing smaller cubes from a larger cube in a self-similar pattern. The result is a highly porous, sponge-like structure with intricate, repeating patterns at multiple scales."),
              FractalFigure("Hexagons","This fractal consists of a larger hexagon which encloses 6 smaller hexagons that are quarter the size of the larger hexagon "),
              FractalFigure("Two Circles","This structure is a fractal composed of a larger circle enclosing two smaller circles. These smaller circles are half the size of the larger one and are positioned in a way that they touch each other and the surrounding larger circle."),
               FractalFigure("Three Circles","This structure is a fractal composed of a larger circle enclosing three smaller circles. These smaller circles are positioned in a way that they touch each other and the surrounding larger circle."),
              FractalFigure("Four Circles","This structure is a fractal composed of a larger circle enclosing four smaller circles. These smaller circles are positioned in a way that they touch each other and the surrounding larger circle."),
              FractalFigure("Custom1","This forms a fractal pattern featuring a larger circle that encompasses five smaller circles. These smaller circles are a quarter of the size of the larger one. Additionally, there are five more circles that are 1/9th the size of the larger circle, as well as another five circles that are 1/18th the size of the larger circle."),
              FractalFigure("Custom2","This design is a fractal consisting of a central hexagon surrounded by smaller hexagons, each touching one of the larger hexagon's edges. The alternate edges of the hexagons converge at the center, creating a visual impression of a cube. "),
              FractalFigure("Custom3","This fractal figure consists of 2 sets of three circle figure which are drawn at an angle so that it resembles a flower within a circle. This pattern is then repeated iteratively to form a hexagon. This is a slow running fractal, hence it is recommended to use smaller order such as 1, 2, 3. This is programmed to ddraw circles in random colors"),
              FractalFigure("Custom4","This figure consists of 4 ferns that are 90 degrees to each other. This simple structure will recursively build up to form a hexagon for higher order. This is a slow running fractal, hence it is recommended to use smaller order such as 1, 2, 3")]
