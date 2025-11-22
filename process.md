# Development Process (How the Project Was Built)

The project was developed iteratively, ensuring a clear separation of concerns in each Git commit. [cite_start]This process was logged using descriptive commit messages, exceeding the requirement of 5 meaningful commits.

### 1. VS Code Setup and Initial Commit

[cite_start]The project began by setting up the development environment in VS Code[cite: 27]. The `calculator.py` file was created, and the repository was initialized locally:
* [cite_start]`git init` [cite: 33]
* The first commit established the function structure and entry point.

### 2. Implementing User Input

The next stage focused entirely on gathering the necessary inputs from the user: two integers and the operation choice string. This required using the `input()` function and the `int()` casting function in Python.

### 3. Arithmetic Logic Implementation (Two Commits)

The core functionality was split into two commits for clarity:

1.  **Commit 3:** Implemented the `if` and `elif` blocks for **Addition (A)** and **Subtraction (B)**.
2.  **Commit 4:** Completed the main logic by adding the `elif` blocks for **Multiplication (C)** and **Division (D)**.

### 4. Documentation and Final Polish

The final stage involved creating all required documentation and setting up the repository structure:

* [cite_start]Creation of the `docs/` folder and the required Markdown files.
* [cite_start]Creation of the `.gitignore` file to exclude system and VS Code-specific files[cite: 40].
* Implementation of the final `else` block to handle invalid operation choices.

### 5. Hosting on GitHub

After all commits were staged locally, the project was linked to a remote repository and pushed to GitHub using:
* `git remote add origin [URL]`
* [cite_start]`git push -u origin main` [cite: 35]

---

### ⏭️ Future Improvements

[cite_start]*(This section addresses the requirement for future improvements [cite: 50] and should be placed in its own file, `docs/FutureImprovements.md`)*

**\[File: `docs/FutureImprovements.md`]**

1.  **Robust Error Handling:** Currently, the program crashes on `ZeroDivisionError` or `ValueError` (if non-numeric input is given). Future versions should use `try-except` blocks to catch and handle these errors gracefully.
2.  **Operation Looping:** The current program runs once and exits. A future feature would be to wrap the `calculator()` function in a loop, allowing the user to perform multiple calculations until they explicitly choose to exit.
3.  **Advanced Functions:** Expand the feature set to include modulus, exponentiation, and potentially scientific functions (sin, cos, log).