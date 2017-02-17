"""
Created on 30-Jan-2015

@author: Asawari.Vaidya
"""

import certifi
from urllib3.connectionpool import HTTPSConnectionPool
from urllib3.util.timeout import Timeout


class Environment:

    ENV_TEST = None
    ENV_PROD = None

    def __init__(self, host_url, max_connections=10, pool_enable=True,
                 connection_timeout=30, read_timeout=30):
        
        self._host_url = host_url
        self._pool = HTTPSConnectionPool(host_url, 
                                         maxsize=max_connections, 
                                         block=pool_enable,
                                         timeout=Timeout(
                                                    connect=connection_timeout, 
                                                    read=read_timeout),
                                         retries=False,
                                         cert_reqs='CERT_REQUIRED',
                                         ca_certs=certifi.where())

    @classmethod
    def _get_env(cls, params_env):
        if params_env == 'TEST':
            if not Environment.ENV_TEST:
                # TODO both url addresses should be in some kind of config file, and not here
                Environment.ENV_TEST = Environment('api.test.paysafe.com')
            return Environment.ENV_TEST
        elif params_env == 'LIVE':
            if not Environment.ENV_TEST:
                Environment.ENV_PROD = Environment('api.paysafe.com')
            return Environment.ENV_PROD
        # TODO in case user enter wrong env, this should raise some nice error.
        raise Exception('env accepts only TEST or LIFE as valid parameters')
