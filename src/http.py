from string import Template

import requests
from requests import Response, HTTPError

from src.exceptions import FailedFetchError, FailedResponseError


class Http:
    _response_error = Template(
        "$status_code\nRequest: $request_params\nResponse: $response"
    )
    def make_safe_request(self, http_method: str, request_params: dict) -> dict:
        """Query execution with error catching"""
        try:
            method = getattr(requests, http_method)
            response: Response = method(**request_params)
        except HTTPError:
            raise FailedFetchError(request_params.get("url"))

        try:
            response.raise_for_status()
        except HTTPError:
            raise FailedResponseError(
                self._response_error.substitute(
                    status_code=response.status_code,
                    request_params=request_params,
                    response=response.text
                )
            )
        return response.json()
