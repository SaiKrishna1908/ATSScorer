
from model.core import MistralModel


class Job:
    def __init__(self, job_description):
        self.job_description = job_description
        self.model = MistralModel()

    def extract_keywords(self):
        json_struct = "\{ \"skills:\" [\"skill1\", \"skill2\", \"skill3\"] \}"
        prompt = f'''
            Extract ATS keywords for this job description, give the response in below json format

            {json_struct}

            This is the job description:

            {self.job_description}
        '''
        # print(prompt)
        return self.model.call(prompt)

    def include_keywords_in_skills(self, ats_keywords):
        prompt = f'''
            I am going to provide tex file which is a my resume. Include the following keywords which have been 
            extracted from a job description in the skills section. Feel free to create sub-sections in "Skills" section 
            if necessary and give back just the tex code

            ATS Keywords:

            {ats_keywords}
        '''

        return self.model.call(prompt)

    def include_keywords_in_experience():
        return None