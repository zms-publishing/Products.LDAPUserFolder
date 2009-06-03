##############################################################################
#
# Copyright (c) 2000-2009 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Tests for the LDAPDelegate class

$Id$
"""

import unittest


class TestSimple(unittest.TestCase):

    def _getTargetClass(self):
        from Products.LDAPUserFolder.LDAPDelegate import LDAPDelegate

        return LDAPDelegate

    def _makeOne(self, *args, **kw):
        klass = self._getTargetClass()

        return klass(*args, **kw)

        
def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(TestSimple),
        ))
