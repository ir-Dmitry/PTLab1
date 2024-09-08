# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        for student in root.findall('student'):
            self.key = student.get('name')
            self.students[self.key] = []
            for subject in student.findall('subject'):
                subj_name = subject.get('name')
                score = int(subject.get('score'))
                self.students[self.key].append((subj_name, score))
        return self.students
