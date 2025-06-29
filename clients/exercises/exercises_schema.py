from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic.alias_generators import to_camel
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа вывода списка заданий
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа вывода задания
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    course_id: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class UpdateExerciseQueryRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class UpdateExerciseQueryResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление упражнения
    """
    exercise: ExerciseSchema
