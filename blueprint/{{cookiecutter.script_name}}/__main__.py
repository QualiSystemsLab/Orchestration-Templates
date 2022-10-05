from cloudshell.workflow.orchestration.sandbox import Sandbox
from custom_module import custom_flow

sandbox = Sandbox()
custom_flow(sandbox=sandbox)
