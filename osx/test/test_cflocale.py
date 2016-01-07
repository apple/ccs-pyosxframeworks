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

from ..utils import CFLocaleRef
import unittest


"""
CFLocaleRef tests.
"""

class CFLocaleRefTestCase(unittest.TestCase):
    """
    Tests for L{CFLocaleRef}.
    """

    def test_typeid(self):
        """
        Make sure L{CFLocaleRef.instanceTypeId} returns the right value.
        """

        locale = CFLocaleRef.currentLocale()
        self.assertEqual(locale.instanceTypeId(), CFLocaleRef.typeId())


    def test_preferredLanguages(self):
        """
        Make sure L{CFLocaleRef.description} is the correct string.
        """

        langs = CFLocaleRef.preferredLanguages()
        self.assertTrue(len(langs) > 0)
        self.assertTrue(all([isinstance(lang, str) for lang in langs]))
