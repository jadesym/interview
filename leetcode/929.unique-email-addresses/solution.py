class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniques = set()
        for email in emails:
            unique_email = self.getUniqueEmail(email)
            uniques.add(unique_email)
        return len(uniques)
        
    def getUniqueEmail(self, email):
        unique_email = ""
        at_found = False
        plus_found = False
        for letter in email:
            if at_found:
                unique_email += letter
            elif letter == ".":
                continue
            elif letter == "@":
                at_found = True
                unique_email += letter
            elif letter == "+":
                plus_found = True
            elif plus_found and not at_found:
                continue
            else:
                unique_email += letter
        return unique_email
        