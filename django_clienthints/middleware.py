from .utils import get_future_policy_header_value


class ClientHintsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        feature_policy = get_future_policy_header_value()
        if feature_policy:
            if 'Feature-Policy' in response:
                response[
                    'Feature-Policy'
                ] = f'{response["Feature-Policy"]};{feature_policy}'
            else:
                response['Feature-Policy'] = feature_policy

        return response
