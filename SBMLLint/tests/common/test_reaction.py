"""
Tests for Reactions
"""
from SBMLLint.common import constants as cn
from SBMLLint.common.simple_sbml import SimpleSBML
from SBMLLint.common.molecule import Molecule, MoleculeStoichiometry
from SBMLLint.common.reaction import Reaction, REACTION_SEPARATOR
from SBMLLint.common import simple_sbml

import numpy as np
import os
import unittest


IGNORE_TEST = False
NUM_S1 = 2
NUM_S2 = 3


#############################
# Tests
#############################
class TestReaction(unittest.TestCase):

  def setUp(self):
    self.simple = SimpleSBML(cn.TEST_FILE)
    self.reactions = self.simple.reactions
    Reaction.initialize(self.simple)

  def testGetId(self):
    self.reaction = Reaction(self.reactions[2])
    identifier1 = self.reaction.getId()
    self.assertTrue(REACTION_SEPARATOR in identifier1)
    identifier2 = self.reaction.getId(is_include_kinetics=False)
    self.assertGreater(len(identifier1), len(identifier2))
    self.assertFalse(cn.KINETICS_SEPARATOR in identifier2)

  def testConstructor(self):
    if IGNORE_TEST:
      return
    reaction = Reaction(self.reactions[2])
    self.assertTrue(isinstance(reaction.reactants[0],
        MoleculeStoichiometry))
    self.assertTrue(isinstance(reaction.products[0],
        MoleculeStoichiometry))
    self.assertEqual(reaction.category, cn.REACTION_1_n)
    self.assertGreater(len(Molecule.molecules), 0)
    count = len(Reaction.reactions)
    reaction = Reaction(self.reactions[3])
    self.assertEqual(len(Reaction.reactions), count)

  # Test the stoichiometry
  def testConstructor2(self):
    if IGNORE_TEST:
      return
    simple = SimpleSBML(cn.TEST_FILE2)
    libsbml_reaction = simple.reactions[0]
    reaction = Reaction(libsbml_reaction)
    self.assertEqual(reaction.reactants[0].stoichiometry, NUM_S1)
    self.assertEqual(reaction.products[0].stoichiometry, NUM_S2)

  def testInitialize(self):
    if IGNORE_TEST:
      return
    self.assertEqual(len(Reaction.reactions), cn.NUM_REACTIONS)

  def testIsEqual(self):
    if IGNORE_TEST:
      return
    for reaction in Reaction.reactions[1:]:
      self.assertTrue(reaction.isEqual(reaction))
      self.assertFalse(reaction.isEqual(Reaction.reactions[0]))

  def testMakeIdentifier(self):
    if IGNORE_TEST:
      return
    for reaction in Reaction.reactions:
      parts = reaction.identifier.split('->')
      self.assertTrue(";" in parts[-1])  # Kinetics is last


if __name__ == '__main__':
  unittest.main()
