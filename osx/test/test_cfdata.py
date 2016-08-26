##
# Copyright (c) 2010-2016 Apple Inc. All rights reserved.
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

from ..corefoundation import CFDataRef
import unittest
import tempfile


"""
CFDataRef tests.
"""


class CFDataRefTestCase(unittest.TestCase):
    """
    Tests for L{CFDataRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFDataRef.instanceTypeId} returns the right value.
        """

        data = CFDataRef.fromString("abc")
        self.assertEqual(data.instanceTypeId(), CFDataRef.typeId())

    def test_description(self):
        """
        Make sure L{CFDataRef.description} is the correct string.
        """

        data = CFDataRef.fromString("abc")
        self.assertTrue("CFData" in data.description())

    def test_to_from_string(self):
        """
        Make sure L{CFDataRef.fromString} and L{CFDataRef.toString} work properly.
        """

        data = CFDataRef.fromString("abc")
        self.assertEqual(data.toString(), "abc")

    def test_count(self):
        """
        Make sure L{CFDataRef.count} returns correct length.
        """

        data = CFDataRef.fromString("abc")
        self.assertEqual(data.count(), 3)

    def test_binary(self):
        """
        Make sure L{CFDataRef.fromString} and L{CFDataRef.toString} work properly.
        """

        tmp = tempfile.mktemp()
        with open(tmp, "w") as f:
            for i in range(100):
                f.write(chr(i))

        with open(tmp, "r") as f:
            binary = f.read()

        data = CFDataRef.fromString(binary)
        self.assertEqual(data.count(), 100)
        result = data.toString()
        self.assertEqual(len(result), 100)
        for i in range(100):
            self.assertEqual(result[i], chr(i))
