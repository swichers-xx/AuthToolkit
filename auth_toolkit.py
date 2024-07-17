
from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from authenticate_tool import AuthenticateTool

class AuthToolkit(BaseToolkit, ABC):
    name: str = "Auth Toolkit"
    description: str = "Toolkit to handle username and password authentication"

    def get_tools(self) -> List[BaseTool]:
        return [AuthenticateTool()]

    def get_env_keys(self) -> List[str]:
        return []
                