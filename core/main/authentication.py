# import base64
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.exceptions import AuthenticationFailed


# class CustomBasicAuthentication(BasicAuthentication):

#     def authenticate(self, request):
#         # Получаем заголовок Authorization
#         auth = request.headers.get("Authorization")

#         if not auth or not auth.startswith("Basic "):
#             return None  # Нет аутентификации

#         # Декодируем base64 строку
#         try:
#             auth_parts = base64.b64decode(auth.split(" ")[1]).decode("utf-8")
#             username, password = auth_parts.split(":")
#         except (TypeError, ValueError):
#             raise AuthenticationFailed("Invalid Basic Auth Header")

#         # Аутентификация стандартным способом
#         user, _ = super().authenticate(request)

#         # Если аутентифицирован, выводим в терминал данные в base64
#         if user:
#             base64_credentials = base64.b64encode(
#                 f"{username}:{password}".encode("utf-8")
#             ).decode("utf-8")
#             print(f"AUTHORIZATION IN BASE64: Basic {base64_credentials}")

#         return (user, None)
