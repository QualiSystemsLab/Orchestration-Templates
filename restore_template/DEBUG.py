from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.helpers.scripts.cloudshell_dev_helpers import attach_to_cloudshell_as
from credentials import credentials
from first_module import first_module_flow

LIVE_SANDBOX_ID = "36f433ae-e5b5-4af2-9570-c5485f1958b5"

attach_to_cloudshell_as(user=credentials["user"],
                        password=credentials["password"],
                        domain=credentials["domain"],
                        reservation_id=LIVE_SANDBOX_ID,
                        server_address=credentials['server'])

sandbox = Sandbox()
first_module_flow(sandbox=sandbox, components=None)
