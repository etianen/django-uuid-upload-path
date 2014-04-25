from __future__ import absolute_import, unicode_literals

import re
from unittest import TestCase

from uuid_upload_path.uuid import uuid
from uuid_upload_path.storage import upload_to_factory, upload_to


class TestCaseBase(TestCase):

    # HACK: Backport for Python 2.6.
    def assertRegexpMatches(self, value, regexp):
        self.assertTrue(re.match(regexp, value))

    # HACK: Backport for Python 2.6.
    def assertNotIn(self, value, container):
        self.assertFalse(value in container)



class UuidTest(TestCaseBase):

    # It's hard to test random data, but more iterations makes the tests
    # more robust.
    TEST_ITERATIONS = 1000

    def testUuidFormat(self):
        for _ in range(self.TEST_ITERATIONS):
            self.assertRegexpMatches(uuid(), r"^[a-zA-Z0-9\-_]{22}$")

    def testUuidUnique(self):
        generated_uuids = set()
        for _ in range(self.TEST_ITERATIONS):
            new_uuid = uuid()
            self.assertNotIn(new_uuid, generated_uuids)
            generated_uuids.add(new_uuid)


class TestModel(object):

    class _meta:
        app_label = "test"


class StorageTest(TestCaseBase):

    def testUploadToFactory(self):
        self.assertRegexpMatches(
            upload_to_factory("test")(object(), "test.txt"),
            r"^test/[a-zA-Z0-9\-_]{22}\.txt$"
        )

    def testUploadTo(self):
        self.assertRegexpMatches(
            upload_to(TestModel(), "test.txt"),
            r"^test/testmodel/[a-zA-Z0-9\-_]{22}\.txt$"
        )