# Moss in Linux/macOS
[Moss](https://theory.stanford.edu/~aiken/moss/) can detect plagiarism in code.
It automatically detects program similarity and reports the similar parts in
different colors.

## Homework Overview

Let assume, you are an instructor or a TA of a course and you want to find
the similarities among students' submitted code for a homework assignment. 
You will use Moss for this job. 

In the homework, the students are tasked to
solve a problem in Java (or any programming language). 
Some skleton codes are provided in a few Java files
(optional) and the students will write their code on top of that. Finally,
each student will submit his/her Java project in a .zip file. The expected 
directory (package) structure of the project is - 
*Student_Name/src/edu/mystate/cs101/hw1*.

## Step 1: Setup Environment 

1. Perl

    (a) Check Perl is installed
    - Open a terminal and run: `perl -v`
    - If Perl is installed, you should see output like "This is perl 5 ..."

    (b) If Perl is not installed, install it from terminal
    - `sudo apt install perl` (Linux)
    - `brew install perl` (macOS)

2. Python 3

    (a) Check Python 3 is installed on your system
    - Open a Terminal and run: `python3 --version`
    - If Python 3 is installed, you should see output showing the version 
      number, like "Python 3.x.y" (where x and y are any number).

    (b) If Python 3 is not installed, follow the official documentation 
    or read the Python wiki 
    [page](https://wiki.python.org/moin/BeginnersGuide/Download) to install it.

## Step 2: Download (or clone) the repo

Download the repo 
[https://github.com/JobayerAhmmed/moss](https://github.com/JobayerAhmmed/moss)
as a zip file and extract it, or clone the repo using git.

## Step 3: Register for Moss [(link)](https://theory.stanford.edu/~aiken/moss/#:~:text=Registering%20for%20Moss)

- Send an email to `moss@moss.stanford.edu`
    - Email subject (optional): registeruser
    - Email body: 
    ```
    registeruser
    mail <email_address>
    ```
    - In the email body, replace **<email_address>** with **your** email address.

- Save the content of the reply email to the *moss.pl* file in the *moss* directory.
- Open a terminal in *moss* directory and set execution permission: `chmod +x moss.pl`

## Step 4: Download Students' Submissions

- Log in to Canvas and go to the course home page
- Go to *Assignments* -> *Homework 1*, 
  (or, homework you want to work on).
- Use the *Download Submissions* link and download all the student submissions 
  as a .zip file.
- Keep the zip file (*submissions.zip*) inside the *moss* directory.

## Step 5: Process Submissions for Moss

- Open a terminal and go to the *moss* directroy
- Run: `python3 main.py`

## Step 6: Upload Submissions to Moss

- Open a terminal and go to the *moss* directroy
- Run: 
    - `./moss.pl -l java -d HW1/submissions_for_moss/*/edu/mystate/cs101/hw1/*.java`
    - You can change this command according to the programming language 
      and the directory structure:
        - -l: programming language (i.e., *java*).
        - -d: submissions are by directory. Files in a directory are taken to
          be part of the same program and reported matches are organized
          accordingly by directory
          (i.e., *HW1/submissions_for_moss/\*/edu/mystate/cs101/hw1/*).
- If the run is success, you will see a message similar to - 

    "Query submitted.  Waiting for the server's response."
 
- Wait a few seconds and the Moss server will return a URL in the terminal 
(like: http://moss.stanford.edu/results/2/5294092300784).
- Copy the URL from the terminal and open it in a browser.
- You should see the Moss report for each student's directory.
- Click on a link and it will open the similarity report for the student.
