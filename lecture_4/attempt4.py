from typing import TypeAlias

FinishedPlace: TypeAlias = int
FinishedTimeSeconds: TypeAlias = str | int | float
RacerName: TypeAlias = str
RacerTeam: TypeAlias = str

RacerInfo: TypeAlias = dict[
    str, FinishedPlace | FinishedTimeSeconds | RacerName | RacerTeam
]

RACE_DATA: dict[int, RacerInfo] = {
    1: {
        'RacerName': 'Vova',
        'RacerTeam': 'KAMAZ',
        'FinishedPlace': 3,
        'FinishedTimeSeconds': 3600,
    },
    2: {
        'RacerName': 'Vova',
        'RacerTeam': 'VAZ',
        'FinishedPlace': 2,
        'FinishedTimeSeconds': 3321,
    },
    3: {
        'RacerName': 'Gennady',
        'RacerTeam': 'MAZ',
        'FinishedPlace': 1,
        'FinishedTimeSeconds': 3000,
    },
    4: {
        'RacerName': 'Grisha',
        'RacerTeam': 'KAMAZ',
        'FinishedPlace': 5,
        'FinishedTimeSeconds': 5041,
    },
    5: {
        'RacerName': 'Sergey',
        'RacerTeam': 'LG+BT',
        'FinishedPlace': 4,
        'FinishedTimeSeconds': 4144,
    },
}


def count (x: int | str | float | dict [int | str | float, int | str | float]) -> int | str | float:

    for key in RACE_DATA.items:
        for key in range (1, 6):
            if 'FinishedPlace' == 1:
                for key, value in RACE_DATA.items():
                    print(f'Победитель: {key} {value}')
            elif 'FinishedPlace' == 2:
                for key, value in RACE_DATA.items():
                    print(f'Второе место: {key} {value}')
            elif 'FinishedPlace' == 3:
                for key, value in RACE_DATA.items():
                    print(f'Третье место: {key} {value}')
answer = count(RACE_DATA.keys)
print (answer)
