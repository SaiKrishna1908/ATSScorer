from model.core import DeepSeek, GeminiModel, MistralModel, SambaNovaCloud


class Job:
    def __init__(self, job_description, model='gemini'):
        self.job_description = job_description
        if model == 'deepseek':
            self.model = DeepSeek()
        elif model == 'mistral':
            self.model = MistralModel()
        elif model == 'gemini':
            self.model = GeminiModel()
        else:
            self.model = SambaNovaCloud()

    def extract_keywords(self):
        json_struct = "\{ \"skills:\" [\"skill1 \", \"skill2\", \"skill3\"] \}"
        prompt = f'''
            Extract ATS keywords for this job description, give the response in below json format.

            {json_struct}

            This is the job description:

            {self.job_description}
        '''
        
        return self.model.call(prompt)    
        
    def include_keywords_in_skills(self, ats_keywords, tex_content, job_title, previous_job_experience=''):

        prompt = f'''
                I am providing my resume in TeX format. Modify only the Skills section while keeping all other sections unchanged.

                Skills Section:

                Incorporate the appropriate provided ATS keywords naturally into this section.
                Feel free to introduce new subsections if necessary to categorize the skills effectively.
                
                Job Title Update:

                Change my current job title to {job_title} wherever applicable.

                ATS Keywords: \n{ats_keywords}\n

                My Tex Content: \n{tex_content}                
            
                Output Instructions:
                - Do NOT include any introduction, explanation, or summary in your response.  
                - ONLY return the complete updated TeX file.
                - replace "&" with "\&"                       
            '''

        return self.model.call(prompt)    

    def include_skills_in_professional_experience(self, ats_keywords, tex_content, previous_job_experience=''):
        if previous_job_experience != '':
            job_experience_prompt = f'''
            These are the features offered by the organization I previously worked on. For each feature create a 
            point in professional experience with the ATS skills I provided.

            {previous_job_experience}

            '''

        prompt = f'''

        I am providing my resume in TeX format. Modify only the Professional Experience sections while keeping all other sections unchanged.

        Professional Experience Section:

        Update Professional Experience section by adding relevant bullet points that demonstrate my experience with the given ATS keywords.
        Ensure that the modifications align with my previous roles and responsibilities while making them more relevant to the target job.
        Include specific numbers for each point you add to quantify impact
                
        Rewrite or refine existing bullet points where necessary to improve clarity and impact.


        ATS Keywords: \n{ats_keywords}\n

        My Resume in Tex Content: \n{tex_content}\n

        \n{job_experience_prompt}\n

        \nTake these points into consideration, when rewriting\n
        \nDo not use buzz words\n
        \nAvoid using repetitive action verbs, if they are present replace them\n

        Output Instructions:
                - Do NOT include any introduction, explanation, or summary in your response.  
                - ONLY return the complete updated TeX file.
                - replace "&" with "\&"       
                - emphasize important skills using bold font:  {{\\bf <keyword>}} example {{\\bf springboot}}
        '''
        
        return self.model.call(prompt)