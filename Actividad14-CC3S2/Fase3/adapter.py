"""
Fase 3.2 — MockBucketAdapter
Simula la conexión con un bucket de almacenamiento para exportar infraestructura.
"""

import json
import datetime
from pathlib import Path

class MockBucketAdapter:
    """Adaptador simulado para subir configuraciones a un 'bucket'."""
    def __init__(self, bucket_name="mock-bucket"):
        self.bucket_name = bucket_name
        self.storage_path = Path("mock_storage")
        self.storage_path.mkdir(exist_ok=True)
        self.uploads = []

    def upload(self, file_name: str, content: dict):
        """Simula la subida de un archivo JSON al bucket."""
        file_path = self.storage_path / file_name
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2)
        record = {
            "bucket": self.bucket_name,
            "file": file_name,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        self.uploads.append(record)
        return record

    def export_metadata(self):
        """Exporta un JSON con todos los uploads simulados."""
        meta_path = self.storage_path / "bucket_metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(self.uploads, f, indent=2)
        return str(meta_path)


if __name__ == "__main__":
    adapter = MockBucketAdapter()
    example_data = {"module": "infra_test", "resources": 3}
    adapter.upload("infra_test.json", example_data)
    print(adapter.export_metadata())
