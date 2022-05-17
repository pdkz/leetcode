class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = collections.Counter()
        for addr in emails:
            account, domain = addr.split('@')
            names = account.split('+')
            firstname = names[0]
            
            name = ''.join(firstname.split('.'))
            
            d['@'.join([name, domain])] += 1
    
        return len(d.keys())
