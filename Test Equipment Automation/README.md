# SmallPythonProjects
Just small Python projects.

## List of available projects:

**Recursive To-Do list**

 >Just a small Python terminal To-Do list.
 It's recursive.
 You can add/remove and view your items, exit on command.

---

**Web Scraping with Selenium into a CSV with Pandas**
 
 >Scrape a website full of basketball player Data.
 Get players names and salaries.
 Import into a CSV.
 
 ---
 
 **Test Equipment Automation**
 - Keysight N5182B Signal Generator
 
 >Automate the N5181B Signal Generator.
 >You can choose Frequency and Amplitude, the program will go from one amplitude to another with user chosen steps.
 >Turns RF Output ON at start and OFF when done.<br>
 
 - Tektronix FCA3031 Timer/Counter Analyzer
 
 >Automate the FCA3031 Counter.
 >The program will take samples of time interval between INPUT1 and INPUT2 from the counter every second, into a csv file.
 >Everytime the program is run it will make a new file with date and time stamp for easier data management<br>
 
 >Required pyvisa python library, can be installed with:
``` 
pip3 install -U pyvisa
```
 
 > NI-VISA is neccesery as backend, found at:
 > https://pyvisa.readthedocs.io/en/latest/faq/getting_nivisa.html<br>
 > The commands are taken from the respective programmers guide, included in the folder.
 
 ---
