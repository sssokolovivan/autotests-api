from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_client import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import CreateUserRequestSchema, get_public_users_client
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png",
)
create_file_response = files_client.create_file(create_file_request)
print("Create file data:", create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="string",
    maxScore=10,
    minScore=1,
    description="string",
    estimatedTime="string",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print("Create course data:", create_course_response)

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema(
    title="string",
    courseId=create_course_response.course.id,
    maxScore=create_course_response.course.max_score,
    minScore=create_course_response.course.min_score,
    orderIndex=0,
    description="string",
    estimatedTime="string",
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)