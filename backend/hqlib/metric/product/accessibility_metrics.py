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

from hqlib.typing import MetricValue
from ... import metric_source
from ...domain import LowerIsBetterMetric

class AccessibilityViolations(LowerIsBetterMetric):
    """ Metric for measuring the number of accessibility violations. """

    unit = 'toegankelijkheid violations'
    metric_source_class = metric_source.AxeReport
    name = 'Toegankelijkheid violations'
    target_value = 0
    low_target_value = 0

    def value(self) -> MetricValue:
        """ Return the actual value of the metric. """
        return -1 if not self._metric_source else self._metric_source.nr_violations()

