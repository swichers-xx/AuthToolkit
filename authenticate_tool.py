
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests

class AuthInput(BaseModel):
    username: str = Field(..., description="Username for authentication")
    password: str = Field(..., description="Password for authentication")
    login_url: str = Field(..., description="Login URL of the website or service")

class AuthenticateTool(BaseTool):
    name: str = "Authenticate Tool"
    args_schema: Type[BaseModel] = AuthInput
    description: str = "Tool to authenticate into websites and services using username and password"

    def _execute(self, username: str, password: str, login_url: str):
        payload = {
            'username': username,
            'password': password
        }
        response = requests.post(login_url, data=payload)
        if response.status_code == 200:
            return "Authentication successful"
        else:
            return f"Authentication failed: {response.status_code}, {response.text}"
                