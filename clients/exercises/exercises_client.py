from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseDict(TypedDict):
    """
    Описание структуры обновления упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения упражнения
    """
    exercises: list[Exercise]

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса создания упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQuery(TypedDict):
    """
    Описание структуры query параметров упражнения
    """
    courseId: str

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuery) -> Response:
        """
        Метод для получения списка exercises

        :param query: Словарь с query (course_id)
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения конкретного exercise

        :param exercise_id: Идентификатор упражнения
        :return: Ответ в виде httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания exercise

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseDict) -> Response:
        """
        Метод для обновления exercise

        :param exercise_id: Идентификатор упражнения 
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления exercise

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        """
        Метод, который возвращает ответ в виде json
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQuery) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExercisesResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseDict) -> GetExercisesResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

    def delete_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        response = self.delete_exercise_api(exercise_id)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))