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


class ResourcetagController(BaseController):
    class Meta:
        label = 'resourcetag'
        help = 'Resource-Tag API'
        description = '''
        resourcetag cli 子命令，资源标签相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--resource-vo'], dict(help="""(resourceReqVo) 资源标签参数对象 """, dest='resourceVo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获得资源与对应标签列表详情，不含资源名称和可用区。<br/>; 注意查询cdn的资源时url中regionId必须指定为cn-all。<br/>; 该接口目前不支持分页功能。;  ''',
        description='''
            获得资源与对应标签列表详情，不含资源名称和可用区。<br/>; 注意查询cdn的资源时url中regionId必须指定为cn-all。<br/>; 该接口目前不支持分页功能。; 。

            示例: jdc resourcetag describe-resources  --resource-vo '{"":""}'
        ''',
    )
    def describe_resources(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.DescribeResourcesRequest import DescribeResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--tag-keys-vo'], dict(help="""(tagsReqVo) 标签参数 """, dest='tagKeysVo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取资源标签。<br/>; 注意查询cdn资源的标签时url中regionId必须指定为cn-all。<br/>; 注意查询不限制地域时url中regionId必须指定为all-region。;  ''',
        description='''
            获取资源标签。<br/>; 注意查询cdn资源的标签时url中regionId必须指定为cn-all。<br/>; 注意查询不限制地域时url中regionId必须指定为all-region。; 。

            示例: jdc resourcetag describe-tags  --tag-keys-vo '{"":""}'
        ''',
    )
    def describe_tags(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.DescribeTagsRequest import DescribeTagsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeTagsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--tag-keys-vo'], dict(help="""(tagKeysReqVo) 标签键参数 """, dest='tagKeysVo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取标签键 ''',
        description='''
            获取标签键。

            示例: jdc resourcetag describe-keys  --tag-keys-vo '{"":""}'
        ''',
    )
    def describe_keys(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.DescribeKeysRequest import DescribeKeysRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeKeysRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--tag-values-vo'], dict(help="""(tagValuesReqVo) 标签值参数 """, dest='tagValuesVo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取标签值 ''',
        description='''
            获取标签值。

            示例: jdc resourcetag describe-values  --tag-values-vo '{"":""}'
        ''',
    )
    def describe_values(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.DescribeValuesRequest import DescribeValuesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeValuesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--tag-resources'], dict(help="""(tagResourcesReqVo) 绑定标签参数 """, dest='tagResources',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 资源标签绑定。<br/>; 注意cdn资源绑定标签时url中regionId必须指定为cn-all。;  ''',
        description='''
            资源标签绑定。<br/>; 注意cdn资源绑定标签时url中regionId必须指定为cn-all。; 。

            示例: jdc resourcetag tag-resources  --tag-resources '{"":""}'
        ''',
    )
    def tag_resources(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.TagResourcesRequest import TagResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = TagResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--un-tag-resources'], dict(help="""(unTagResourcesReqVo) 解绑标签参数 """, dest='unTagResources',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 资源标签解绑。<br/>; 注意cdn资源解绑标签时url中regionId必须指定为cn-all。;  ''',
        description='''
            资源标签解绑。<br/>; 注意cdn资源解绑标签时url中regionId必须指定为cn-all。; 。

            示例: jdc resourcetag un-tag-resources  --un-tag-resources '{"":""}'
        ''',
    )
    def un_tag_resources(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.UnTagResourcesRequest import UnTagResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UnTagResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--query-resource'], dict(help="""(queryResourceReqVo) 查找资源id的参数对象 """, dest='queryResource',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据标签查找资源。 <br/>; 若要查找cdn产品线的资源则url中的regionId必须指定为cn-all。;  ''',
        description='''
            根据标签查找资源。 <br/>; 若要查找cdn产品线的资源则url中的regionId必须指定为cn-all。; 。

            示例: jdc resourcetag query-resource  --query-resource '{"":""}'
        ''',
    )
    def query_resource(self):
        client_factory = ClientFactory('resourcetag')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.resourcetag.apis.QueryResourceRequest import QueryResourceRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryResourceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-resources','describe-tags','describe-keys','describe-values','tag-resources','un-tag-resources','query-resource',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('resourcetag', self.app.pargs.api)
        skeleton.show()
