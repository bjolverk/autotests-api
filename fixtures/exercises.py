import pytest

from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseQueryRequestSchema, CreateExerciseResponseSchema
from fixtures.users import UserFixture
from fixtures.courses import CourseFixture

from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseQueryRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exercises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseQueryRequestSchema(course_id=function_course.response.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
