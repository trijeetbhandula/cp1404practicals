"""
CP1404 Practical
Project Management Class
Estimate: 150 min (including project management program)
Actual:   178 minutes
"""


class Project:
    """Represent information about a project."""

    def __init__(self, name, start_date, priority, cost_estimate, percentage_complete):
        """Construct a Project from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage_complete = percentage_complete

    def __repr__(self):
        """Return string representation of a Project class"""
        return f'{self.name}, start: {self.start_date.strftime("%d/%m/%Y")}, priority {self.priority}, ' \
               f'estimate: ${self.cost_estimate:.2f}, completion: {self.percentage_complete}%'

    def __lt__(self, other):
        """Sorting the projects by priority."""
        return self.priority < other.priority

    def is_completed(self):
        """To determine if the project is completed or not"""
        return self.percentage_complete == 100
