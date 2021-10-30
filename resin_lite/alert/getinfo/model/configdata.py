from typing import List, Literal
import pydantic

class ConfigData(pydantic.BaseModel):
    UID: str
    COOKIE:str
    QQ: str
    SLEEP_TIME: int
    