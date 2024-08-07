import datetime as dt
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
    prog='new_series.py',
    description='Create a new directory structure and metadata files for an experimental series'
)

parser.add_argument('-d', '--directory', default=Path(r'/Work/Experiments/'), type=Path, help='Path to the base directory in which to create a new series directory. If not specified it will be `./Work/Experiments/')
parser.add_argument('-i', '--identifier', help='An identifyer specifying the number of the series. If not specified, it will be a number equal to 1 larger than the number of directories in the base directory')
parser.add_argument('-n', '--name', type=str, default='Series', help='The name of the series.')

def make_journal(name, identifier):
    return f"""
    # {args.name} {identifier} Journal
    
    |   |   |
    |---|---|
    |Date|{dt.today().isoformat()}|
    |Aim||
    |Participants||
    |Equipment||
    |Sample||

    ## Summary
    |Data|Details|
    |----|---|
    |`filename`|`some details`|

    | Data number | Parameter | Result |
    |-------------|-----------|--------|
    |1|P1|Hypthesis correct|

    ## Section
    Detailed explanation of some part of the experiment goes here
    """

def make_metadata():
    return """
    {
    \t"sample": "",
    \t"beam_energy": 200,
    \t"mode": "",
    \t"spot": null,
    \t"cameralength": null,
    \t"magnification": null,
    \t"exposure_time": null,
    \t"navigation_shape": [null, null],
    \t"lineskip": null,
    \t"Holder": "",
    \t"X": null,
    \t"Y": null,
    \t"Z": null,
    \t"Alpha": null,
    \t"Beta": null,
    \t"rocking_frequency": null,
    \t"rocking_angle": null
    }
    """

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.directory)
    if not args.directory.is_dir():
        raise TypeError(f'Path "{args.directory}" is not a directory. Please try again with a path to a directory instead.')
    args.directory.mkdir(parents=True, exist_ok=True)
    if args.identifier is None:
        identifier = 0
        for p in args.directory:
            if p.is_dir():
                identifier+=1
        identifier = int(identifier)
    else:
        identifier = str(identifier)
    
    series_path = args.directory / f'{args.name}{identifier}'
    data_path = series_path / 'Data'
    data_path.mkdir(parents=True, exist_ok=True)

    #Create the journal.md file
    (series_path/'journal.md').write_text(make_journal(args.name, identifier))
    
    #Create
    (data_path/'metadata.json').write_text(make_journal(args.name, identifier))




