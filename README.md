# Awesome Algorithms 🚀
This repository contains a collection of challenging algorithms that I've worked through and explained in detail, with corresponding Python implementations.

### Project Structure
```
awesome-algorithms/
│
├── [README.md](README.md)            # Project overview
│
├── sliding-window/      # Each algorithm has its own folder
│   ├── maxi-of-minimums/         # Example: Sorting algorithms
│   │   ├── [idea-and-usage.md](sliding-window/maxi-of-minimums/idea-and-usage.md)  # Markdown post explaining the algorithm
│   │   └── [max_of_minimums.py](sliding-window/maxi-of-minimums/max_of_minimums.py)  # Python code for the algorithm
│   │
│   ├── ...              # More algorithms
│
└── assets/              # (Optional) Images or diagrams for explanations
```

### Commit Message Conventions
To maintain a clean and consistent commit history, please follow these conventions for commit messages:

1. **Format**: Use the following format for commit messages:
   ```
   <type>(<scope>): <subject>
   ```

2. **Types**:
   - `feat`: A new feature
   - `fix`: A bug fix
   - `docs`: Documentation changes
   - `style`: Code style changes (formatting, missing semi-colons, etc.)
   - `refactor`: Code refactoring (no functional changes, no bug fixes)
   - `test`: Adding or updating tests
   - `chore`: Changes to the build process or auxiliary tools and libraries

3. **Scope**: The scope should be the name of the module or file that the commit affects.

4. **Subject**: A brief description of the changes. Use the imperative mood (e.g., "Add", "Fix", "Update").

#### Examples
- `feat(sliding-window): Add max of minimums algorithm`
- `fix(max_of_minimums.py): Fix boundary calculation bug`
- `docs: Update README with commit message conventions`

By following these conventions, we can ensure that our commit history is easy to read and understand.
