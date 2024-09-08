# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        # Пример данных в формате XML
        xml_content = """<students>
            <student name="Иванов Иван Иванович">
                <subject name="математика" score="80" />
                <subject name="программирование" score="90" />
                <subject name="литература" score="76" />
            </student>
            <student name="Петров Петр Петрович">
                <subject name="математика" score="100" />
                <subject name="социология" score="90" />
                <subject name="химия" score="61" />
            </student>
            <student name="Сидоров Сидор Сидорович">
                <subject name="математика" score="50" />
                <subject name="физика" score="45" />
                <subject name="химия" score="80" />
            </student>
        </students>"""

        # Ожидаемая структура данных
        data = {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 61)
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 50),
                ("физика", 45),
                ("химия", 80)
            ]
        }

        return xml_content, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        # Создаем временный XML файл
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
