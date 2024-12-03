from datetime import datetime

class CodeCollaboration:
    def __init__(self):
        self.code = ""
        self.reviews = {}
        self.edit_history = []
        self.merged_code = ""
        self.pending_reviews = 0

    def edit_code(self, user, new_code):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.code = new_code
        self.edit_history.append((user, new_code, timestamp))
        return f"Code edited by {user} at {timestamp}."

    def review_code(self, reviewer, feedback):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.reviews[reviewer] = {'feedback': feedback, 'timestamp': timestamp}
        self.pending_reviews -= 1
        return f"Code reviewed by {reviewer} at {timestamp}. Feedback: {feedback}"

    def request_review(self):
        self.pending_reviews += 1
        return "Review requested. Waiting for feedback."

    def merge_code(self, reviewer):
        if self.pending_reviews == 0:
            self.merged_code = self.code
            return f"Code successfully merged by {reviewer}."
        return "Merge failed: Review required before merge."

    def get_current_code(self):
        return self.code

    def get_merged_code(self):
        return self.merged_code

    def get_reviewers_feedback(self):
        return self.reviews

    def get_edit_history(self):
        return self.edit_history


