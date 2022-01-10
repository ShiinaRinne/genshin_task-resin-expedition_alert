from typing import Literal, Optional
import pydantic


class ConfigData(pydantic.BaseModel):
    RUN_ENV: Literal["local", "cloud"]
    UID: str
    COOKIE: str
    NAME: Optional[str]

    SCKEY: Optional[str] = ""
    SCTKEY: Optional[str] = ""
    BARK_URL: Optional[str] = ""
    BARK_KEY: Optional[str] = ""
    BARK_GROUP: Optional[str] = ""
    BARK_ICON: Optional[str] = ""
    BARK_ARCHIVE: Optional[str] = ""
    WW_ID: Optional[str] = ""
    WW_APP_SECRET: Optional[str] = ""
    WW_APP_USERID: Optional[str] = ""
    WW_APP_AGENTID: Optional[str] = ""
    WW_BOT_KEY: Optional[str] = ""
    DD_BOT_TOKEN: Optional[str] = ""
    DD_BOT_SECRET: Optional[str] = ""
    DISCORD_WEBHOOK: Optional[str] = ""
    IGOT_KEY: Optional[str] = ""
    PUSH_PLUS_TOKEN: Optional[str] = ""
    PUSH_PLUS_USER: Optional[str] = ""
    TG_BOT_API: Optional[str] = ""
    TG_BOT_TOKEN: Optional[str] = ""
    TG_USER_ID: Optional[str] = ""
    COOL_PUSH_SKEY: Optional[str] = ""
    COOL_PUSH_MODE: Literal["send", "psend", "group", "pgroup"] = ""
    COOL_PUSH_SENDID: Optional[str] = ""
    QMSG_KEY: Optional[str] = ""
    CQHTTP_IP: Optional[str] = ""
    CQHTTP_PORT: Optional[int] = 5700
    CQHTTP_MESSAGE_TYPE: Literal["private", "group"] = ""
    CQHTTP_SEND_ID: Optional[str] = ""
    CQHTTP_TOKEN: Optional[str] = ""

    RESIN_ALERT_NUM: int
    RECEIVE_RESIN_DATA: Literal["ON", "OFF"]
    RECEIVE_BOSS_COUNT: Literal["ON", "OFF"]
    RECEIVE_TASK_NUM: Literal["ON", "OFF"]
    REVEIVE_EXPEDITION_NUM: Literal["ON", "OFF"]
    RECEIVE_HOMECOIN_ALERT: Literal["ON", "OFF"]
    EXPEDITION_COMPLETE_ALERT: Literal["ON", "OFF"]
    INCOMPLETE_ALERT: str
    SLEEP_TIME: int
    ALERT_SUCCESS_SLEEP_TIME: int
    SLEEP_START_TIME: Optional[str] = ""
    SLEEP_END_TIME: Optional[str] = ""