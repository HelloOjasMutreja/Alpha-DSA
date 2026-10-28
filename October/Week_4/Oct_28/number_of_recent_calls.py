class RecentCounter:

    def __init__(self):
        self.RecentCounter = []

    def ping(self, t):
        self.RecentCounter.append(t)

        i = 0

        for stamp in self.RecentCounter:
            if stamp >= t-3000:
                i += 1

        return i

c = RecentCounter()
results = []
for t in [1, 100, 3001, 3002]:
    results.append(c.ping(t))
print(results)     # expect [1, 2, 3, 3]