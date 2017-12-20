from django.conf import settings
import return_code

def gen(rslt, rslt_json, error_code=return_code.NORMAL_RESPONSE, error_msg='None'):
    return {
        'status': error_code,
        'errormsg': error_msg,
        rslt: rslt_json
    }
