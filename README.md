# githubkm
The project has been created on **13th March 2021**.
***
 ## Project Title: Analysis of Bikeshare Data
 ***
Filter bikesharing data based on local and time preferences:

*1. Chicago*  
*2. New York City*  
*3. Washington*  

Filter data by:

- a *selectable month* or
- a *selectable day of the week*.  

Corresponding statistics are provided.
  
chicago.csv  
new_york_city.csv  
washington.csv 

The following sources were used:  
 **1:** https://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.mode.html     
 **2:** https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
 **3:** https://stackoverflow.com/questions/43983622/remove-unnamed-columns-in-pandas-dataframe  
 **4:** https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe
 **5:** https://stackoverflow.com/questions/50848454/pulling-most-frequent-combination-from-csv-columns  

### Updates and Revisions

The project started in March 2021 considering referring to data files Chicago.csv, New York City.csv and Washington.csv. Currently, no updates have been made.

 An extension of the project to include data from other cities is being considered.

### Required Software
The following software requirements apply:
 - **Python 3**, **NumPy** and **Pandas** should be installed using [Anaconda][1]  
 - a text editor like Atom
 - a terminal application (Terminal on Mac and Linux or Cygwin on Windows)  

 [1]: https://www.anaconda.com/products/individual#windows "Anaconda"

 To test if you can run Anaconda, enter  
 ```
 conda --version
 ```
 in your terminal/Anaconda prompt. This should print the version number of your installation.

 #### Install NumPy using Anaconda ####
 NumPy is included with Anaconda. In case of a necessary version upgrade/downgrade, use the following command in the Terminal/Anaconda prompt:  
 ```
 # Use either one command  

 pip install --upgrade numpy==X.XX    
 conda install numpy=X.XX
 ```   
 (where *X.XX* is the specific version number)

 #### Install Pandas using Anaconda ####
 Pandas is included with Anaconda. Pandas version 0.22 is used. Check which version you have by using the command.
 ```
 conda list pandas
 ```
 in your Anaconda prompt or the command
 ```
 !conda list pandas
 ```
 in your Jupyter Notebook.  
 If you have another version of Pandas installed in your computer, update your version by typing
 ```
 conda install pandas=0.22
 ```
 in the Anaconda prompt.

 To get started with JupyterLab/Jupyter Notebook use the following commands in your Terminal:  
 ```
 pip install jupyterlab  
 jupyter-lab  
 pip install notebook  
 jupyter notebook
 ```
