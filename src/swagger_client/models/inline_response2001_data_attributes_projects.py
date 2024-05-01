# coding: utf-8

"""
    Kengine API

    The official OpenAPI spec for the Kengine API.  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2001DataAttributesProjects(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "pull_request_number": "Object",
        "repo_name": "str",
        "org_name": "str",
        "branch": "str",
        "commit_hash": "str",
    }

    attribute_map = {
        "pull_request_number": "pull_request_number",
        "repo_name": "repo_name",
        "org_name": "org_name",
        "branch": "branch",
        "commit_hash": "commit_hash",
    }

    def __init__(
        self,
        pull_request_number=None,
        repo_name=None,
        org_name=None,
        branch=None,
        commit_hash=None,
    ):  # noqa: E501
        """InlineResponse2001DataAttributesProjects - a model defined in Swagger"""  # noqa: E501
        self._pull_request_number = None
        self._repo_name = None
        self._org_name = None
        self._branch = None
        self._commit_hash = None
        self.discriminator = None
        if pull_request_number is not None:
            self.pull_request_number = pull_request_number
        if repo_name is not None:
            self.repo_name = repo_name
        if org_name is not None:
            self.org_name = org_name
        if branch is not None:
            self.branch = branch
        if commit_hash is not None:
            self.commit_hash = commit_hash

    @property
    def pull_request_number(self):
        """Gets the pull_request_number of this InlineResponse2001DataAttributesProjects.  # noqa: E501


        :return: The pull_request_number of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :rtype: Object
        """
        return self._pull_request_number

    @pull_request_number.setter
    def pull_request_number(self, pull_request_number):
        """Sets the pull_request_number of this InlineResponse2001DataAttributesProjects.


        :param pull_request_number: The pull_request_number of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :type: Object
        """

        self._pull_request_number = pull_request_number

    @property
    def repo_name(self):
        """Gets the repo_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501


        :return: The repo_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this InlineResponse2001DataAttributesProjects.


        :param repo_name: The repo_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :type: str
        """

        self._repo_name = repo_name

    @property
    def org_name(self):
        """Gets the org_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501


        :return: The org_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this InlineResponse2001DataAttributesProjects.


        :param org_name: The org_name of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def branch(self):
        """Gets the branch of this InlineResponse2001DataAttributesProjects.  # noqa: E501


        :return: The branch of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this InlineResponse2001DataAttributesProjects.


        :param branch: The branch of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def commit_hash(self):
        """Gets the commit_hash of this InlineResponse2001DataAttributesProjects.  # noqa: E501


        :return: The commit_hash of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """Sets the commit_hash of this InlineResponse2001DataAttributesProjects.


        :param commit_hash: The commit_hash of this InlineResponse2001DataAttributesProjects.  # noqa: E501
        :type: str
        """

        self._commit_hash = commit_hash

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(InlineResponse2001DataAttributesProjects, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001DataAttributesProjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
