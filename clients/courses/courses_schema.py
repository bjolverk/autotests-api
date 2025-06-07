from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from pydantic.alias_generators import to_camel
from tools.fakers import fake


# Добавили описание структуры курса
class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema  # Вложенная структура файла
    estimated_time: str
    created_by_user: UserSchema  # Вложенная структура пользователяженная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    user_id: str


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
    # Добавили генерацию случайного заголовка
    title: str = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    # Добавили генерацию случайного идентификатора файла
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    # Добавили генерацию случайного идентификатора пользователя
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


# Добавили описание структуры запроса на создание курса
class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    # Добавили генерацию случайного заголовка
    title: str | None = Field(default_factory=fake.sentence)
    # Добавили генерацию случайного максимального балла
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    # Добавили генерацию случайного минимального балла
    min_score: int | None = Field(alias="minScore", default_factory=fake.min_score)
    # Добавили генерацию случайного описания
    description: str | None = Field(default_factory=fake.text)
    # Добавили генерацию случайного предполагаемого времени прохождения курса
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)
