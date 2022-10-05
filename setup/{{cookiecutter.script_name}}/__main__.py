from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.workflow.orchestration.setup.default_setup_orchestrator import DefaultSetupWorkflow
from custom_module import custom_flow

sandbox = Sandbox()
DefaultSetupWorkflow().register(sandbox)
sandbox.workflow.on_configuration_ended(custom_flow)
sandbox.execute_setup()
