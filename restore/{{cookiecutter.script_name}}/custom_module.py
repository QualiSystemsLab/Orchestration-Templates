from cloudshell.workflow.orchestration.sandbox import Sandbox
from cloudshell.helpers.sandbox_reporter.reporter import SandboxReporter


def custom_flow(sandbox, components=None):
    """
    Workflow functions must have (sandbox, components) signature
    :param Sandbox sandbox:
    """
    api = sandbox.automation_api
    sb_id = sandbox.id
    logger = sandbox.logger
    reporter = SandboxReporter(api, sb_id, logger)  # logs to file and print to sandbox console

    reporter.warning("Starting pre-restore custom flow..")

    sb_details = api.GetReservationDetails(reservationId=sb_id, disableCache=True).ReservationDescription
    resources = sb_details.Resources
    reporter.info(f"Resource count in sandbox: {len(resources)}")

