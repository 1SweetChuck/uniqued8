```
                      X            
                     XXX           
                    X X X          
                   X  X  X         
                  X   X   X        
            F    X    X    X    G   
                X     X     X      
               X   D  X   A  X      
              X       X       X     
             X        X        X    
            XXXXXXXXXXXXXXXXXXXXX    
             X        X        X    
              X       X       X     
               X   C  X   B  X      
                X     X     X      
            E    X    X    X     H
                  X   X   X        
                   X  X  X         
                    X X X          
                     XXX           
                      X            
```

This Python3 script will take an eight digit input representing the faces
of a d8, and return the lowest equivalent eight digit output for the same 
d8.  For example the image above represents a d8 with four faces 
visible, and four faces hidden. The first four digits of the input would 
be starting from the face in the upper right quadrant, and moving around
the faces clockwise.  In this case ABCD. The next four digits would
start from the opposite face from the upper right quadrent, E, and again 
moving clockwise. In this case EFGH.  The full eight digit input
would be ABCDEFGH.

### Notation about rotations
For this code, there are three axis defined as follows:
* Omega is the axis looking straight down. One turn around Omega is a
90 degree turn clockwise, A moves to B, B moves to C, C moves to D,...
E moves to F, F moves to G, etc.
* Theta is the axis from right to left.  One turn around Theta is a 90
degree turn clockwise when viewed from the right:  A moves to G, G moves to H, H moves to B, B 
moves to A...
* Phi is the axis from bottom to top. One turn around Phi is a 90 degree
turn clockwise when viewed from the bottom: C moves to B, B moves to H, 
and so on.

The code works by "rotating" the die so that the 1 is in the A position,
and the face adjacent to 1, that has the smallest value, is moved to 
the B position.  From there the output is generated in the same way
as the input, by reading of the new values that are in the positions
for ABCDEFGH.
