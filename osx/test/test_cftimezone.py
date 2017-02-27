##
# Copyright (c) 2010-2017 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from ..utils import CFTimeZoneRef
import unittest


"""
CFTimeZoneRef tests.
"""


class CFTimeZoneRefTestCase(unittest.TestCase):
    """
    Tests for L{CFTimeZoneRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFTimeZoneRef.instanceTypeId} returns the right value.
        """

        tz = CFTimeZoneRef.defaultTimeZone()
        self.assertEqual(tz.instanceTypeId(), CFTimeZoneRef.typeId())

    def test_name(self):
        """
        Make sure L{CFTimeZoneRef.description} is the correct string.
        """

        tz = CFTimeZoneRef.defaultTimeZone()
        name = tz.name()
        self.assertTrue(isinstance(name, str))
        self.assertEqual(name, CFTimeZoneRef.defaultTimeZoneName())
