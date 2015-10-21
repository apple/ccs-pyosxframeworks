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

from ..corefoundation import CFArrayRef, CFDataRef, CFDictionaryRef, CFStringRef
from ..utils import CFPropertyListRef
import os
import unittest

"""
CFPropertyListRef tests.
"""

class CFPropertyListRefTestCase(unittest.TestCase):
    """
    Tests for L{CFPropertyListRef}.
    """

    def test_readStringData(self):
        """
        Make sure L{CFPropertyListRef} can parse a string-only plist.
        """

        data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <string>Hello World!</string>
</plist>
"""
        dataref = CFDataRef.fromString(data)
        plist = CFPropertyListRef.createFromData(dataref)
        self.assertEqual(plist.instanceTypeId(), CFStringRef.typeId())
        self.assertEqual(plist.toString(), "Hello World!")


    def test_readArrayData(self):
        """
        Make sure L{CFPropertyListRef} can parse an array plist.
        """

        data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <array>
        <string>Hello World!</string>
        <string>Salve Mundi!</string>
    </array>
</plist>
"""
        dataref = CFDataRef.fromString(data)
        plist = CFPropertyListRef.createFromData(dataref)
        self.assertEqual(plist.instanceTypeId(), CFArrayRef.typeId())
        self.assertEqual(plist.count(), 2)
        items = plist.toList()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0], "Hello World!")
        self.assertEqual(items[1], "Salve Mundi!")


    def test_readDictionaryData(self):
        """
        Make sure L{CFPropertyListRef} can parse a dict plist.
        """

        data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>English</key>
        <string>Hello World!</string>
        <key>Latin</key>
        <string>Salve Mundi!</string>
    </dict>
</plist>
"""
        dataref = CFDataRef.fromString(data)
        plist = CFPropertyListRef.createFromData(dataref)
        self.assertEqual(plist.instanceTypeId(), CFDictionaryRef.typeId())
        self.assertEqual(plist.count(), 2)
        items = plist.toDict()
        self.assertEqual(len(items), 2)
        self.assertEqual(items["English"], "Hello World!")
        self.assertEqual(items["Latin"], "Salve Mundi!")


    dataDir = os.path.join(os.path.dirname(__file__), "data")

    def test_readDictionaryXMLFile(self):
        """
        Make sure L{CFPropertyListRef} can parse a XML plist read from a file.
        """

        data = open(os.path.join(self.dataDir, "xml_fmt.plist")).read()
        dataref = CFDataRef.fromString(data)
        plist = CFPropertyListRef.createFromData(dataref)
        self.assertEqual(plist.instanceTypeId(), CFDictionaryRef.typeId())
        self.assertEqual(plist.count(), 2)
        items = plist.toDict()
        self.assertEqual(len(items), 2)
        self.assertEqual(items["English"], "Hello World!")
        self.assertEqual(items["Latin"], "Salve Mundi!")


    def test_readDictionaryBinaryFile(self):
        """
        Make sure L{CFPropertyListRef} can parse a binary plist read from a file.
        """

        data = open(os.path.join(self.dataDir, "binary_fmt.plist")).read()
        dataref = CFDataRef.fromString(data)
        plist = CFPropertyListRef.createFromData(dataref)
        self.assertEqual(plist.instanceTypeId(), CFDictionaryRef.typeId())
        self.assertEqual(plist.count(), 2)
        items = plist.toDict()
        self.assertEqual(len(items), 2)
        self.assertEqual(items["English"], "Hello World!")
        self.assertEqual(items["Latin"], "Salve Mundi!")
