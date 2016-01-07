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

from .._corefoundation import lib as od
from ..opendirectory import ODSession, ODNode, ODRecord, ODQuery
import unittest


"""
OpenDirectory tests.
"""

class OpenDirectoryTestCase(unittest.TestCase):
    """
    Tests for OpenDirectory cffi wrappers.
    """

    def test_session(self):
        """
        Make sure L{ODSession} works.
        """

        session = ODSession.defaultSession()
        self.assertTrue(session is not None)


    def test_nodeNames(self):
        """
        Make sure L{ODSession.nodeNames} returns a set of nodes.
        """

        session = ODSession.defaultSession()
        names = session.nodeNames()
        self.assertTrue(isinstance(names, list))
        self.assertTrue("/Search" in names)


    def test_node(self):
        """
        Make sure L{ODNode} returns a valid node.
        """

        session = ODSession.defaultSession()
        node = ODNode(session, "/Search")
        self.assertTrue(node is not None)
        self.assertTrue(isinstance(node.details(["dsAttrTypeStandard:RecordType", ]), dict))


    def test_record(self):
        """
        Make sure L{ODRecord} returns a valid node.
        """

        session = ODSession.defaultSession()
        node = ODNode(session, "/Local/Default")
        record = node.record("dsRecTypeStandard:Users", "_www")
        self.assertTrue(isinstance(record, ODRecord))
        self.assertTrue(isinstance(record.details(["dsAttrTypeStandard:RecordType", ]), dict))


    def test_query(self):
        """
        Make sure L{ODQuery} returns records.
        """

        session = ODSession.defaultSession()
        node = ODNode(session, "/Local/Default")
        query = ODQuery.newQuery(
            node, ["dsRecTypeStandard:Users"], "dsAttrTypeStandard:RealName",
            od.kODMatchContains, "_",
            ["dsAttrTypeStandard:UniqueID"], 100
        )
        self.assertTrue(isinstance(query, ODQuery))

        results = query.results()
        self.assertTrue(isinstance(results, list))
        self.assertTrue(len(results) > 0)
        self.assertTrue(isinstance(results[0], ODRecord), msg=results)
