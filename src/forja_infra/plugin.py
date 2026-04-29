"""Registro del plugin forja-infra."""
from __future__ import annotations

from pathlib import Path

TEMPLATES_PATH = Path(__file__).parent / "templates"


def register(registry) -> None:
    registry.add_architecture(
        key="infra",
        description="Infraestructura como código — Ansible playbooks para proyectos forja",
        template_path=TEMPLATES_PATH / "infra_project",
        _source="forja-infra",
    )
