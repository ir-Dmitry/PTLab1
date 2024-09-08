# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments() -> tuple[list[str], tuple[str, str]]:
    return ["-p", "/home/user/file.txt", "-f",
            "txt"], ("/home/user/file.txt", "txt")


@pytest.fixture()
def correct_arguments_xml() -> tuple[list[str], tuple[str, str]]:
    return ["-p", "/home/user/file.xml", "-f",
            "xml"], ("/home/user/file.xml", "xml")


@pytest.fixture()
def noncorrect_arguments_missing_format() -> list[str]:
    return ["/home/user/file.txt"]


@pytest.fixture()
def noncorrect_arguments_missing_flag() -> list[str]:
    return ["-p", "/home/user/file.txt"]


@pytest.fixture()
def noncorrect_arguments_invalid_format() -> list[str]:
    return ["-p", "/home/user/file.txt", "-f", "pdf"]


def test_get_path_from_correct_arguments(
    correct_arguments: tuple[list[str], tuple[str, str]]
) -> None:
    path, format_ = get_path_from_arguments(correct_arguments[0])
    assert (path, format_) == correct_arguments[1]


def test_get_path_from_correct_arguments_xml(
    correct_arguments_xml: tuple[list[str], tuple[str, str]]
) -> None:
    path, format_ = get_path_from_arguments(correct_arguments_xml[0])
    assert (path, format_) == correct_arguments_xml[1]


def test_get_path_from_noncorrect_arguments_missing_format(
    noncorrect_arguments_missing_format: list[str]
) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_missing_format)
    assert e.type == SystemExit


def test_get_path_from_noncorrect_arguments_missing_flag(
    noncorrect_arguments_missing_flag: list[str]
) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_missing_flag)
    assert e.type == SystemExit


def test_get_path_from_noncorrect_arguments_invalid_format(
    noncorrect_arguments_invalid_format: list[str]
) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_invalid_format)
    assert e.type == SystemExit
