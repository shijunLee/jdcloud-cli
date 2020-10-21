# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

import unittest
import os
import json


class VqdTest(unittest.TestCase):

    def test_set_callback(self):
        cmd = """python ../../main.py vqd set-callback  --callback-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_callback(self):
        cmd = """python ../../main.py vqd query-callback """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_submit_vqd_task(self):
        cmd = """python ../../main.py vqd submit-vqd-task  --media '{"":""}' --template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_batch_submit_vqd_tasks(self):
        cmd = """python ../../main.py vqd batch-submit-vqd-tasks  --media-list '[{"":""}]' --template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_vqd_tasks(self):
        cmd = """python ../../main.py vqd list-vqd-tasks """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_vqd_task(self):
        cmd = """python ../../main.py vqd get-vqd-task  --task-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vqd_task(self):
        cmd = """python ../../main.py vqd delete-vqd-task  --task-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_vqd_task_result(self):
        cmd = """python ../../main.py vqd query-vqd-task-result  --task-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_batch_delete_vqd_tasks(self):
        cmd = """python ../../main.py vqd batch-delete-vqd-tasks """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_list_vqd_templates(self):
        cmd = """python ../../main.py vqd list-vqd-templates """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_vqd_template(self):
        cmd = """python ../../main.py vqd create-vqd-template  --template-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_vqd_template(self):
        cmd = """python ../../main.py vqd get-vqd-template  --template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_vqd_template(self):
        cmd = """python ../../main.py vqd update-vqd-template  --template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vqd_template(self):
        cmd = """python ../../main.py vqd delete-vqd-template  --template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

