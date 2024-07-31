# Requirements Document

## Task Class

The `Task` class represents a single task in the task manager.

### Attributes

- `title` (str): Stores the task title.
- `description` (str): Stores the task description.

### Methods

- `__init__(title, description)`:
  - Initializes the attributes `title` and `description`.
  - **Returns**: None.

- `__repr__()`:
  - Converts a `Task` object to a string format for saving in a `.json` file.
  - **Returns**: A string in `"Title-Description"` format.

- `__str__()`:
  - Converts a `Task` object to a string displayable to the user.
  - **Returns**: A string in `"title\n\tdescription"` format.

- `from_str(string)`:
  - A class method to convert a string back into a `Task` object.
  - **Returns**: A `Task` object.

- **Getters and Setters**:
  - For both `title` and `description` attributes.

## TaskManager Class

The `TaskManager` class manages a collection of `Task` objects.

### Attributes

- `tasks` (list): A list of `Task` objects.

### Methods

- `__init__()`:
  - Initializes an empty list of tasks.
  - **Returns**: None.

- `write_to_file()`:
  - Writes all tasks to a `.json` file.
  - **Returns**: None.

- `load_from_file()`:
  - Loads tasks from a `.json` file.
  - **Returns**: None.

- `add_task(title, description)`:
  - Adds a new task to the list. The title must be unique.
  - **Returns**: None.
  - **Note**: User input is handled inside the function.

- `view_tasks()`:
  - Displays all tasks.
  - **Returns**: None.

- `search_task(title)`:
  - Searches for a task by title.
  - **Returns**: The index of the task.
  - **Note**: This function is used internally for modifying tasks.

- `delete_task(title)`:
  - Deletes a task by title. Uses `search_task()` to find the task.
  - **Returns**: None.

- `update_task(title, new_description)`:
  - Updates a task. Uses `search_task()` to find the task.
  - **Returns**: None.

## Extra Points

- **Duplicates**: Task titles must be unique; duplicates are not allowed.
- **User Access**: Users do not have direct access to the `search_task()` function; it is used internally by other methods.

