from typing import List, Literal
import pydantic

class ConfigData(pydantic.BaseModel):
    UID: str
    COOKIE:str
    WECOM_STATUS:Literal["ON","OFF"]
    SERVER_CHAN_STATUS:Literal["ON","OFF"]
    SENDKEY:str
    WECOM_CORP_ID: str
    WECOM_SECRET: str 
    WECOM_USER_ID: str
    WECOM_AGENT_ID: str 

    RESIN_ALERT_NUM: str 
    RECEIVE_RESIN_DATA: Literal["ON","OFF"]
    RECEIVE_BOSS_COUNT: Literal["ON","OFF"]
    RECEIVE_TASK_NUM: Literal["ON","OFF"]
    REVEIVE_EXPEDITION_NUM: Literal["ON","OFF"]
    INCOMPLETE_ALERT: str 
    SLEEP_TIME: int 
    