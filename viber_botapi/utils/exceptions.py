class ApiViberException(Exception):
    def __init__(self, method, result):
        super().__init__(
            f"Error code: {result['code']}. Method: {method}. \
            Message: {result['message']}. Description: {result['description']}")


class ApiHttpException(Exception):
    def __init__(self, status, reason, text):
        super().__init__(
            f"The server returned HTTP {status} {reason}. Response body:\n[{text}]"
        )


class ApiInvalidJsonException(Exception):
    def __init__(self, result):
        super().__init__(
            f"The server returned an invalid JSON response. \
            Response body:\n[{result.text.encode('utf8')}]"
        )
