import pdflatex
from model.job import Job
import json
import subprocess
import os
import shutil

def read_config():
    with open('./config.json', 'r') as f:
        data = json.load(f)        
        return data

def read_file(fileName):
    jd = open(fileName, "r")    
    return jd.read()

def write_file(fileName, tex_content):
    if ".tex" not in fileName:
        fileName = fileName+".tex"
    
    folder_path = os.path.dirname(fileName)
    if folder_path and not os.path.exists(folder_path):
        os.makedirs(folder_path)

               
    f = open(fileName, "w")
    f.write(tex_content)
    f.close()

def convert_tex_to_pdf(filePath, pdfFileName):
    output_dir = '/'.join(filePath.split('/')[:-1])
    print(output_dir)
    os.chdir(output_dir)
    subprocess.run(['pdflatex', filePath.split('/')[-1]])

def copy_cls_files(src_folder, dest_folder):    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        
    for file in os.listdir(src_folder):
        if file.endswith(".cls"):            
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)
            shutil.copy2(src_path, dest_path)  # Copies with metadata

    print(f"Copied all .cls files from {src_folder} to {dest_folder}")

if __name__ == '__main__':
    app_config = read_config()    
    job_description = read_file(app_config['jobDescription'])
    job = Job(job_description=job_description)
    ats_keywords = job.extract_keywords()    

    latex_file_location = app_config['latexPath']
    latex_content = read_file(latex_file_location)

    pdf_file_name = app_config['jobName']

    job_title = app_config['jobTitle']

    prev_job_experience_file_path = app_config['previousJobExperience']
    prev_job_experience = read_file(prev_job_experience_file_path)
    
    updated_latex = job.include_keywords_in_skills(ats_keywords, latex_content, job_title, prev_job_experience)    
    updated_latex = job.include_skills_in_professional_experience(ats_keywords, updated_latex, prev_job_experience)
    copy_cls_files("./in/base_resume", "out/")
    write_file(f'./out/{pdf_file_name}.tex', updated_latex)
    convert_tex_to_pdf(f'./out/{pdf_file_name}.tex', f'./out/{pdf_file_name}.pdf')


    