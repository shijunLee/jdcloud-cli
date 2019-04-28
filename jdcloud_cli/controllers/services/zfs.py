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

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class ZfsController(BaseController):
    class Meta:
        label = 'zfs'
        help = 'CFS的API'
        description = '''
        zfs cli 子命令，CFS(Cloud-File-Service)的API包含CFS相关接口。。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) fileSystemId - 文件系统ID，精确匹配，支持多个; name - 文件系统名称，模糊匹配，支持单个; status - 文件系统状态，精确匹配，支持多个 FileSystem Status/creating、available、in-use;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' -   查询文件系统列表。; -   filters多个过滤条件之间是逻辑与(AND)，每个条件内部的多个取值是逻辑或(OR);  ''',
        description='''
            -   查询文件系统列表。; -   filters多个过滤条件之间是逻辑与(AND)，每个条件内部的多个取值是逻辑或(OR); 。

            示例: jdc zfs describe-file-systems 
        ''',
    )
    def describe_file_systems(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DescribeFileSystemsRequest import DescribeFileSystemsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeFileSystemsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--name'], dict(help="""(string) 文件系统名称 """, dest='name',  required=True)),
            (['--description'], dict(help="""(string) 文件系统描述 """, dest='description',  required=True)),
            (['--client-token'], dict(help="""(string) 幂等性参数(只支持数字、大小写字母，且不能超过64字符) """, dest='clientToken',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' - 创建一个新的文件系统，为这个文件系统分配一个Id;  ''',
        description='''
            - 创建一个新的文件系统，为这个文件系统分配一个Id; 。

            示例: jdc zfs create-file-system  --name xxx --description xxx --client-token xxx
        ''',
    )
    def create_file_system(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.CreateFileSystemRequest import CreateFileSystemRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateFileSystemRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--file-system-id'], dict(help="""(string) 文件系统ID """, dest='fileSystemId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询文件系统详情 ''',
        description='''
            查询文件系统详情。

            示例: jdc zfs describe-file-system  --file-system-id xxx
        ''',
    )
    def describe_file_system(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DescribeFileSystemRequest import DescribeFileSystemRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeFileSystemRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--file-system-id'], dict(help="""(string) 文件系统ID """, dest='fileSystemId',  required=True)),
            (['--name'], dict(help="""(string) 文件系统名称(参数规则：不可为空，只支持中文、数字、大小写字母、英文下划线“_”及中划线“-”，且不能超过32字符) """, dest='name',  required=False)),
            (['--description'], dict(help="""(string) 文件系统描述(参数规则：不能超过256字符) """, dest='description',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改文件系统属性(name 和 description 必须要指定一个) ''',
        description='''
            修改文件系统属性(name 和 description 必须要指定一个)。

            示例: jdc zfs modify-file-system-attribute  --file-system-id xxx
        ''',
    )
    def modify_file_system_attribute(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.ModifyFileSystemAttributeRequest import ModifyFileSystemAttributeRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ModifyFileSystemAttributeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--file-system-id'], dict(help="""(string) 文件系统ID """, dest='fileSystemId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' -   删除一个文件系统，一旦删除，该文件系统将不存在，也无法访问已删除的文件系统里的任何内容。;  ''',
        description='''
            -   删除一个文件系统，一旦删除，该文件系统将不存在，也无法访问已删除的文件系统里的任何内容。; 。

            示例: jdc zfs delete-file-system  --file-system-id xxx
        ''',
    )
    def delete_file_system(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DeleteFileSystemRequest import DeleteFileSystemRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteFileSystemRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) fileSystemId - 文件系统ID，精确匹配，支持多个; mountTargetId - 挂载目标ID，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' -   查询挂载目标列表。;  ''',
        description='''
            -   查询挂载目标列表。; 。

            示例: jdc zfs describe-mount-targets 
        ''',
    )
    def describe_mount_targets(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DescribeMountTargetsRequest import DescribeMountTargetsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMountTargetsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--file-system-id'], dict(help="""(string) 创建挂载目标的文件系统 """, dest='fileSystemId',  required=True)),
            (['--subnet-id'], dict(help="""(string) 子网id """, dest='subnetId',  required=True)),
            (['--vpc-id'], dict(help="""(string) vpcId """, dest='vpcId',  required=True)),
            (['--security-group-id'], dict(help="""(string) 安全组id """, dest='securityGroupId',  required=True)),
            (['--client-token'], dict(help="""(string) 幂等性参数(只支持数字、大小写字母，且不能超过64字符) """, dest='clientToken',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' - 为一个文件系统创建一个挂载目标。通过这个挂载目标,你可以挂载将一个文件系统挂载到主机实例上。; - 创建一个挂载目标，为这个挂载目标分配一个Id;  ''',
        description='''
            - 为一个文件系统创建一个挂载目标。通过这个挂载目标,你可以挂载将一个文件系统挂载到主机实例上。; - 创建一个挂载目标，为这个挂载目标分配一个Id; 。

            示例: jdc zfs create-mount-target  --file-system-id xxx --subnet-id xxx --vpc-id xxx --security-group-id xxx --client-token xxx
        ''',
    )
    def create_mount_target(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.CreateMountTargetRequest import CreateMountTargetRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateMountTargetRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--mount-target-id'], dict(help="""(string) 挂载目标ID """, dest='mountTargetId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询挂载目标详情 ''',
        description='''
            查询挂载目标详情。

            示例: jdc zfs describe-mount-target  --mount-target-id xxx
        ''',
    )
    def describe_mount_target(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DescribeMountTargetRequest import DescribeMountTargetRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMountTargetRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--mount-target-id'], dict(help="""(string) 挂载目标ID """, dest='mountTargetId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' -   删除挂载目标的同时会删除相关的网络接口。;  ''',
        description='''
            -   删除挂载目标的同时会删除相关的网络接口。; 。

            示例: jdc zfs delete-mount-target  --mount-target-id xxx
        ''',
    )
    def delete_mount_target(self):
        client_factory = ClientFactory('zfs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.zfs.apis.DeleteMountTargetRequest import DeleteMountTargetRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteMountTargetRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-file-systems','create-file-system','describe-file-system','modify-file-system-attribute','delete-file-system','describe-mount-targets','create-mount-target','describe-mount-target','delete-mount-target',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('zfs', self.app.pargs.api)
        skeleton.show()