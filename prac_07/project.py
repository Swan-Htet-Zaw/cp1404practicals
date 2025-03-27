"""Project class for CP1404 Project Management Program
Estimated time: 2.5 hours
"""

from datetime import datetime


class Project:
    """Represent a project with name, start date, priority, cost, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion_percentage == 100

    def update(self, new_percentage=None, new_priority=None):
        """Update the completion and/or priority."""
        if new_percentage != "":
            self.completion_percentage = int(new_percentage)
        if new_priority != "":
            self.priority = int(new_priority)

    def __lt__(self, other):
        """Sort by priority (lowest first)."""
        return self.priority < other.priority
