# Name

`dump_to_file`

## Description

Script to dump json to a file as yaml or json. Can be easily extended for your own purposes.

### Example

```python
from dump_to_file import dump_to_file

dump_to_file(
    data=json_data,
    file_type="json",
    file_name="top_ten",
    output_dir=None
)
```
