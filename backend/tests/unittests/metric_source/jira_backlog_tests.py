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

import unittest
from unittest.mock import patch
import urllib.error
from hqlib.metric_source import Jira, JiraFilter
from hqlib.metric_source.jira_backlog import JiraBacklog


@patch.object(JiraFilter, 'nr_issues')
class JiraBacklogTests(unittest.TestCase):
    """ Unit tests of the constructor of the Jira class. """

    @patch.object(JiraFilter, '__init__')
    def test_init(self, mock_init, mock_nr_issues):
        """ Tests that the inner JiraFilter is initialized with correct parameters """
        mock_init.return_value = None
        backlog = JiraBacklog('url!', 'username!', 'password!', 'project!')
        backlog.nr_user_stories()
        mock_nr_issues.assert_called_once()
        mock_init.assert_called_once_with('url!', 'username!', 'password!')
        self.assertEqual('Jira backlog', backlog.metric_source_name)

    def test_nr_user_stories(self, mock_nr_issues):
        """ Tests that the function invokes correct default jql query. """
        mock_nr_issues.return_value = 1, None
        backlog = JiraBacklog('url!', 'username!', 'password!', 'project!')
        result = backlog.nr_user_stories()
        self.assertEqual(1, result)
        mock_nr_issues.assert_called_once_with('project = "project!" AND type in (Story, "Logical Test Case")')

    def test_nr_user_stories_custom(self, mock_nr_issues):
        """ Tests that the function invokes correct custom jql query. """
        mock_nr_issues.return_value = 1, None
        backlog = JiraBacklog('url!', 'username!', 'password!', 'project!', {"nr_user_stories": ['1st {project}', '2nd {project}']})
        result = backlog.nr_user_stories()
        self.assertEqual(1, result)
        mock_nr_issues.assert_called_once_with('1st project!', '2nd project!')

    def test_nr_user_stories_custom_filter_number(self, mock_nr_issues):
        """ Tests that the function invokes correct custom jira filter number instead of the query. """
        mock_nr_issues.return_value = 1, None
        backlog = JiraBacklog('url!', 'username!', 'password!', 'whatever!?', {"nr_user_stories": [11, '12']})
        result = backlog.nr_user_stories()
        self.assertEqual(1, result)
        mock_nr_issues.assert_called_once_with('11', '12')
