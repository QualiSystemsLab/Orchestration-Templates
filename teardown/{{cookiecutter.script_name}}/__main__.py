from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.teardown.default_teardown_orchestrator import DefaultTeardownWorkflow
from custom_module import custom_flow

sandbox = Sandbox()
DefaultTeardownWorkflow().register(sandbox)
sandbox.workflow.add_to_teardown(custom_flow)
sandbox.execute_teardown()
