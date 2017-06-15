import unittest
import rover as r

""" Runs through a series of tests on the methods of the rover class """

class TestRoverCode(unittest.TestCase):

    def test_class_function(self):
      rov = r.rover(1,2,8,9,'E')
      self.assertEqual(rov.fac, [1,0])
      self.assertEqual(rov.loc, [1,2])
      self.assertEqual(rov.loc_history, [(1,2)])
      self.assertEqual(rov.limits, (8,9))
    
    def test_move_function(self):
      rov = r.rover(1,2,8,8,'E')
      rov.move_rover()
      self.assertEqual(rov.loc, [2,2])
      rov.move_rover()
      self.assertEqual(rov.loc, [3,2])
    
    def test_update_rotate_function(self):
      rov = r.rover(1,2,8,8,'E')
      self.assertEqual(rov.rot, 0)
      rov.update_rotate_rover('L')
      self.assertEqual(rov.rot, 90)
      rov.update_rotate_rover('L')
      self.assertEqual(rov.rot, 180)
      rov.update_rotate_rover('L')
      self.assertEqual(rov.rot, -90)
      rov.update_rotate_rover('R')
      self.assertEqual(rov.rot, -180)
      rov.update_rotate_rover('R')
      self.assertEqual(rov.rot, 90)
    
    def test_update_rotate_function(self):
      rov = r.rover(1,2,8,8,'E')
      rov.rot = 0
      rov.rotate_rover()
      self.assertEqual(rov.fac, [1,0])
      rov.rot = 90
      rov.rotate_rover()
      self.assertEqual(rov.fac, [0,1])
      rov.rot = -90
      rov.rotate_rover()
      self.assertEqual(rov.fac, [1,0])
      rov.rot = -180
      rov.rotate_rover()
      self.assertEqual(rov.fac, [-1,0])

    def test_move_sequence(self):
      #'MLMRRM' 
      rov = r.rover(1,1,8,8,'E')
      rov.move_rover() # M
      self.assertEqual(rov.loc, [2,1])
      
      rov.update_rotate_rover('L') # L
      rov.move_rover() # M
      self.assertEqual(rov.loc, [2,2])
      
      self.assertEqual(rov.loc_history, [(1,1),(2,1),(2,2)] )

      # Verify that we don't record duplicate points
      rov.update_rotate_rover('R') # R
      rov.update_rotate_rover('R') # R
      rov.move_rover() # M

      self.assertEqual(rov.loc_history, [(1,1),(2,1),(2,2)])
      self.assertEqual(rov.loc, [2,1] )

    def test_run_rover_command(self):
      
      rov = r.rover(1,1,8,8,'E')
      cmdset = 'MLMRRM'
      rov.run_rover_command(cmdset)
      self.assertEqual(rov.loc_history, [(1,1),(2,1),(2,2)])
      self.assertEqual(rov.loc, [2,1] )
     
      # Run the demo code
      rov = r.rover(1,2,8,8,'E')
      cmdset = 'MMLMRMMRRMML'
      rov.run_rover_command(cmdset)
      self.assertEqual(rov.loc, [3,3] )
      self.assertEqual(rov.get_facing_direction(), 'S')


if __name__ == '__main__':
    unittest.main()
#     self.assertEqual(fun(3), 4)
