# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, choices=["txt", "xml"],
                        required=True, help="Format of the datafile")
    args = parser.parse_args(args)
    return args.path, args.format


def main():
    path, file_format = get_path_from_arguments(sys.argv[1:])
    if file_format == "txt":
        reader = TextDataReader()
    elif file_format == "xml":
        reader = XMLDataReader()

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debt_count = CalcRating(students).calc_academic_debts()
    print("Number of students with exactly 2 academic debts: ", debt_count)


if __name__ == "__main__":
    main()
