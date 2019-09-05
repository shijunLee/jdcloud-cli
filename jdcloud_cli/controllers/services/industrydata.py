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


class IndustrydataController(BaseController):
    class Meta:
        label = 'industrydata'
        help = '产业数据服务API'
        description = '''
        industrydata cli 子命令，产业数据服务API。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/industry-data-service/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId',  required=False)),
            (['--region'], dict(help="""(string) 查询区域，比如某某省或某某市（可选区域以最终授权为准） """, dest='region',  required=True)),
            (['--industry'], dict(help="""(string) 查询行业，比如某个水果或者农作物（可选行业以最终授权为准） """, dest='industry',  required=True)),
            (['--start-date'], dict(help="""(string) 查询起始时间，格式如下：yyyy-MM-dd """, dest='startDate',  required=True)),
            (['--end-date'], dict(help="""(string) 查询结束时间，格式如下：yyyy-MM-dd """, dest='endDate',  required=True)),
            (['--first-index'], dict(help="""(string) 数据对应的第一级分析指标（可选一级指标以最终授权为准） """, dest='firstIndex',  required=True)),
            (['--second-index'], dict(help="""(string) 数据对应的第二级分析指标，如不填写，则默认把一级指标下的所有二级指标都查询出来（可选二级指标以最终授权为准） """, dest='secondIndex',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据区域、行业、一级指标、二级指标、起始时间等条件查询数据 ''',
        description='''
            根据区域、行业、一级指标、二级指标、起始时间等条件查询数据。

            示例: jdc industrydata get-large-screen-data  --region xxx --industry xxx --start-date xxx --end-date xxx --first-index xxx
        ''',
    )
    def get_large_screen_data(self):
        client_factory = ClientFactory('industrydata')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.industrydata.apis.GetLargeScreenDataRequest import GetLargeScreenDataRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetLargeScreenDataRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['get-large-screen-data',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('industrydata', self.app.pargs.api)
        skeleton.show()