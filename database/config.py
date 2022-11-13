from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    dialect: str
    user: str
    password: str
    host: str
    port: str
    db: str

    @property
    def connection_str(self):
        return (
            f'{self.dialect}://'
            f'{self.user}:'
            f'{self.password}@'
            f'{self.host}:'
            f'{self.port}/'
            f'{self.db}'
        )