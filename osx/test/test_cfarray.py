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

from ..corefoundation import CFArrayRef, CFStringRef
import gc
import unittest


"""
CFArrayRef tests.
"""

class CFArrayRefTestCase(unittest.TestCase):
    """
    Tests for L{CFArrayRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFArrayRef.instanceTypeId} returns the right value.
        """

        array = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertEqual(array.instanceTypeId(), CFArrayRef.typeId())


    def test_description(self):
        """
        Make sure L{CFArrayRef.description} is the correct string.
        """

        array = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertTrue("CFArray" in array.description(), msg=array.description())


    def test_retain(self):
        """
        Make sure L{CFArrayRef.retainCount} returns the correct value based on ownership.
        """

        array1 = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertEqual(array1.retainCount(), 1)
        array2 = CFArrayRef(array1.ref(), owned=False)
        self.assertEqual(array1.retainCount(), 2)
        self.assertEqual(array2.retainCount(), 2)
        del array1
        gc.collect()
        self.assertEqual(array2.retainCount(), 1)


    def test_to_from_list(self):
        """
        Make sure L{CFArrayRef.fromString} and L{CFArrayRef.toString} work properly.
        """

        array = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertEqual(array.toList(), ["abc", "def", ])


    def test_count(self):
        """
        Make sure L{CFArrayRef.count} returns the right number.
        """

        array = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertEqual(array.count(), 2)


    def test_valueAt(self):
        """
        Make sure L{CFArrayRef.valueAtIndex} returns the right number.
        """

        array = CFArrayRef.fromList((CFStringRef.fromString("abc"), CFStringRef.fromString("def"),))
        self.assertEqual(array.valueAtIndex(0), "abc")
        self.assertEqual(array.valueAtIndex(1), "def")
