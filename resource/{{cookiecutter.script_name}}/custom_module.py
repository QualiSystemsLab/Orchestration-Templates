from typing import Dict

from cloudshell.helpers.scripts import cloudshell_scripts_helpers as script_help
from cloudshell.logging.qs_logger import get_qs_logger
from cloudshell.helpers.sandbox_reporter.reporter import SandboxReporter
from cli_handler import LinuxSSH


def _get_attrs_without_namespace(attrs: dict) -> Dict[str, str]:
    """
    removes shell namespace from attribute keys
    Allows to do dictionary key lookups without prefixing the model / shell name
    example: {"Cisco Router 2G.User": root} --> {"User": root }
    """
    return {k.split(".")[-1]: v for k, v in attrs.items()}


def custom_flow():
    api = script_help.get_api_session()
    sb_details = script_help.get_reservation_context_details()
    resource_details = script_help.get_resource_context_details()
    sb_id = sb_details.id
    logger = get_qs_logger(log_group=sb_id,
                           log_category=resource_details.model,
                           log_file_prefix=resource_details.name)
    reporter = SandboxReporter(api, sb_id, logger)

    # extract resource details
    namespaced_attrs = resource_details.attributes
    normalized_attrs = _get_attrs_without_namespace(namespaced_attrs)
    user = normalized_attrs.get("User")
    if not user:
        raise ValueError(f"Please populate User attribute on resource {resource_details.name}")
    encrypted_password = normalized_attrs.get("Password")
    decrypted_password = api.DecryptPassword(encrypted_password).Value
    if not decrypted_password:
        raise ValueError(f"Please populate Password attribute on resource {resource_details.name}")

    # instantiate session to device
    ssh = LinuxSSH(ip=resource_details.address, user=user, password=decrypted_password)

    # start flow
    reporter.warning(f"Starting command for {resource_details.name}...")
    output = ssh.send_command(f"ifconfig")

    # printing to std_out will be the output return value
    print(output)
