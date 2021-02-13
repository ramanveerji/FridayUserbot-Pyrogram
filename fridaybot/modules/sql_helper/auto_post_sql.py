#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sqlalchemy import Column, String, UnicodeText
from fridaybot.modules.sql_helper import BASE, SESSION


class Post(BASE):
    __tablename__ = "post"
    to_post_chat_id = Column(String(14))
    target_chat_id = Column(String(14))

    def __init__(self, target_chat_id, to_post_chat_id):
        self.target_chat_id = target_chat_id
        self.to_post_chat_id = to_post_chat_id


Post.__table__.create(checkfirst=True)


def add_new_post_data_in_db(to_post_chat_id: str, target_chat_id: str):
    post_adder = Post(str(to_post_chat_id), str(target_chat_id))
    SESSION.add(post_adder)
    SESSION.commit()


def get_all_post_data(to_post_chat_id: str):
    try:
        s__ = SESSION.query(Post).get(str(to_post_chat_id))
        if s__:
            return str(s__.target_chat_id), str(s__.to_post_chat_id)
    finally:
        SESSION.close()


def is_post_data_in_db(target_chat_id: str):
    try:
        s__ = SESSION.query(Post).get(str(target_chat_id))
        if s__:
            return str(s__.to_post_chat_id)
    finally:
        SESSION.close()


def remove_post_data(to_post_chat_id):
    sed = SESSION.query(Post).get(str(to_post_chat_id))
    if sed:
        SESSION.delete(sed)
        SESSION.commit()
