class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter 
        
        # 出現頻度数を降順ソート
        freqs = sorted(Counter(s).values(), reverse=True)
        max_frequency = max(freqs)

        # 最大の合計出現頻度数
        # 最大出現頻度が4ならば合計出現頻度数は4+3+2+1=12
        total_frequency = 0
        for i in range(0, max_frequency+1):
            total_frequency += i
        
        unique_freqs = []
        delete_count = 0
        while len(freqs) > 0:
            if len(unique_freqs) >= max_frequency:
                # 全ての出現頻度が出揃った
                break

            freq = freqs.pop(0)
            
            while total_frequency > 0 and freq >= 1:
                if freq not in unique_freqs:
                    unique_freqs.append(freq)
                    break
                else:
                    # すでに選択されているので,頻度を減らしていく
                    freq -= 1
                    delete_count += 1
                    total_frequency -= 1

        if len(freqs) > 0:
            # 選択できなかった文字を全て削除
            delete_count += sum(freqs)
        
        return delete_count