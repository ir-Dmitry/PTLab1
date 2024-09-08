# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
import pytest

RatingsType = dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 50),
                ("физика", 45),
                ("химия", 80)
            ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000,
            "Сидоров Сидор Сидорович": 58.3333
        }

        debt_count = 1  # Сидоров Сидор Сидорович имеет задолженности

        return data, rating_scores, debt_count

    def test_init_calc_rating(self, input_data: tuple[DataType, RatingsType,
                                                      int]) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType, int]) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]

    def test_calc_academic_debts(self, input_data: tuple[DataType, RatingsType,
                                                         int]) -> None:
        calc_rating = CalcRating(input_data[0])
        debt_count = calc_rating.calc_academic_debts()
        assert debt_count == input_data[2]
