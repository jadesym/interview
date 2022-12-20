class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = []
        domain_map = {}
        for domain in cpdomains:
            countDomain = domain.split(' ')
            count = int(countDomain[0])
            parts = countDomain[1].split('.')
            for i in range(len(parts)):
                part_domain = '.'.join(parts[i:])
                if part_domain in domain_map:
                    domain_map[part_domain] += count
                else:
                    domain_map[part_domain] = count
        return [str(v) + ' ' + k for k,v in domain_map.items()]