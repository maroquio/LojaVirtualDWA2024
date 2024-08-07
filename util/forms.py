from pydantic import BaseModel


def as_form(cls: BaseModel):
    def as_form_func(
        *args,
        **kwargs,
    ) -> BaseModel:
        return cls(**kwargs)

    return as_form_func
