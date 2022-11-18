import json
from datetime import datetime


class JSONSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return str(datetime.isoformat(o))

        return self.default(o)
