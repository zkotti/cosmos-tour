# How to contribute

We love pull requests. Here's a quick guide:

## Getting Started

- Make sure you have a GitHub account <a href="https://github.com/signup/free/" target="_blank">Github</a>
- Submit a ticket for your issue, assuming one does not already exist.
- Clearly describe the issue including steps to reproduce when it is a bug. If your prospective contribution concerns an idea rather than an error, describe it in full detail using the respective template for guidance.
- Make sure you fill in the earliest version that you know has the issue, using commit hashes if possible.
- Fork the repository on GitHub.

## Getting up-to-date

It is always a good practice to _update frequently_ your local records based on the changes that
have been made on the codebase recently.

### How to achieve that?

- If you are on the **main branch**, you could use `git pull`.
- If you are **not on main branch**, you could use:

  #### _Rebase_

  You could use the git command: `git rebase main`

  ###### _Note:_

  <p>If there are conflicts, needs to be resolved.
  This is the only issue that could arise using rebase.</p>

  #### _Merge_

  You could use the git command: `git merge main`

  > > _*Tip:*_<br>Despite the fact that both commands are very useful, it is preferable in projects with many contributors like ours, to use the _rebase_ command.
  > > <br>Why?<br>
  > > _Merge_ command creates a new commit each time being used, making _*commit history*_ less readable and manageable for maintainability and readability purposes.

## Making Changes

- Create a topic branch from where you want to base your work (this is usually the master branch.)
- Only target release branches if you are certain your fix must be on
  that branch.
- To quickly create a topic branch based on master;
  `git branch fix/master/my_contribution master` then checkout
  the new branch with `git checkout fix/master/my_contribution`.
  Please avoid working directly on the `master` branch.
- Make commits of logical units.
- Follow our `coding style`.
- Check again your code to assure nothing else was accidentally broken.

## Testing

We have created some tests in python. Currently, we do not require to install pytest.

#### Install Pytest
  
  Installing pytest by typing this command in command line: 
  ```pip install -U pytest```

#### Run Tests

You could run the tests that exist inside of file, by typing the following command:
   ```pytest -q -name_of_file```                                


###### Notes
- Given that you use pip manager, you could use those installation commands. Similar commands used for other package managers. 
- You install packages on the same place with your python package. Make sure that you use the same pip manager which is part of your python package to install the package correctly.

## Submitting Changes

- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request to the repository.

## Contribution Tips

- If contributing content to the guide, please make sure that your contribution conforms with [Google's guidelines on writing accessible documentation](https://developers.google.com/style/accessibility) where relevant.
- If adding a new Markdown file, it may be worth checking out whether it should also appear on the [website version of the guide](https://e-panourgia.github.io/cosmos-tour/). If so, it should be included in the `nav` section of [mkdocs.yml](https://github.com/zkotti/cosmos-tour/blob/main/mkdocs/mkdocs.yml).

## Style pattern

Every coding warehouse nowadays follows a specific pattern of code style,
so as to make life of developpers easier and their code prettier. _And so are we!_

#### Please take the following advices as kindly suggested:

##### Conventions

- Shall use **snake case** formatting for naming **modules** and **files**
- Shall use **title case** formatting for naming **Classes**
- Shall use **snake case** formatting for **variables**
- Shall use **upper case** formatting for **constants**
- **Code lines** should **not** exceed the length of **100 characters**

##### Additional Suggestions

- Classes should be saparated by two new lines of codes
- Classes should be saparated by one new lines of codes
- Every block of code should not be separated by new line in its core part.
- Comments should exist on separate line from code lines.
- Comments should not be separated with new lines from code lines.

###### Note

While style pattern has not been extracted from a specific resource,
it could be said that is inspired from PEP8 coding style.

## Additional Resources

- General GitHub documentation for help <a href="https://docs.github.com/en/" target="_blank">Help</a>
- GitHub pull request
  documentation <a href="https://help.github.com/articles/about-pull-requests/" target="_blank">Pull Request</a>
- PEP8 official style guide <a href="https://peps.python.org/pep-0008/" target="_blank">PEP8 guide</a>
- Pytest tool <a href="https://docs.pytest.org/en/7.1.x/" target="_blank">Pytest </a>
