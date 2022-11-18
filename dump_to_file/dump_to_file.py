from os import PathLike
from pathlib import Path
from typing import Any, Union


def dump_to_file(
        data: Any,
        file_type: Union[str, PathLike] = None,
        file_name: Union[str, PathLike] = None,
        output_dir: Union[str, PathLike] = None,
) -> str:
    """
    Dump data to file as json or yaml.

    Optionally provide parameters.

    :param data: Serializable string.
    :param file_type: Defaults to json.
    :param file_name: Defaults to results.
    :param output_dir: Defaults to current directory.

    :return: str
    """

    file_types = ["json", "yaml"]
    file_type = file_type if file_type else "json"

    output_dir = Path(output_dir) if output_dir else Path()

    if file_type.lower() not in file_types:
        raise ValueError(
            f"File type must not in: {file_types} or None to default to json."
        )

    file_name = f"{file_name}.{file_type}" if file_name else f"results.{file_type}"

    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / file_name

    with file_path.open("w") as rf:
        if file_type == "json":
            import json

            rf.write(json.dumps(data, sort_keys=False))

        if file_type == "yaml":
            import yaml

            yaml.dump(data, rf, sort_keys=False)

    return f"Output written to {file_path}."
