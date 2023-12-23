# Part 1: Introduction to Telegram Bot

Welcome to Part 2 of the A2SV Remote Second Year Telegram Bot Development Phase! In this section, we'll delve into keybord types in telegram bot using aiogram library. To get a hands on experience you will be building keyboards to take your user's preference and send data based on the user's order. In the Excercise folder there will be a data stored in 

## Getting Started

To begin this exercise, follow these detailed steps (If you haven't done them already):

1. **Clone the Repository / Open the github Codespace:**
   - Use GitHub Codespace for a consistent development environment.
   - Or Clone the repository to your local 

2. **Create Your Branch:**
   - Ensure platform consistency by creating a new branch with the format `[First_Name].[Task].2`.
   - **Task:** Run the command `git checkout -b YourName.Task.2` to create your branch.

3. **Copy Task Folder:**
   - Your submission should be inside the Part_2 directory and it should be within a directory called [Your_first_name]
   - **Task:** After finishing your task, make sure to add a readme and add your deployed bot name to it.

## Task Overview

### 1. Introduction to keyboard types and callbacks for Telegram Bot using Aiogram Library
   - Learn about the keyboard types and callbacks for building your Telegram bot project.
   - **Task:** Read the following [learning material](https://docs.google.com/document/d/1jhgL_lXxaGzKUmxj8Rz-I6jIcLqVJQQMAY2EUcxhH04/edit?usp=sharing).

### 2. Create reply buttons:
   - Use BotFather to create your second Telegram bot. Then build reply buttons
   - **Task:** create reply buttons: Register phone, Register location and one or more custom buttons <br> 
   Note: 
        - All buttons should appear after the `/start` command is sent by the user
        - When Register phone is clicked the user should be prompted to share their phone
        - When Register location is clicked the user should be prompted to share their location
        - When your custom buttons are clicked there must be some visible action
         

### 4.Create inline buttons:
   - On your second Telegram bot you created on step 2, build inline keyboard buttons
   - **Task:** create inline buttons: Register phone and one or more custom buttons <br> 
   Note: 
        - All buttons should appear after the `/start` command is sent by the user
        - When Register phone is clicked the user should be prompted to share their phone via text
        - When your custom buttons are clicked there must be some visible action

### 5. Create other inline buttons with callback:
    - In addition to redirecting to a url inline buttons can be used for doing callback queries
    - **Task:** create other inline buttons: make sure to add callbacks and do some actions

### 6. Host on PythonAnywhere

   - Use the tutorial below to understand how you can host your bot on PythonAnywhere
   - **Task:** Copy all your files and folders within folder to pythonanywhere folder and then run it. Don't forget putting your deployed bot in the readme file within your solution directory.
   Resource: [tutorial](https://youtu.be/mYlM4RWTHnk) (Turn on subtitles and autotranslate to English)
     
### 7. Send a Pull Request
   - Once tasks are completed, send a pull request with your changes.
   - If your solution is accepted, it will be merged, and you can move on to the next task.

Happy coding!
