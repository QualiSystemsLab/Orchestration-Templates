from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
from credentials import credentials
from first_module import first_module_flow

LIVE_SANDBOX_ID = "8385019c-2d84-4396-b091-dc5b5ea3cdbf"
TARGET_RESOURCE_NAME = "micro 1"
TARGET_SERVICE_NAME = None

attach_to_cloudshell_as(user=credentials["user"],
                        password=credentials["password"],
                        domain=credentials["domain"],
                        reservation_id=LIVE_SANDBOX_ID,
                        server_address=credentials['server'],
                        resource_name=TARGET_RESOURCE_NAME,
                        service_name=TARGET_SERVICE_NAME)

first_module_flow()
