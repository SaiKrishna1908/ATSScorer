
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
        
    def include_keywords_in_skills(self, ats_keywords, tex_content, job_title, previous_job_experience=''):
        
        # if previous_job_experience != '':
        #     job_experience_prompt = f'''
        #     I previously worked at {previous_job_experience}. Scrape their website to identify the services and features they developed.

        #     - Use the extracted features and services to add relevant, impactful bullet points to my work experience.  
        #     - Naturally incorporate the provided ATS keywords while ensuring the descriptions align with my role and responsibilities.  
        #     - Maintain a concise and results-driven format for each bullet point.

        #     '''

        prompt = f'''
                I am providing my resume in TeX format. Modify only the Skills and Professional Experience sections while keeping all other sections unchanged.

                Skills Section:

                Incorporate the provided ATS keywords naturally into this section.
                Feel free to introduce new subsections if necessary to categorize the skills effectively.


                Professional Experience Section:

                Update this section by adding relevant bullet points that demonstrate my experience with the given ATS keywords.
                Ensure that the modifications align with my previous roles and responsibilities while making them more relevant to the target job.
                
                Rewrite or refine existing bullet points where necessary to improve clarity and impact.                
                
                Job Title Update:

                Change my current job title to {job_title} wherever applicable.

                ATS Keywords: {ats_keywords}

                My Tex Content: {tex_content}
            
                Output Instructions:
                - Do NOT include any introduction, explanation, or summary in your response.  
                - ONLY return the complete updated TeX file.
            '''

        return self.model.call(prompt)    