from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseQueryRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture
from fixtures.files import FileFixture

from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseQueryRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercise_client=ExercisesClient,
        function_user=UserFixture
) -> ExerciseFixture:
    request = CreateExerciseQueryRequestSchema()
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
