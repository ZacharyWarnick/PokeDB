# CONTRIBUTING

## Setup

### Environment

Development should be done in a virtual environment (preferably) using [conda](https://docs.conda.io/projects/conda/en/latest/).

Miniconda is recommended, unless there is a specific need for the GUI features and add-ons provided by the full Anaconda installation.

The project specific environment info is saved in `environment.yml`.

*Note:* All commands should be run from the project root directory.

**Conda Setup:**
1. [Install conda](https://docs.conda.io/projects/conda/en/latest/)
2. Run `conda update -n root conda` to bring your installation to the latest version
3. Run `conda update --all` to upgrade the preinstalled packages

---

**Creating the Environment:**
```bash
$ conda env create -f environment.yml
```

**Entering or Leaving the Environment:**
```bash
$ conda activate idb
$ conda deactivate idb
```

**Updating the Environment:**
```bash
$ conda deactivate idb
$ conda env update -f=environment.yml
$ conda activate idb
```

### Project Layout

- cs329e-idb/ (Project Root)
    - .gitlab/ (Gitlab specific files, e.g. issue templates)
    - doc/
        - Generated documentation files...
        - Documentation configuration files...
    - idb/ (source package)
        - templates/ (Flask template files, e.g. dynamic HTML)
        - static/ (Flask static files, e.g. css)
        - \_\_init\_\_.py
        - Other top level source files...
    - test/
        - Test case files...
        - Test resource files (e.g. test SQL database)...
        - Other required files for testing...
    - .gitignore
    - README
    - CONTRIBUTING
    - Makefile
    - Other top-level project files...

## Workflow

1. Create a new issue or assign yourself to an existing issue
    - Make sure to add the issue label `in progress`
    - Reach out to anyone working on related issues
    - Use a template to create an issue when possible
    - Configure the issue (for newly created issues)
        - Provide a good description
        - Add up to 4 of the most relevant labels
        - Estimate a deadline
        - Assign a weight based on estimated work load
            - Scale weights: 1 (< 1 hour) - 10 (> 5 hours)
            - Use a weight of 0 for extremely quick/low priority tasks
        - Link any related issues
        - Choose the correct milestone
2. Update your local `develop` branch
    - `git checkout develop`
    - `git pull`
3. Checkout a new branch for the assigned issue
    - On the develop branch, run: `git checkout -b #-issue-desc`
    - Format: (issue\#)-simple-desc
    - Example: 2-contrib-rules
    - Try to keep branch names less than 20 characters
4. Check for a related test issue
    - If no related issue exists, add a new issue for the test cases
    - If the issue exists, assign it to yourself it it is unassigned
    - If the issue is already assigned, try to work with the existing assignee
    - Test cases have separate issues, but *development goes on the feature branch*
    - Pair programming should be used when possible for related feature/test issues
5. Add code and make commits on the issue branch
    - Periodically push the issue branch after committing
    - Avoid lots very small commits (e.g. < 5 changes)
    - To update the remote copy: `git push origin 2-contrib-rules`
    - Commit messages should fill in the blank: "If added to the repo, this commit will \_\_\_\_\_\_\_\_."
    - Standard practice is to omit the period at the end of commit messages
    - **Good Example:** Add the contribution guidelines
    - **Invalid Example:** Finished the contribution guidelines
6. Prepare to create a merge request
    - Run `git diff develop`
    - No red (i.e. bad) whitespace should show up
    - Check that code conforms to [PEP 8](https://www.python.org/dev/peps/pep-0008/) (optionally, run [autopep8](https://github.com/hhatto/autopep8) to format code)
    - Check that new code has docstring and explanatory comments
    - Update documentation using [pydoc](https://docs.python.org/3/library/pydoc.html)
    - Make sure all tests are passing
7. Create a merge request
    - Make sure the merge is from `#-issue-desc` to `develop`
    - Merges are done from `develop` to `master` when milestones are complete
8. Have at least 2 people approve of the changes
9. Merge the changes
    - If the merge can be condensed to a single commit, you can [squash & merge](https://docs.gitlab.com/ee/user/project/merge_requests/squash_and_merge.html)
    - Write a [good commit message](https://medium.com/@andrewhowdencom/anatomy-of-a-good-commit-message-acd9c4490437) for a squash commit
    - Delete the merged branch from gitlab (it won't automatically be deleted from your local machine)

## Review

These are basic guidelines, and review can be more or less intense depending on the content and scale of a merge request.

**Things to Review:**
- Is the code clear (readable/understandable)?
- Are the variable names good?
- Are the comments useful?
- Is the documentation clear and comprehensive?
- Are the test cases useful?
- Is everything spelled correctly?
- Does code follow PEP 8 formatting?
- Is the code free of bad whitespace?
- Are the test cases meaningful?
- Are test cases comprehensive?
- Is coverage sufficient (should be at least 95%)?
- Does the CI pipeline succeed?

If the above items all have a "yes" response, then approve the merge.

Once at least 2 users have approved the merge (excluding the person who opened it), then the merge can be made.

For merges into master, at least 3 users should approve the changes.
