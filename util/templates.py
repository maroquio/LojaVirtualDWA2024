from fastapi.templating import Jinja2Templates
from jinja2 import ChoiceLoader, FileSystemLoader


def obter_jinja_templates(diretorio: str) -> Jinja2Templates:
    loader1 = FileSystemLoader(diretorio)
    loader2 = FileSystemLoader("templates/shared")
    loader = ChoiceLoader([loader1, loader2])
    templates = Jinja2Templates(directory="templates", loader=loader)
    return templates
