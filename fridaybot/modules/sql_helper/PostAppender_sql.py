from sqlalchemy import Boolean, Column, String, UnicodeText

from fridaybot.modules.sql_helper import BASE, SESSION


class Pa(BASE):
    __tablename__ = "pa"
    chat_id = Column(String(14), primary_key=True)
    textto_append = Column(UnicodeText)
    append_foot = Column(Boolean, default=False)

    def __init__(self, chat_id, textto_append, append_foot):
        self.chat_id = chat_id
        self.append_foot = append_foot
        self.textto_append = textto_append


Pa.__table__.create(checkfirst=True)


def add_new_datas_in_db(chat_id: int, textto_append, append_foot):
    setting_adder = Pa(str(chat_id), textto_append, append_foot)
    SESSION.add(setting_adder)
    SESSION.commit()


def get_all_setting_data(chat_id: int):
    try:
        s__ = SESSION.query(Pa).get(str(chat_id))
        return int(s__.chat_id), s__.append_foot, s__.textto_append
    finally:
        SESSION.close()


def is_data_indbs(chat_id: int):
    try:
        s__ = SESSION.query(Pa).get(str(chat_id))
        if s__:
            return s__.textto_append, s__.append_foot
    finally:
        SESSION.close()


def remove_datas(chat_id):
    s__ = SESSION.query(Pa).get(str(chat_id))
    saved_data = s__.chat_id, s__.append_foot, s__.textto_append
    if s__:
        SESSION.delete(saved_data)
        SESSION.commit()
