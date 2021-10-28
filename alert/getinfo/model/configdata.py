from typing import List, Literal
import pydantic

class ConfigData(pydantic.BaseModel):
    UID: str
    COOKIE:str
    NAME:str

    SCKEY:str
    SCTKEY:str
    BARK_KEY:str
    BARK_GROUP:str
    BARK_ICON:str
    BARK_ARCHIVE:str
    WW_ID: str
    WW_APP_SECRET: str
    WW_APP_USERID: str
    WW_APP_AGENTID: str
    WW_BOT_KEY: str
    DD_BOT_TOKEN: str
    DD_BOT_SECRET: str
    DISCORD_WEBHOOK: str
    IGOT_KEY: str
    PUSH_PLUS_TOKEN: str
    PUSH_PLUS_USER: str
    TG_BOT_API: str
    TG_BOT_TOKEN: str
    TG_USER_ID: str
    COOL_PUSH_SKEY: str
    COOL_PUSH_MODE: Literal["send","psend","group","pgroup"]
    COOL_PUSH_SENDID: str
    QMSG_KEY: str

    RESIN_ALERT_NUM: int
    RECEIVE_RESIN_DATA: Literal["ON","OFF"]
    RECEIVE_BOSS_COUNT: Literal["ON","OFF"]
    RECEIVE_TASK_NUM: Literal["ON","OFF"]
    REVEIVE_EXPEDITION_NUM: Literal["ON","OFF"]
    INCOMPLETE_ALERT: str 
    SLEEP_TIME: int 
    ALERT_SUCCESS_SLEEP_TIME:int
    