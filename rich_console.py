from rich.console import Console

console = Console()

def merge_dict(dict_1, dict_2):
    merged_dict = {**dict_1, **dict_2}
    console.log(merged_dict, log_locals=True)

merge_dict({'id': 1}, {'name': 'Ashutosh'})