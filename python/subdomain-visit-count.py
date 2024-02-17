from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_count = {}

        for cpdom in cpdomains:
            count, domain = cpdom.split(' ')
            count = int(count)

            fragments = domain.split('.')
            for i in range(len(fragments)):
                subdomain = '.'.join(fragments[i:])
                domain_count[subdomain] = domain_count.get(subdomain, 0) + count

        result = []
        for domain, count in domain_count.items():
            result.append(f"{count} {domain}")

        return result
    