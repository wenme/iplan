# -*- coding: utf-8 -*-

import oss2
from itertools import islice

OSS_HOST = 'oss-cn-qingdao.aliyuncs.com'
OSS_AK = 'e2tnfzYPdVcaDxqz'
OSS_SK = 'aTWGvbk3icXvxdRl9ogjQHkg0vjFA8'
BUCKET = 'iplan'

def sign(object_key):
    auth = oss2.Auth(OSS_AK, OSS_SK)
    bucket = oss2.Bucket(auth, OSS_HOST, BUCKET)
    return bucket.sign_url('GET', object_key, 3600)
