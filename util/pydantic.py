from pydantic import ValidationError
from pydantic_core import InitErrorDetails


def create_validation_error(instance, field_name, error_message):
    values = instance.dict()
    error_detail = InitErrorDetails(
        {
            "type": "value_error",
            "loc": ["body", field_name],
            "input": values[field_name],
            "ctx": {
                "error": f"{error_message}",
            },
        }
    )
    errors_obj = ValidationError.from_exception_data(
        title="detail", line_errors=[error_detail]
    )
    return {"detail": errors_obj.errors()}


def create_validation_errors(instance, field_names, error_messages):
    values = instance.dict()
    validation_errors = []
    for field_name, error_message in zip(field_names, error_messages):
        error_detail = InitErrorDetails(
            {
                "type": "value_error",
                "loc": ["body", field_name],
                "input": values[field_name],
                "ctx": {
                    "error": f"{error_message}",
                },
            }
        )
        validation_errors.append(error_detail)
    errors_obj = ValidationError.from_exception_data(
        title="detail", line_errors=validation_errors
    )
    return {"detail": errors_obj.errors(include_input=False, include_url=False)}
