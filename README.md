Name	: Dihya Fauzan Haryadi

NPM	    : 2506637003

Class	: PBP KKI

## Assignment 1
1.  The design of my portfolio website are mostly based on the tutorial design with some minor edit and addition to fit the criteria of Assignment 1. As for the use of HTML5's semantic elements i use <section> to make my code much more organized and easy to read especialy to separate the Main profile with the about me part, while also making it much more easy to be customized in CSS.

2.  I fortunately did not encounter this problem wether when i open it using dekstop or mobile, however on dekstop mode whilst on window when i try to make the window to a much more potrait view i saw that the image on the website positioned itself between the name and the little about me section, but i don't see this as a problem as it doesn't cause an overlap or an error.

3.  When testing the Email button on the website it redirects the user to an external app in my case it open an app named "Outlook" which other than unfamiliar for me i'd much rather to be able to direct the user to Google mail or have the email address be visible rather than in the form of a link that much prefers the user's operating system and not the user preference. Other than that i would like to implement some animation to my website. 

AI disclosure
    I use Gemini AI to guide me on this assignment. I mostly use it to help me adding a background colour and manage the spacing above and below the About me section as well as helping how to create a new section on my website. Other than that, the website is created based on the orders from the previous tutorials.

## Assignment 2
Reflective Questions

When a user send a request from their browser the first thing that happen is the request gets fetched by urls.py which is the project, and then urls.py would read the first part of the URL address, then using the function path("",include(mainApplication.urls")) the request would then be passed to the internal route file of the application. After that the file would then receive an operand route and check the rest of the URL address, which would call those specific data processing function inside the view file. Then the View file would ask for the data that are needed for the Model, after the Model gave the data that it needed to the database, View would wrapped the data into a dictionary named context, and then it will call the Template HTML to be rendered. The Model here acts as the bridge between python and the database. When getting asked by View, Model would translate the code from python to become a query SQL that can retrieve data and project from the database, and then give it to View in the form of a Python code. Lastly the Template is the one that receive the data from View in the form of Context, combining those data into the HTML frame and producing a static HTML file that is send back to the browser of the user.

Through the aspect of Application maintenance, the use of Model helps us adding or changing the data instantly without touching the program code, completely bypasing the need to use git add, commit, and push, making the future edit on the page much easier and safer.

For Future Development, the data that is kept inside the Model are flexible and reusable, therefore if in the future there were to be a situation that needed the similar feature, they can easily edit a few part of it rather than creating a code that woks in similar fashion from scratch.

makemigrations serve as a bluprint for the migrate action, it is tasked to scan models.py to see if there are any changes, if there is Django would create a new instruction file inside the migrations/ folder. This action wouldn't affect the database since it only note for the plans of changing in a python text file.
migrate would then execute those plans, it would read the instruction files inside migrations/ and execute the instruction that has never been runned, which would affect the database.

As an example, in my program inside models.py i wrote "score = models.IntegerField(blank=True, null=True)" which i needed to run makemigrations so Django could detect the change and write a file to plan for migrate, and then after i run migrate, Django now can create a column titled score inside the database table. Withouse both of these action, the aplication would experience OperationalError when trying to store the scores data.

AI disclosure: I use Gemini AI to help with editing the new page titled "certificate" where it would showcase pictures of my real life certificates. By copying the template on tutorial 2, i make some edit to fit my picture for this page such as adding the feature to add and show the image on the page and in here is where i use the AI to help me tackle some mistakes and errors. And also when opening the site through PWS there are some troubleshooting needed to be done since the application i created used a python app called Pillow and Gemini gave me some tips and the method so that the app can run on PWS.