from rest_framework.response import Response
from rest_framework.views import exception_handler

def handle_authentication_failure(exc, context):
    response = exception_handler(exc, context)
    if response.status_code == 401:
        return Response({
            'detail': "Please use utility app(Postman, httpie, or wget/curl) to login using your valid FGCES Trading Bot account.You've receive an Access Token that you can use to invoke API endpoints."
                }, 
            status=response.status_code
            )

    if response is not None:
        response.data['status_code'] = response.status_code

    return response