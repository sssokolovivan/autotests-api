from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class UpdateExerciseDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class CreateExerciseDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQuery(TypedDict):
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

    def create_exercise_api(self, request: CreateExerciseDict) -> Response:
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
