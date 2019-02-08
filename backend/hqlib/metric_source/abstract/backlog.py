"""
Copyright 2012-2018 Ministerie van Sociale Zaken en Werkgelegenheid

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from ... import domain


class Backlog(domain.MetricSource):
    """ Abstract base class for user story metrics. """

    def nr_user_stories(self) -> int:
        """ Return the total number of user stories. """
        raise NotImplementedError

    def approved_user_stories(self) -> int:
        """ Return the number of user stories that have been approved. """
        raise NotImplementedError

    def reviewed_user_stories(self) -> int:
        """ Return the number of user stories that have been reviewed. """
        raise NotImplementedError

    def nr_user_stories_with_sufficient_ltcs(self) -> int:
        """ Return the number of user stories that have enough logical test cases. """
        raise NotImplementedError
