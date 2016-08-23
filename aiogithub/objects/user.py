from datetime import datetime

from aiogithub.objects.base_object import BaseResponseObject
from aiogithub import objects
from aiogithub.utils import return_key


class PartialUser(BaseResponseObject):
    _url = 'users/{login}'
    _default_urls = {
        'followers_url': 'users/{login}/followers',
        'following_url': 'users/{login}/following{{/other_user}}',
        'gists_url': 'users/{login}/gists{{/gist_id}}',
        'starred_url': 'users/{login}/starred{{/owner}}{{/repo}}',
        'subscriptions_url': 'users/{login}/subscriptions',
        'organizations_url': 'users/{login}/orgs',
        'repos_url': 'users/{login}/repos',
        'events_url': 'users/{login}/events{{/privacy}}',
        'received_events_url': 'users/{login}/received_events',
    }

    async def get_followers(self) -> 'objects.BaseList[objects.User]':
        return await self._get_related_url('followers_url', objects.User)

    async def get_following(self) -> 'objects.BaseList[objects.User]':
        return await self._get_related_url('following_url', objects.User)

    async def get_starred(self) -> 'objects.BaseList[objects.Repo]':
        return await self._get_related_url('starred_url', objects.Repo)

    async def get_subscriptions(self) -> 'objects.BaseList[objects.Repo]':
        return await self._get_related_url('subscriptions_url', objects.Repo)

    async def get_repos(self) -> 'objects.BaseList[objects.Repo]':
        return await self._get_related_url('repos_url', objects.Repo)

    async def get_events(self) -> 'objects.BaseList[objects.Event]':
        return await self._get_related_url('events_url', objects.Event)

    async def get_received_events(self) -> 'objects.BaseList[objects.Event]':
        return await self._get_related_url('received_events_url',
                                           objects.Event)

    @property
    @return_key
    def login(self) -> str:
        pass

    @property
    @return_key
    def id(self) -> int:
        pass

    @property
    @return_key
    def gravatar_id(self) -> str:
        pass

    @property
    @return_key
    def html_url(self) -> str:
        pass

    @property
    @return_key
    def type(self) -> str:
        pass

    @property
    @return_key
    def site_admin(self) -> str:
        pass


class User(PartialUser):
    _url = 'users/{login}'
    _default_urls = {
        'followers_url': 'users/{login}/followers',
        'following_url': 'users/{login}/following{{/other_user}}',
        'gists_url': 'users/{login}/gists{{/gist_id}}',
        'starred_url': 'users/{login}/starred{{/owner}}{{/repo}}',
        'subscriptions_url': 'users/{login}/subscriptions',
        'organizations_url': 'users/{login}/orgs',
        'repos_url': 'users/{login}/repos',
        'events_url': 'users/{login}/events{{/privacy}}',
        'received_events_url': 'users/{login}/received_events',
    }

    @property
    @return_key
    def company(self) -> str:
        pass

    @property
    @return_key
    def blog(self) -> str:
        pass

    @property
    @return_key
    def location(self) -> str:
        pass

    @property
    @return_key
    def email(self) -> str:
        pass

    @property
    @return_key
    def hireable(self) -> bool:
        pass

    @property
    @return_key
    def bio(self) -> str:
        pass

    @property
    @return_key
    def public_repos(self) -> int:
        pass

    @property
    @return_key
    def public_gists(self) -> int:
        pass

    @property
    @return_key
    def followers(self) -> int:
        pass

    @property
    @return_key
    def following(self) -> int:
        pass

    @property
    @return_key
    def created_at(self) -> datetime:
        pass

    @property
    @return_key
    def updated_at(self) -> datetime:
        pass


class AuthenticatedUser(User):
    @property
    @return_key
    def total_private_repos(self) -> int:
        pass

    @property
    @return_key
    def owned_private_repos(self) -> int:
        pass

    @property
    @return_key
    def private_gists(self) -> int:
        pass

    @property
    @return_key
    def disk_usage(self) -> int:
        pass

    @property
    @return_key
    def collaborators(self) -> int:
        pass

    @property
    @return_key
    def plan(self) -> dict:
        pass
