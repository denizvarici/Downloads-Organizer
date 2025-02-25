# Downloads-Organizer
Windows downloads folder organizer developed by python language

How to use on your computer ?
- 
Create a json folder named like "downloadsettings.json" or use the template json file in repository.(It's also called downloadsettings.json)
Open json_helper.py and copy full path of that json file to variable: json_file_path . example : "C:\\Desktop\\JsonFile\\downloadsettings.json"

Create a ".txt" file and edit according to your computer's path the path below:
@echo off
call "C:\Example\Example2\Downloads-Organizer\Program\venv\Scripts\activate"
python "D:\Example\Example2\Downloads-Organizer\Program\script.py"
and save as ".bat" file

Double click to the bat file and it should be work!!

