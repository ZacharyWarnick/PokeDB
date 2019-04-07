"""Provides an easier API to convert objects into nested JSON.

This code was adapted from the following source:
https://wakatime.com/blog/32-flask-part-1-sqlalchemy-models-to-json
"""

import json
from sqlalchemy.orm.attributes import QueryableAttribute


def dot_add(p, k): return '{}.{}'.format(p, k)


def create_base_model(db):
    """Creates a BaseModel class for a given database."""

    class BaseModel(db.Model):

        __abstract__ = True

        def to_dict(self, show=None, _hide=None, _path=None):
            """Return a dictionary representation of this model."""

            show = show or []
            _hide = _hide or []

            def try_field(f):
                return getattr(self, f) if hasattr(self, f) else []

            hidden = try_field('__hiddenfields__')
            default = try_field('__defaultfields__') + ['id']

            if not _path:
                _path = self.__tablename__.lower()

                def prepend_path(item):
                    item = item.lower()
                    if item.split('.', 1)[0] == _path or not item:
                        return item
                    item = item if item[0] == '.' else '.' + item
                    return _path + item

                _hide[:] = [prepend_path(x) for x in _hide]
                show[:] = [prepend_path(x) for x in show]

            columns = self.__table__.columns.keys()
            relationships = self.__mapper__.relationships.keys()
            properties = dir(self)

            def handle_nested(key, item):
                return None if item is None else item.to_dict(
                    show=show,
                    _hide=_hide,
                    _path=dot_add(_path, key.lower()))

            def should_keep(key):
                check = dot_add(_path, key)
                should_skip = (key.startswith('_')
                               or check in _hide or key in hidden)

                return not should_skip and (check in show or key in default)

            ret_data = {}
            for key in list(filter(should_keep, columns)):
                ret_data[key] = getattr(self, key)

            for key in list(filter(should_keep, relationships)):
                rel = self.__mapper__.relationships[key]
                _hide.append(dot_add(_path, key))
                if rel.uselist:
                    items = getattr(self, key)
                    if rel.query_class is not None and hasattr(items, 'all'):
                        items = items.all()
                    for item in items:
                        ret_data.get(key, []).append(handle_nested(key, item))
                elif (rel.query_class is not None
                        or rel.instrument_class is not None):
                    item = getattr(self, key)
                    ret_data[key] = handle_nested(key, item)
                else:
                    ret_data[key] = getattr(self, key)

            rem_props = set(properties) - set(columns) - set(relationships)
            for key in list(filter(should_keep, rem_props)):
                if key.startswith('_') or not hasattr(self.__class__, key):
                    continue
                attr = getattr(self.__class__, key)
                if not isinstance(attr, (property, QueryableAttribute)):
                    continue

                item = getattr(self, key)
                if hasattr(item, 'to_dict'):
                    ret_data[key] = handle_nested(key, item)
                else:
                    ret_data[key] = json.loads(json.dumps(item))

            return ret_data

    return BaseModel
