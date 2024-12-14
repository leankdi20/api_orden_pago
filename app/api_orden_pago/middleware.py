from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import traceback

class ProcessExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        try:
            # Formato del mensaje
            texto = f'ERROR: {str(exception)}\n{traceback.format_exc()}'
        except Exception as e:
            print(e)

        # Cliente de Slack
        client = WebClient(token=os.environ.get('SLACK_TOKEN'))

        try:
            # Enviar el mensaje a Slack
            response = client.chat_postMessage(
                channel="#orden-pago",  # Asegúrate de que el canal sea correcto
                text=texto
            )
            print('Slack notification sent to channel')
        except SlackApiError as slack_error:
            print(f"Error enviando mensaje a Slack: {slack_error.response['error']}")
