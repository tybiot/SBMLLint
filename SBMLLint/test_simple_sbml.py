"""
Tests for simple_sbml
"""
import unittest
import numpy as np
#import tesbml
import simple_sbml
#import tesedml


IGNORE_TEST = True
TEST_FILE = "chemotaxis.xml"
TEST_FILE = "BIOMD0000000001.xml"
NUM_REACTIONS = 111
NUM_PARAMETERS = 27
MAX_REACTANTS = 10


#############################
# Tests
#############################
class TestSimpleSBML(unittest.TestCase):

  def setUp(self):
    self.simple = simple_sbml.SimpleSBML(TEST_FILE)

  def testConstructor(self):
    self.simple.getStr()
    generator = simple_sbml.biomodelIterator(initial=1, final=1)
    idx, model = [x for x in generator][0]
    simple = simple_sbml.SimpleSBML(model)
    #
    self.assertEqual(len(simple.getReactions()), NUM_REACTIONS)
    self.assertEqual(len(self.simple.getReactions()), NUM_REACTIONS)
    for reaction in self.simple.getReactions():
      #self.assertTrue(isinstance(reaction, tesbml.Reaction))
      self.assertLessEqual(reaction.getNumReactants(), MAX_REACTANTS)
    self.assertEqual(len(self.simple.getParameters()), NUM_PARAMETERS)



class TestFunctions(unittest.TestCase):

  def testBiomodelIterator(self):
    if IGNORE_TEST:
      return
    FINAL = 2
    generator = simple_sbml.biomodelIterator(final=FINAL)
    for idx, model in generator:
      self.assertGreaterEqual(FINAL, idx)
      #self.assertTrue(isinstance(model, tesbml.libsbml.Model))

if __name__ == '__main__':
  unittest.main()
