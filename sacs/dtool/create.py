from dtool_cli.cli import CONFIG_PATH
import datetime
import getpass
import dtoolcore

def complete_readme_template(string):
    user_email = dtoolcore.utils.get_config_value(
    "DTOOL_USER_EMAIL",
    CONFIG_PATH,
    "you@example.com"
    )

    user_full_name = dtoolcore.utils.get_config_value(
    "DTOOL_USER_FULL_NAME",
    CONFIG_PATH,
    "Your Name")
    return string.format(
        username=getpass.getuser(),
        DTOOL_USER_FULL_NAME=user_full_name,
        DTOOL_USER_EMAIL=user_email,
        date=datetime.date.today(),
        )