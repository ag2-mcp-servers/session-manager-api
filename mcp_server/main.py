# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T12:05:24+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import CreatenewsessionRequest, EditsessionRequest

app = MCPProxy(
    contact={},
    description="This documentation goes in detail how to interact with Session Manager's API. For a more top-level approach, check the [design documentation](https://help.vtex.com/tutorial/using-session-manager-to-track-browsing-sessions-in-vtex-stores--1pA0tqsD4BFnJYhQ7ORQBd).",
    title='Session Manager API',
    version='1.0',
    servers=[
        {'url': 'https://vtex.local'},
        {
            'description': 'VTEX server url',
            'url': 'https://{accountName}.{environment}.com.br/api',
            'variables': {
                'accountName': {
                    'default': '{accountName}',
                    'description': 'Name of the VTEX account. Used as part of the URL',
                },
                'environment': {
                    'default': '{environment}',
                    'description': 'Environment to use. Used as part of the URL.',
                },
            },
        },
    ],
)


@app.get(
    '/segments',
    description=""" You can add certain public fields in the query string and the system will attempt to fulfill it. Values such as `cultureInfo` and `utm` are overwriteable, just keep in mind such changes will not be reflected in the client's session.


If you wish to change the value on the session (and thus be reflected on the segment without special query strings), then use the PATCH request to session. """,
    tags=['session_management'],
)
def get_segment():
    """
    Get Segment
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sessions',
    description=""" Items are the keys of the values you wish to get. It follows the format `namespace1.key1,namespace2.key2`. So if you wish to recover the data sent on the previous request, it should be `public.country,public.postalCode`.


> The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment.


> If you want to retrieve all keys from Session Manager, you can use the wildcard operator (`*`) in your request (i.e. `?items=*`). """,
    tags=['session_management'],
)
def get_session(items: str):
    """
    Get Session
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/sessions',
    description=""" This works exactly the same as the POST create session, but when the request is sent with a vtex_session cookie, it retrieves the session first and then applies the changes instead of generating a new one.


As with the `POST` method, only keys inside the public namespace on the body are considered, and query parameters are automatically added to the public namespace.


> The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment. """,
    tags=['session_management'],
)
def editsession(body: EditsessionRequest):
    """
    Edit session
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sessions',
    description=""" The response should contain a session cookie. Further `POST` or `PATCH` requests will edit the existing session rather than creating a new one. All parameters in the body that are not within the public namespace will be ignored. Query string items will automatically be added to the public namespace. Cookies relevant to the session manager execution are also recorded.


> The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment. """,
    tags=['session_management'],
)
def createnewsession(body: CreatenewsessionRequest):
    """
    Create new session
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
