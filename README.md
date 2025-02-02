# Install MiKTex

```
MikTex.bat
```

# Add MiKTex to your PATH

```
C:\miktex-portable\texmfs\install\miktex\bin\x64\
```

# Setting up the input folder

Place your resume which is in tex format in the ./in/base_resume folder. The script recognizes the cls files 
and copies to out folder automatically

# Job Description

By default jd is placed as plain text inside jd.txt under `in` folder. This behaviour can be changed in `config.json`

# Config.json

```
jobDescription: Path where the jd is present. jd must be a txt file
latexPath: Path where the resume is present in latex file
jobName: This if field is currently used to name the output pdf in the "out" folder
jobTitle: This script recognizes the job title in your resume and replaces it with this field.
```

# Run the script


```
python ./main.py
```

# Out Folder

your updated pdf file is present in the out folder along with the updated tex file