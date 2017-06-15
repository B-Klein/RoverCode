#!/usr/bin/python -tt
# Benjamin Klein 2017

import sys
import math

""" 
Code to work out, given an initial location (x,y) and a set of unit move M and 90 degree
left L and right R rotation commands where a rover will end up. A grid is given and the
Rover cannot move beyond this. 

small app for Next45
"""

class rover:
  """ Represents a Mars Rover 
    fields:
    .loc - current location [x,y] (int)
    .limits - limits of the current grid (x,y) (int)
    .loc_history - unique history of where the rover has been [(x,y),(x,... ] (int)
    .fac - xy unit vector directed where the rover is facing [x,y] (int)
    .rot - current required rotation in degrees (int)
  """

  def __init__(self, start_x, start_y, limit_x, limit_y, facing):
    try:
      self.loc = [int(start_x),int(start_y)]
      self.limits = (int(limit_x),int(limit_y))
    except:
      sys.stderr.write('Invalid data format')
      sys.exit(1)

    # Perform some basic checks
    if int(start_x) <= 0 or int(start_y) <= 0 or int(limit_x) <= 0 or int(limit_y) <= 0 :
      sys.stderr.write('All values must be positive')
      sys.exit(1)
    if int(start_x) > int(limit_x) or int(start_y) > int(limit_y) :
      sys.stderr.write('Current location violates limits')
      sys.exit(1)

    # history of where the rover has been, stored as an array of tuples, not strictly
    # neccesary but aides in testing the code
    self.loc_history = [(int(start_x),int(start_y))]

    if facing == 'E':
      self.fac = [1,0]
    elif facing == 'W':
      self.fac = [-1,0]
    elif facing == 'N':
      self.fac = [0,1]
    elif facing == 'S':
      self.fac = [0,-1]
    else:
      sys.stderr.write('Invalid direction')
      sys.exit(1)
    # set the original rotation
    self.rot = 0 


  def move_rover(self):
    """moves the rover one unit in current facing direction"""
    # check if we need to first rotate
    if self.rot:
      self.rotate_rover()
    
    # peform the rotation
    self.loc = [self.loc[i] + self.fac[i] for i in range(len(self.loc))]

    # check if we have moved beyond our limits
    if self.loc[0] <= 0 or self.loc[1] <= 0 or self.loc[0] > self.limits[0] or self.loc[1] > self.limits[1]:
      sys.stderr.write('Moved beyond limits') 
      sys.exit(1)

    # Add the current point to the visited points, without duplication
    if (self.loc[0],self.loc[1]) not in self.loc_history:
      self.loc_history.append((self.loc[0],self.loc[1]))

  def rotate_rover(self):
    " rotates the rover by it's current rotation variable and resets it to 0"
    # using 2D matrix rotation
    xp = self.fac[0]*math.cos(math.radians(self.rot)) - self.fac[1]*math.sin(math.radians(self.rot))
    yp = self.fac[0]*math.sin(math.radians(self.rot)) + self.fac[1]*math.cos(math.radians(self.rot))
    self.fac=[int(xp),int(yp)]
    self.rot = 0


  def update_rotate_rover(self,rot):
    """adds a left or right rotation to the current rotation variable, and maps it to 0-180, NB doesn't rotate the rover"""
    if rot == 'L':
      self.rot+=90
    elif rot == 'R':
      self.rot-=90
    else:
      sys.stderr.write('Invalid rotation')
      sys.exit(1)
    # Check if we have over-rotated map back to 
    n = abs(self.rot/90)
    if abs(self.rot) > 180:
      self.rot = -1 * self.rot/n 

  def run_rover_command(self,cmdset):
    """ runs a set of rover commands in order """
    if cmdset == None: 
      return
    for cmd in cmdset:
      if cmd == 'M':
        self.move_rover() 
      elif cmd == 'L' or cmd == 'R':
        self.update_rotate_rover(cmd) # R
      else:
        sys.stderr.write('Invalid command given to Rover')
        sys.exit(1)
    # update the rotation and we are done
    self.rotate_rover()


  def get_facing_direction(self):
    """ gets which way the rover is facing in NESW map co-ordinates"""
    if self.fac == [1,0]:
      return 'E'
    elif self.fac == [-1,0]:
      return 'W'
    elif self.fac == [0,1]:
      return 'N'
    elif self.fac == [0,-1]:
      return 'S'
    else:
      return None


# Define a main() function that prints the final rover location
def main():
  """takes in a list of rover commands and prints out the final location
  usage: python rover cmd facing start_x start_y grid_x grid_y 
  example: rover MMLMRM E 1 2 8 8 """

  if len(sys.argv) == 7:
    rov = rover(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[2])
    rov.run_rover_command(sys.argv[1])
    print 'Final location: ' + str(rov.loc) + ' ' + rov.get_facing_direction()
  else:
    print 'usage: python cmd facing start_x start_y grid_x grid_y \nexample: rover MMLMRM E 1 2 8 8 '

  # This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
