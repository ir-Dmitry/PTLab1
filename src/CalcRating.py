# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CalcRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating

    def calc_academic_debts(self) -> int:
        debt_count = 0
        for key in self.data:
            debt_subject_count = 0
            for subject in self.data[key]:
                if subject[1] < 61:
                    debt_subject_count += 1
            if debt_subject_count == 2:
                debt_count += 1
        return debt_count
