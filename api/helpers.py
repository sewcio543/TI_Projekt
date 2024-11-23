from dataclasses import dataclass

from application.services.interfaces.icomment_service import ICommentService
from application.services.interfaces.igrudge_service import IGrudgeService
from application.services.interfaces.ipost_service import IPostService
from application.services.interfaces.iuser_service import IUserService
from domain.contracts.icomment_repository import ICommentRepository
from domain.contracts.igrudge_repository import IGrudgeRepository
from domain.contracts.ipost_repository import IPostRepository
from domain.contracts.iuser_repository import IUserRepository


@dataclass
class Repositories:
    users: IUserRepository
    posts: IPostRepository
    comments: ICommentRepository
    grudges: IGrudgeRepository


@dataclass
class Services:
    users: IUserService
    posts: IPostService
    comments: ICommentService
    grudges: IGrudgeService
