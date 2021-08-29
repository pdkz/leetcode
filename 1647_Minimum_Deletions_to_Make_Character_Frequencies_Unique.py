class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter 
        
        freqs = sorted(Counter(s).values(), reverse=True)
        max_frequency = max(freqs)
        total_frequency = 0
        for i in range(0, max_frequency+1):
            total_frequency += i
        
        unique_freqs = []
        delete_count = 0
        while len(freqs) > 0:
            if len(unique_freqs) >= max_frequency:
                break

            freq = freqs.pop(0)
            
            while total_frequency > 0 and freq >= 1:
                if freq not in unique_freqs:
                    unique_freqs.append(freq)
                    break
                else:
                    freq -= 1
                    delete_count += 1
                    total_frequency -= 1

        if len(freqs) > 0:
            delete_count += sum(freqs)
        
        return delete_count