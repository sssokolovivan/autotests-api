import re
import httpx
from typing import TypedDict
from clients.api_client import APIClient


class GetCoursesQuery(TypedDict):
    userId: str

class CreateCourseDict(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
    previewFileId: str | None
    createdByUserId: str | None

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_courses_api(self, query: GetCoursesQuery) -> httpx.Response:
        """
        Метод получения списка курсов

        :param query: Словарь с userId 
        :return: Ответ в виде httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> httpx.Response:
        """
        Метод получения курса по course_id

        :param course_id: Индентификатор курса
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseDict) -> httpx.Response:
        """
        Метод для создания курса

        :param request: Словарь с title, maxScore, minScore, description,estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/courses", json=request)
    
    def update_course_api(self, course_id: str, request: UpdateCourseDict):
        """
        Метод для частичного или полного обновления курса

        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description,estimatedTime, previewFileId, createdByUserId
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/courses")

    def delete_course_api(self, course_id: str) -> httpx.Response:
        """
        Метод для удаления курса по course_id

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}")
