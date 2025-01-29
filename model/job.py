
from model.core import DeepSeek, MistralModel, SambaNovaCloud


class Job:
    def __init__(self, job_description, model='mistral'):
        self.job_description = job_description
        if model == 'deepseek':
            self.model = DeepSeek()
        elif model == 'mistral':
            self.model = MistralModel()
        else:
            self.model = SambaNovaCloud()

    def extract_keywords(self):
        json_struct = "\{ \"skills:\" [\"skill1\", \"skill2\", \"skill3\"] \}"
        prompt = f'''
            Extract ATS keywords for this job description, give the response in below json format

            {json_struct}

            This is the job description:

            {self.job_description}
        '''
        
        return self.model.call(prompt)

    def extract_skills_section(self):
        prompt = f'''
            I am going to give you a latex file extract the "Skill" section of the latex code and return it back.

        '''
    def include_keywords_in_skills(self, ats_keywords, tex_content):
        prompt = f'''
            I am going to provide tex file which is my resume. Include the following keywords which have been 
            extracted from a job description in the skills section and also add appropriate points in my 
            Professional Experience Section. Feel free to include new sub sections if necessary in "Skills". 
            Update my tex file. Keep my other sections as it is just change my "Skills" and "Professional Experience" sections

            ATS Keywords that are needed to make changes in Skills and Professional Experience:

            {ats_keywords}

            My Resume in Tex

            {tex_content}

            Give complete tex file and don't include intro convo
        '''

        return self.model.call(prompt)    