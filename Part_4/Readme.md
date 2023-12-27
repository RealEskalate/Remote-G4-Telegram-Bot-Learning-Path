# Part 4: Connecting To Database and Adding Webhook

Welcome to Part 4 of the A2SV Remote Second Year Telegram Bot Development Phase! In this section, we'll transition from temporary storage using FSM to permanent storage in mongodb or any of your favorite storage space using aiogram library. To get a hands on experience you will be implementing commands that will register user, get all users registered so far, get one user using his/her Id, filter users by name, update one user by his/her ID, delete one user by his/her Id. You will also get chance to look at web hook concept and experiment with it.

## Getting Started

To begin this exercise, follow these detailed steps (If you haven't done them already):

1. **Clone the Repository / Open the github Codespace:**
   - Use GitHub Codespace for a consistent development environment.
   - Or clone the repository to your local 

2. **Create Your Branch:**
   - Ensure platform consistency by creating a new branch with the format `[First_Name].[Task].4`.
   - **Task:** Run the command `git checkout -b YourName.Task.4` to create your branch.

3. **Create Your Solutions Folders:**
   - Your submission should be inside the Part_4 directory and it should be within a directory called [Your_first_name] and [Your_first_name_webhook] for the database and webhook tasks respectively
   - **Task:** After finishing your task, make sure to add a readme and add your deployed bot name to it.

## Task Overview

### 1. Introduction to connecting to database and adding webhook
   - Learn about the concept of FSM and storage for building your Telegram bot project.
   - **Task:** Read the following [learning material](https://docs.google.com/document/d/1ny7-xi52rpzLJTOwYFy4CVlmPbEYhRiGwwTkoa-YB5s/edit?usp=sharing).

### 2. Create a telegram bot that registers users and store their data on temporary storage then on Mongodb or any of your prefered database:
   - Use BotFather to create your fourth telegram bot with commands that will register user, get all users registered so far, get one user using his/her Id, filter users by name, update one user by his/her ID, delete one user by his/her Id.
   - **Task:** Build a telegram bot that registers users and store their data on temporary storage then on to permanenet databeth. After successfull operation the bot should return the registered data back to the user.
   - **Note:** If you intend to use mongo db you can check out the Exercise folder. It already has a MongoDb atlas set and its mongodb URL is found on config.py.
   - **Note:** ⚠⚠⚠⚠ If you decide to use the database set in Exercise folder, make sure to go to Part_4/Exercise/database/loader.py then change the database name to [Your_First_Name].⚠⚠⚠⚠ The collection name can stay the same as 'myCollection' <br>
     ![image](https://github.com/RealEskalate/Remote-G4-Telegram-Bot-Learning-Path/assets/62964622/be194bdc-ce1c-4c54-a530-241104f7cb9c)


### 3. Implement a webhook to one of your previous bots or a new one
    - Use the resources provided in the learning materials and push a folder with a telegram bot that has incorporated a webhook
   - **Task:** Create a telegram bot that has webhook implementation inside a folder [Your_first_name_webhook] then submit
   - **Note:** You can add webhook to one of your previous bots or create a new one
      
### 4. Host on PythonAnywhere

   - Use the tutorial below to understand how you can host your bot on PythonAnywhere
   - **Task:** Copy all your files and folders within folder to pythonanywhere folder and then run it. Don't forget putting your deployed bot in the readme file within your solution directory.
   Resource: [tutorial](https://youtu.be/mYlM4RWTHnk) (Turn on subtitles and autotranslate to English)
     **Note:**  Make sure to kill the consoles of your previous tasks since python anywhere only gives you 2 consoles at a time
### 5. Send a Pull Request
   - Once tasks are completed, send a pull request with your changes.
   - If your solution is accepted, it will be merged, and you can move on to the next task.

Happy coding!
