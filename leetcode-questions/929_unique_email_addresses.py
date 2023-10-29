from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            i = 0
            e = ""
            plusFound = False
            while email[i] != "@":
                if not plusFound and email[i] != "." and email[i] != "+":
                    e += email[i]
                elif email[i] == "+":
                    plusFound = True
                i += 1

            e += email[i:]
            unique.add(e)

        return len(unique)
