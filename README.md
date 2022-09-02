# Acronym
This is an Acronym dictionary search tool.

Advantages compared to Excel file:
- Ability to show all mapped explanations.
- Case insensitive.
- Only 1st column is used as search key, to avoid mis-searching fields.
- No need to arrange records by first-starting-letter.

</br>To use it, simply:
<li> 1. Make sure python version==<strong>3.9.7</strong>, other versions are not tested thus not gurenteed to work. </li>
<li> 2. Open up Windows Command Prompt by searching <strong>cmd</strong> in Windows seaching bar, which is right next to start menu icon.</li>
<li> 3. Change directory to root folder by <code>cd REPLACE_WITH_YOUR_PATH_TO_ROOT_FOLDER</code>. </li>
<li> 4. (Optional) Recommend to create a new virtual environment and activate it. If you have conda installed, refer to <a href="https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands" title="Conda Environment Management">Conda Environment Management</a>. If you don't have conda, you can still do it by <a href="https://docs.python.org/3/library/venv.html" title="venv">venv</a>.
<li> 5. Install required packages in <strong>requirements.txt</strong>. Command: <code>pip install -r requirements.txt</code></li>
<li> 6. Put <strong>Acronym dictionary.xlsx</strong> into root folder. </li>
<li> 7. Run the app by typing <code>python app.py</code> in Windows Command Prompt, make sure the location is set to root folder and python is installed correctly.</li>

</br>Note: if package installation process encounters connection problem, try to add CRAN from <strong>tsinghua mirror</strong> by <code>pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple</code>, then try <strong>step 2</strong> again.
