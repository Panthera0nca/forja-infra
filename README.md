# forja-infra

Plugin de [forja](https://pypi.org/project/forja/) — infraestructura como código con Ansible para proyectos forja.

```bash
pip install forja forja-infra
dfg init mi_infra --arch infra
```

## Qué genera

```
mi_infra/
├── ansible.cfg
├── requirements.yml          # colecciones Ansible Galaxy
├── inventory/
│   ├── hosts.yml             # servidores objetivo
│   └── group_vars/
│       └── all.yml           # variables globales
├── playbooks/
│   ├── provision.yml         # setup base (Python, Docker, Postgres)
│   ├── provision_kafka.yml   # brokers Kafka (para forja-streaming)
│   ├── provision_lakehouse.yml # DuckDB serving (para forja-lakehouse)
│   └── deploy.yml            # deploy del proyecto forja
└── roles/
    ├── common/   # Python, Docker
    ├── postgres/ # Postgres 16 via Docker
    ├── kafka/    # Kafka KRaft via Docker
    └── duckdb/   # DuckDB CLI + storage
```

## Uso

```bash
# 1. Instalar Ansible y colecciones
make install

# 2. Editar inventory/hosts.yml con tus IPs
# 3. Editar inventory/group_vars/all.yml con tus passwords

# 4. Verificar conectividad
make ping

# 5. Provisionar según tu stack
make provision              # ETL (Postgres)
make provision-kafka        # + Kafka (streaming)
make provision-lakehouse    # + DuckDB (lakehouse)

# 6. Desplegar el proyecto
make deploy
```

## Compatibilidad con plugins forja

| Plugin | Playbook |
|---|---|
| `forja` (ETL, hexagonal) | `provision.yml` |
| `forja-streaming` | `provision_kafka.yml` |
| `forja-lakehouse` | `provision_lakehouse.yml` |

## Licencia

MIT
