from datetime import datetime

from aiogithub import objects
from aiogithub.objects.user import User
from aiogithub.objects.base_object import BaseResponseObject
from aiogithub.utils import return_key


class PartialRepo(BaseResponseObject):
    _url = 'repos/{user}/{repo}'
    _default_urls = {
        "archive_url": "repos/{owner[login]}/{name}/{{archive_format}}"
                       "{{/ref}}",
        "assignees_url": "repos/{owner[login]}/{name}/assignees{{/user}}",
        "blobs_url": "repos/{owner[login]}/{name}/git/blobs{{/sha}}",
        "branches_url": "repos/{owner[login]}/{name}/branches{{/branch}}",
        "collaborators_url": "repos/{owner[login]}/{name}/collaborators"
                             "{{/collaborator}}",
        "comments_url": "repos/{owner[login]}/{name}/comments{{/number}}",
        "commits_url": "repos/{owner[login]}/{name}/commits{{/sha}}",
        "compare_url": "repos/{owner[login]}/{name}/compare"
                       "/{{base}}...{{head}}",
        "contents_url": "repos/{owner[login]}/{name}/contents/{{+path}}",
        "contributors_url": "repos/{owner[login]}/{name}/contributors",
        "deployments_url": "repos/{owner[login]}/{name}/deployments",
        "downloads_url": "repos/{owner[login]}/{name}/downloads",
        "events_url": "repos/{owner[login]}/{name}/events",
        "forks_url": "repos/{owner[login]}/{name}/forks",
        "git_commits_url": "repos/{owner[login]}/{name}/git/commits{{/sha}}",
        "git_refs_url": "repos/{owner[login]}/{name}/git/refs{{/sha}}",
        "git_tags_url": "repos/{owner[login]}/{name}/git/tags{{/sha}}",
        "git_url": "git:github.com/octocat/Hello-World.git",
        "hooks_url": "repos/{owner[login]}/{name}/hooks",
        "issue_comment_url": "repos/{owner[login]}/{name}/issues"
                             "/comments{{/number}}",
        "issue_events_url": "repos/{owner[login]}/{name}/issues"
                            "/events{{/number}}",
        "issues_url": "repos/{owner[login]}/{name}/issues{{/number}}",
        "keys_url": "repos/{owner[login]}/{name}/keys{{/key_id}}",
        "labels_url": "repos/{owner[login]}/{name}/labels{{/name}}",
        "languages_url": "repos/{owner[login]}/{name}/languages",
        "merges_url": "repos/{owner[login]}/{name}/merges",
        "milestones_url": "repos/{owner[login]}/{name}/milestones{{/number}}",
        "notifications_url": "repos/{owner[login]}/{name}/notifications"
                             "{{?since, all, participating}}",
        "pulls_url": "repos/{owner[login]}/{name}/pulls{{/number}}",
        "releases_url": "repos/{owner[login]}/{name}/releases{{/id}}",
        "stargazers_url": "repos/{owner[login]}/{name}/stargazers",
        "statuses_url": "repos/{owner[login]}/{name}/statuses/{{sha}}",
        "subscribers_url": "repos/{owner[login]}/{name}/subscribers",
        "subscription_url": "repos/{owner[login]}/{name}/subscription",
        "tags_url": "repos/{owner[login]}/{name}/tags",
        "teams_url": "repos/{owner[login]}/{name}/teams",
        "trees_url": "repos/{owner[login]}/{name}/git/trees{{/sha}}"
    }

    @staticmethod
    def _get_key_mappings():
        return {
            'owner': objects.User,
            'organization': objects.Organization,
            'parent': Repo,
            'source': Repo
        }

    @property
    @return_key
    def id(self) -> int:
        pass

    @property
    @return_key
    def owner(self) -> User:
        pass

    @property
    @return_key
    def name(self) -> str:
        pass

    @property
    @return_key
    def full_name(self) -> str:
        pass

    @property
    @return_key
    def description(self) -> str:
        pass

    @property
    @return_key
    def private(self) -> bool:
        pass

    @property
    @return_key
    def fork(self) -> bool:
        pass

    @property
    @return_key
    def html_url(self) -> str:
        pass

    @property
    @return_key
    def clone_url(self) -> str:
        pass

    @property
    @return_key
    def git_url(self) -> str:
        pass

    @property
    @return_key
    def ssh_url(self) -> str:
        pass

    @property
    @return_key
    def mirror_url(self) -> str:
        pass

    @property
    @return_key
    def svn_url(self) -> str:
        pass

    @property
    @return_key
    def homepage(self) -> str:
        pass

    async def get_assignees(self) -> 'objects.BaseList[objects.User]':
        return await self._get_related_url('assignees_url', objects.User)

    async def get_blobs(
            self) -> 'objects.BaseList[objects.BaseResponseObject]':
        return await self._get_related_url('blobs_url',
                                           objects.BaseResponseObject)

    async def get_branches(self) -> 'objects.BaseList[objects.Branch]':
        return await self._get_related_url('branches_url', objects.Branch)

    async def get_branch(self, branch) -> 'objects.Branch':
        return await self._get_related_object('branches_url', objects.Branch,
                                              branch=branch)

    async def get_collaborators(self) -> 'objects.BaseList[objects.User]':
        return await self._get_related_url('collaborators_url', objects.User)

    async def get_comments(self) -> 'objects.BaseList[objects.Comment]':
        return await self._get_related_url('comments_url', objects.Comment)

    async def get_commits(self) -> 'objects.BaseList[objects.Commit]':
        return await self._get_related_url('commits_url', objects.Commit)

    # TODO: compare, contents

    async def get_contributors(self) -> 'objects.BaseList[objects.Repo]':
        return await self._get_related_url('contributors_url', objects.User)

    async def get_events(self) -> 'objects.BaseList[objects.Event]':
        return await self._get_related_url('events_url', objects.Event)

    async def get_forks(self) -> 'objects.BaseList[objects.Repo]':
        return await self._get_related_url('forks_url', objects.Repo)

    async def get_issues(self) -> 'objects.BaseList[objects.Issue]':
        return await self._get_related_url('issues_url', objects.Issue)

    async def get_stargazers(self) -> 'objects.BaseList[objects.User]':
        return await self._get_related_url('stargazers_url', objects.User)


class Repo(PartialRepo):
    @property
    @return_key
    def language(self) -> str:
        pass

    @property
    @return_key
    def forks_count(self) -> int:
        pass

    @property
    @return_key
    def stargazers_count(self) -> int:
        pass

    @property
    @return_key
    def watchers_count(self) -> int:
        pass

    @property
    @return_key
    def size(self) -> int:
        pass

    @property
    @return_key
    def default_branch(self) -> str:
        pass

    @property
    @return_key
    def open_issues_count(self) -> int:
        pass

    @property
    @return_key
    def has_issues(self) -> bool:
        pass

    @property
    @return_key
    def has_wiki(self) -> bool:
        pass

    @property
    @return_key
    def has_pages(self) -> bool:
        pass

    @property
    @return_key
    def has_downloads(self) -> bool:
        pass

    @property
    @return_key
    def pushed_at(self) -> datetime:
        pass

    @property
    @return_key
    def created_at(self) -> datetime:
        pass

    @property
    @return_key
    def updated_at(self) -> datetime:
        pass

    @property
    @return_key
    def permissions(self) -> dict:
        pass
