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

from ..corefoundation import CFDictionaryRef, CFStringRef
import unittest


"""
CFDictionaryRef tests.
"""


class CFDictionaryRefTestCase(unittest.TestCase):
    """
    Tests for L{CFDictionaryRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFDictionaryRef.instanceTypeId} returns the right value.
        """

        cfdict = CFDictionaryRef.fromDict({
            CFStringRef.fromString("abc"): CFStringRef.fromString("1"),
            CFStringRef.fromString("def"): CFStringRef.fromString("2"),
        })
        self.assertEqual(cfdict.instanceTypeId(), CFDictionaryRef.typeId())

    def test_description(self):
        """
        Make sure L{CFDictionaryRef.description} is the correct string.
        """

        cfdict = CFDictionaryRef.fromDict({
            CFStringRef.fromString("abc"): CFStringRef.fromString("1"),
            CFStringRef.fromString("def"): CFStringRef.fromString("2"),
        })
        self.assertTrue("dict" in cfdict.description(), msg=cfdict.description())

    def test_to_from_dict(self):
        """
        Make sure L{CFDictionaryRef.fromDict} and L{CFDictionaryRef.toDict} work properly.
        """

        cfdict = CFDictionaryRef.fromDict({
            CFStringRef.fromString("abc"): CFStringRef.fromString("1"),
            CFStringRef.fromString("def"): CFStringRef.fromString("2"),
        })
        self.assertEqual(cfdict.toDict(), {"abc": "1", "def": "2", })

    def test_count(self):
        """
        Make sure L{CFDictionaryRef.count} returns the right number.
        """

        cfdict = CFDictionaryRef.fromDict({
            CFStringRef.fromString("abc"): CFStringRef.fromString("1"),
            CFStringRef.fromString("def"): CFStringRef.fromString("2"),
        })
        self.assertEqual(cfdict.count(), 2)
