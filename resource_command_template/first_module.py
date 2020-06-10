from helper_code.sandbox_print_helpers import *
import helper_code.automation_api_helpers as api_help
import cloudshell.helpers.scripts.cloudshell_scripts_helpers as script_help
import os
from DEBUG_GLOBALS import DEBUG_MODE

INPUT_COMMAND_PARAMETER = "CUSTOM_PARAM_NAME"


# ========== Primary Function ==========
def first_module_flow():
    """
    Functions passed into orchestration flow MUST have (sandbox, components) signature
    :param Sandbox sandbox:
    :param componentssc
    :return:
    """
    # script helpers to pull in sandbox details, resource details, and api session
    sb_context = script_help.get_reservation_context_details()
    resource_details = script_help.get_resource_context_details()
    api = script_help.get_api_session()

    res_id = sb_context.id
    ip = resource_details.address
    resource_name = resource_details.name


    # environment variables not available during dev, we can mock it
    if DEBUG_MODE:
        warn_print(api, res_id, "=== DEBUG_MODE Boolean is on ===")
        custom_param = "my debug param value"
    else:
        custom_param = os.environ[INPUT_COMMAND_PARAMETER]

    sb_print(api, res_id, "resource name is {}".format(resource_name))
    sb_print(api, res_id, "resource ip is {}".format(ip))
    sb_print(api, res_id, "custom param value: {}".format(custom_param))
