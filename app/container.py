from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory, Singleton

from app.auth.application.service.jwt import JwtService
from app.user.adapter.output.persistence.repository_adapter import UserRepositoryAdapter
from app.user.adapter.output.persistence.sqlalchemy.user import UserSQLAlchemyRepo
from app.user.application.service.user import UserService
from app.statistic_log.application.service.statistic import StatisticService
from app.statistic_log.adapter.output.persistence.repository_adapter import StatisticRepositoryAdapter
from app.statistic_log.adapter.output.persistence.sqlalchemy.statistic import StatistisLogRepo


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(packages=["app"])

    user_repo = Singleton(UserSQLAlchemyRepo)
    user_repo_adapter = Factory(UserRepositoryAdapter, user_repo=user_repo)
    user_service = Factory(UserService, repository=user_repo_adapter)

    statistic_log_repo = Singleton(StatistisLogRepo)
    statistic_repo_adapter = Factory(StatisticRepositoryAdapter, statistic_repo=statistic_log_repo)
    statistic_service = Factory(StatisticService, repository=statistic_repo_adapter)

    jwt_service = Factory(JwtService)
