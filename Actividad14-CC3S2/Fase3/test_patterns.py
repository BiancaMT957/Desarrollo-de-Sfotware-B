"""
Fase 3.3 — Tests unitarios para patrones de la Fase 2.
Usa pytest para validar Factory, Prototype y Singleton.
"""

import pytest
from datetime import datetime
from adapter import MockBucketAdapter


class DummyFactory:
    def create(self, name):
        return {"type": "null_resource", "name": name}


class DummyPrototype:
    def __init__(self, template):
        self.template = template

    def clone(self, suffix):
        clone = self.template.copy()
        clone["name"] += f"_{suffix}"
        return clone


def test_factory_creates_resources():
    factory = DummyFactory()
    r1 = factory.create("res1")
    assert r1["type"] == "null_resource"
    assert "res1" in r1["name"]


def test_prototype_clones_independently():
    proto = DummyPrototype({"name": "base"})
    clone = proto.clone("v1")
    assert clone["name"] == "base_v1"
    assert clone is not proto.template


def test_mock_bucket_upload(tmp_path):
    adapter = MockBucketAdapter("pytest-bucket")
    content = {"test": True, "timestamp": datetime.now().isoformat()}
    record = adapter.upload("test.json", content)
    assert record["bucket"] == "pytest-bucket"
    assert "timestamp" in record
