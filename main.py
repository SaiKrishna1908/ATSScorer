from model.job import Job
import json

def read_config():
    with open('./config.json', 'r') as f:
        data = json.load(f)        
        return data

def read_file(fileName):
    jd = open(fileName, "r")    
    return jd.read()

def update_file(fileName, tex_content):
    if ".tex" not in fileName:
        fileName = fileName+".tex"
    f = open(fileName, "a")
    f.write(tex_content)
    f.close()

if __name__ == '__main__':
    app_config = read_config()
    print(app_config)
    job_description = read_file(app_config['jobDescription'])
    job = Job(job_description=job_description)
    ats_keywords = job.extract_keywords()    

    latex_file_location = app_config['latexPath']
    latex_content = read_file(latex_file_location)


    