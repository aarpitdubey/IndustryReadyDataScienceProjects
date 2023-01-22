# Introduction To Git and Github :

## VC (Version Control) :

- VC is a system that records changes to a file or set of files over time, so that you can recall specific versions later.

- VCS (Version Control system) also generally means that if you screw things up or lose files, you can easily recover them.

## What is Git?

- Git is a distributed version control system that allows developers and operations teams to collaborate and keep track pf the changes made on a project.

- It is a software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during softwaredevelopment.

- its primary goals includes speed, data security (SHA-256) and integrity.

## Why Git?

1. It saves time

2. You can work offline then you can pull changes and push your changes.

3. you can undo or revert changes

4. you can be safe from mixing up things and creating multiple folders with names like "final", "final_part1", "final_part2", "final_part3", and so on.

5. Making useful commits with messages make you remind why you make these changes or for what? 

## What is Github?

- It is a Internet hosting service for software development and version control using Git.

- It is Online software development, hosting and version control platform.

How to create repositories in Github, let's see:

![Creating repo in Github](./images/1_creating_repo_in_Github.gif)

Now, the same task we can do from CMD using Git commands.

Before jumping to CMD, you have to download the git software or distributed VCS in your computer system : [Click to download Git](https://git-scm.com/).

Step 1 :  Goto to your Project Directory and create a new folder and name it anything you want.

Step 2 : I prefer VSCode Editor but you can choose any one of your choice. Open it with that folder, if the Text editor have terminal then it's good but if not then open CMD and change directory(using cd command) to your project directory and folder.

Step 3 : In VSCode edtior, terminal is there but you can do the same from Command Prompt too. From the current working directory in CMD change to your project folder and type this command : ```git init``` 

1. ### ```git init :``` This command is use to create a new repository locally from CMD.
let's see how : 

![git ini command](./images/2_git_init_command.gif)

2. ### ```git status :``` This command is used to check the status of your repository means it displays the state of the working directory and the staging area.