# Install Dependencies

```
pip install -r requirements.txt
```

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

# Update resume based on your past organization features

If you have experience working in a B2C organization, this script allows you to highlight the features you contributed to, while automatically generating relevant technology stacks based on those features.

#### Example:

If your previous organization focused on educational technology, your work experience might include key features such as:

- **Live Virtual Classrooms**: Facilitated real-time interaction between educators and students using technologies like WebRTC for video conferencing, integrated with a web application framework such as React or Angular.  
- **Learning Management System (LMS)**: Developed and maintained an LMS to organize, deliver, and assess educational courses. Backend development was implemented using Django or Node.js, while frontend development leveraged React or Angular.  
- **Microlearning Programs**: Designed and implemented microlearning modules for improved knowledge retention, using modular content delivery systems with databases like MongoDB for content storage.  

This approach ensures that your resume aligns with industry-standard keywords and technical terminology, improving its ATS compatibility.