from typing import TypedDict
import httpx

from clients.api_client import APIClient

class UpdateUserRequestDict(TypedDict):
    """
    Описание стуктуры запроса на обновление пользователя
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> httpx.Response:
        """
        Метод получения текущего пользователя.
        
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")
        
    def get_user_id_api(self, user_id: str) -> httpx.Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/users/{user_id}')

    def update_user_id_api(self, user_id: str, request: UpdateUserRequestDict) -> httpx.Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_id_api(self, user_id: str) -> httpx.Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/users/{user_id}')