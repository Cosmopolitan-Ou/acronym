# Acronym
This is an Acronym dictionary search tool.

Advantages compared to Excel file:
- Ability to show all mapped explanations.
- Case insensitive.
- Only 1st column is used as search key, to avoid mis-searching fields.
- No need to arrange records by first-starting-letter.

</br>To use it, simply:
<li> 1. Make sure python version==3.9.7, other versions are not tested thus not gurenteed to work. </li>
<li> 2. Change directory to root folder by <strong>cd REPLACE_WITH_YOUR_PATH_TO_ROOT_FOLDER</strong>. </li>
<li> 3. Install required packages in requirements.txt, recommend to create a new virtual environment for it. Command: </li>
    > pip install -r requirements.txt
<li> 4. Put <strong>Acronym dictionary.xlsx</strong> into root folder. </li>
<li> 5. Run the app by typing <strong>python app.py</strong> in console, make sure the location is set to root folder and python is installed correctly.</li>

</br>Note: if pip install encounter connection problem, try to add CRAN from tsinghua mirror by <strong>pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple</strong>, then try <strong>step 2</strong> again.
