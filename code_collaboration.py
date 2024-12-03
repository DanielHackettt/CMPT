class CodeCollaboration:
    def __init__(self):
        self.code = ""
        self.reviews = {}
        self.edit_history = []
        self.merged_code = ""

    
    def edit_code(self, user, new_code):
        self.code = new_code
        self.edit_history.append((user, new_code))
        return f"Code edited by {user}."

  
    def review_code(self, reviewer, feedback):
        self.reviews[reviewer] = feedback
        return f"Code reviewed by {reviewer}. Feedback: {feedback}"

    
    def merge_code(self, reviewer):
        if reviewer in self.reviews:
            self.merged_code = self.code
            return f"Code successfully merged by {reviewer}."
        return "Merge failed: Review required before merge."

  
    def get_current_code(self):
        return self.code

   
    def get_merged_code(self):
        return self.merged_code


