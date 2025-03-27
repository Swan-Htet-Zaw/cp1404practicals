"""Project Management Program
Estimated time: 2.5 hours
"""

from project import Project
import datetime


FILENAME = "projects.txt"


def main():
    """Main menu-driven program for managing projects."""
    projects = load_projects(FILENAME)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")
    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
    choice = input(menu + "\n>>> ").lower()

    while choice != 'q':
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice.")
        choice = input(menu + "\n>>> ").lower()

    if input(f"Would you like to save to {FILENAME}? ").lower().startswith("y"):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, 'w') as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and complete projects."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        user_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered = sorted([p for p in projects if p.start_date > user_date], key=lambda p: p.start_date)
        for project in filtered:
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    try:
        project = Project(name, start_date, priority, cost_estimate, completion)
        projects.append(project)
    except ValueError:
        print("Invalid input. Project not added.")


def update_project(projects):
    """Update a project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")
        project.update(new_percentage, new_priority)
    except (IndexError, ValueError):
        print("Invalid selection.")


if __name__ == '__main__':
    main()
