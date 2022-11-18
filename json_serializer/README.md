# Name

`json_serializer`

## Description

When `default=str` isn't enough, write your own.

### Example

```python
from json_serializer import JSONSerializer

json.dumps(data_with_dt_objects, indent=2, cls=JSONSerializer)
```
