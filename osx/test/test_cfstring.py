##
# Copyright (c) 2010-2015 Apple Inc. All rights reserved.
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

from ..corefoundation import CFStringRef
import gc
import unittest


"""
CFStringRef tests.
"""

class CFStringRefTestCase(unittest.TestCase):
    """
    Tests for L{CFStringRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFStringRef.instanceTypeId} returns the right value.
        """

        str = CFStringRef.fromString("abc")
        self.assertEqual(str.instanceTypeId(), CFStringRef.typeId())


    def test_description(self):
        """
        Make sure L{CFStringRef.description} is the correct string.
        """

        str = CFStringRef.fromString("abc")
        self.assertTrue("CFString" in str.description())


    def test_retain(self):
        """
        Make sure L{CFStringRef.retainCount} returns the correct value based on ownership.
        """

        str1 = CFStringRef.fromString("abc")
        self.assertEqual(str1.retainCount(), 1)

        # In this case copy actually uses the same original object but bumps the retain count
        str2 = str1.copy()
        self.assertEqual(str1.retainCount(), 2)
        self.assertEqual(str2.retainCount(), 2)
        del str1
        gc.collect()
        self.assertEqual(str2.retainCount(), 1)

        str3 = CFStringRef.fromString("def")
        self.assertEqual(str3.retainCount(), 1)
        str4 = CFStringRef(str3.ref(), owned=False)
        self.assertEqual(str3.retainCount(), 2)
        self.assertEqual(str4.retainCount(), 2)
        del str3
        gc.collect()
        self.assertEqual(str4.retainCount(), 1)


    def test_to_from_string(self):
        """
        Make sure L{CFStringRef.fromString} and L{CFStringRef.toString} work properly.
        """

        str = CFStringRef.fromString("abc")
        self.assertEqual(str.toString(), "abc")


    def test_copy(self):
        """
        Make sure L{CFStringRef.copy} properly copies a string.
        """

        str = CFStringRef.fromString("abc")
        str2 = str.copy()
        self.assertEqual(str2.toString(), "abc")
